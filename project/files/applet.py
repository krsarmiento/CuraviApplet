#!/usr/bin/python2



#    This file is part of Curavi Applet.
#    Copyright (C) 2011  Kevin Rafael Sarmiento Mendoza

#    Curavi Applet is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Curavi Applet is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Curavi Applet.  If not, see <http://www.gnu.org/licenses/>.




import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet

import sys
import commands
import gobject


class CuraviApplet(gnomeapplet.Applet):
    
    #Diccionario que guardara los datos
    Data = {'APM_LEVEL': '', 'LOAD_CYCLE_COUNT':''};
    
    file = open('/home/mkdir/Documentos/Applets/pass','r')
    password = file.readlines()[0].partition('\n')[0]
    
    #Comandos
    loadCycleCommand = 'smartctl -a /dev/sda | grep Load | cut -d \' \' -f 40'
    apmLevelCommand = 'hdparm -B /dev/sda | column -s \' \' | cut -d \' \' -f 3'
    
    
    def cambiarNivel(self, nivel):
        self.comandoCambiarNivel = 'hdparm -B'+str(nivel)+' /dev/sda'
        commands.getoutput('echo %s|sudo -S %s' % (self.password, self.comandoCambiarNivel))
    
    def monitorear(self):
        
        #Ejecutamos y guardamos la salida
        output = commands.getoutput('echo %s|sudo -S %s && echo %s|sudo -S %s' % (self.password, self.loadCycleCommand, self.password, self.apmLevelCommand))
        
        #Dividimos la salida por lineas
        lines = output.split('\n')
        
        #Guardamos los valores en un diccionario
        try:
            int(lines[0].split(' ')[0])
            int(lines[1].split(' ')[0])
            self.Data['LOAD_CYCLE_COUNT'] = lines[0].split(' ')[0];
            self.Data['APM_LEVEL'] = lines[1].split(' ')[0];
        except:
            int(lines[0].split(' ')[1])
            int(lines[1].split(' ')[1])
            self.Data['LOAD_CYCLE_COUNT'] = lines[0].split(' ')[1];
            self.Data['APM_LEVEL'] = lines[1].split(' ')[1]; 

                
        
        return ""+self.Data['LOAD_CYCLE_COUNT']+","+self.Data['APM_LEVEL']
    
    def analizarEstado(self, apmLevel):
        
        apmLevel = int(apmLevel)
        
        if apmLevel == 254:
            self.tooltips.set_tip(self.image, "Cuidando al maximo el disco duro")
            return "/usr/share/pixmaps/Ok.png"
        elif apmLevel < 254 and apmLevel>200:
            self.tooltips.set_tip(self.image, "Equilibrio entre bateria y disco duro")
            return "/usr/share/pixmaps/Warning.png"
        else:
            self.tooltips.set_tip(self.image, "Ahorro maximo de bateria pero poco cuidado del disco duro")
            return "/usr/share/pixmaps/Danger.png"
            
    
    def mostrarEstado(self):
        self.monitorear()
        self.crearMenu(self.applet);
        self.image.set_from_file(self.analizarEstado(self.Data['APM_LEVEL']))
        return True
    
    
    def crearMenu(self, applet):
        
        self.monitorear()
        
        xml="""<popup name="button3">
        
                    <menuitem name="ItemLoadCycleCount" 
                      verb="Load"
                      label="_# de Ciclos: """+(self.Data['LOAD_CYCLE_COUNT'])+""" "
                      pixtype="stock" 
                      pixname="gtk-load-cycle-count"/>
                      
                      <submenu name="APM" _label="_Nivel APM">
                          <menuitem name="ItemAPMLevel" 
                          verb="Level"
                          label="_Nivel APM:   """+(self.Data['APM_LEVEL'])+""" "
                          pixtype="stock" 
                          pixname="gtk-apm-level"/>
                          
                          <separator/>
                          
                          <menuitem name="ItemVerde" 
                          verb="Verde"
                          label="_Cuidado alto"
                          pixtype="stock" 
                          pixname="gtk-apm-verde"/>
                          
                          <menuitem name="ItemNaranja" 
                          verb="Naranja"
                          label="_Cuidado medio"
                          pixtype="stock" 
                          pixname="gtk-apm-naranja"/>
                          
                          <menuitem name="ItemRojo" 
                          verb="Rojo"
                          label="_Cuidado bajo"
                          pixtype="stock" 
                          pixname="gtk-apm-rojo"/>
                      </submenu>
        
                    <separator/>
        
                    <menuitem name="ItemPreferencias" 
                      verb="Preferencias"
                      label="_Cambiar password"
                      pixtype="stock" 
                      pixname="gtk-preferences"/>
                      
                    <menuitem name="ItemReporte" 
                      verb="Reportar"
                      label="_Ver Reporte"
                      pixtype="stock" 
                      pixname="gtk-report"/>
                      
                      <separator/>
                      
                    <menuitem name="ItemAcercaDe" 
                      verb="Acerca" 
                      label="_Acerca de" 
                      pixtype="stock" 
                      pixname="gtk-about"/>
                </popup>"""
    
        verbs = [('Acerca', self.ventanaAcercaDe), ('Preferencias', self.ventanaPreferencias), 
                 ('Verde', self.opcionVerde), ('Naranja', self.opcionNaranja), ('Rojo', self.opcionRojo)
                 ,('Reportar', self.mostrarReporte)];
        applet.setup_menu(xml, verbs, None)
    
    
    def ventanaAcercaDe(self, *arguments):
        dialog = gtk.Dialog()
        logo = gtk.Image()
        logo.set_from_file("/usr/share/pixmaps/AcercaDe.png")
        dialog.vbox.pack_start(logo, True, True, 0)
        logo.show()
        dialog.show()
    
       
    def ventanaPreferencias(self, *arguments):
        self.dialog = gtk.Dialog()
        
        self.entrada = gtk.Entry(max=0)
        self.entrada.set_visibility(False)
        
        self.dialog.vbox.pack_start(self.entrada, True, True, 0)
        
        boton = gtk.Button("Guardar")
        boton.connect("clicked", self.guardarPass, "Yea!")
        
        self.dialog.vbox.pack_start(boton, True, True, 0)
        
        boton.show()
        self.entrada.show()
        self.dialog.show()
        
        
    def guardarPass(self, *arguments):
        self.password = self.entrada.get_text();
        self.dialog.destroy()
        
    def opcionVerde(self, *arguments):
        self.cambiarNivel(254)
        
    def opcionNaranja(self, *arguments):
        self.cambiarNivel(230)
        
    def opcionRojo(self, *arguments):
        self.cambiarNivel(130)
        
    def mostrarReporte(self, *arguments):
	home = commands.getoutput('echo $HOME')
        output = commands.getoutput('echo %s|sudo -S smartctl -a /dev/sda' % (self.password))
        archivo = open(home+'/.reporte', 'w')
        archivo.write(output)
	archivo.close()
        output = commands.getoutput('gedit ~/.reporte')
    
    def __init__(self, applet, iid):
        
        self.tooltips = gtk.Tooltips()
        
        self.timeout_interval = 1000 * 2  #2 segundos
        self.applet = applet
        
        self.image = gtk.Image()
        self.image.set_from_file('/usr/share/pixmaps/Seek.png')
        self.applet.add(self.image)
        
        self.tooltips.set_tip(self.image, "Detectando estado...")
        
        self.crearMenu(applet)
        applet.show_all()
        gobject.timeout_add(self.timeout_interval, self.mostrarEstado)
        print('Factory started')


def applet_factory(applet, iid):   
    CuraviApplet(applet, iid)
    return gtk.TRUE

#Debugging
if len(sys.argv) == 2:
    if sys.argv[1] == "-d": #Debug mode
        main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        main_window.set_title("Python Applet")
        main_window.connect("destroy", gtk.main_quit)
        app = gnomeapplet.Applet()
        applet_factory(app,None)
        app.reparent(main_window)
        main_window.show_all()
        gtk.main()
        sys.exit()



if __name__ == '__main__':   # testing for execution
    print('Starting factory')
    gnomeapplet.bonobo_factory('OAFIID:GNOME_CuraviApplet_Factory', gnomeapplet.Applet.__gtype__, 'Curavi applet', '0.1', applet_factory)
