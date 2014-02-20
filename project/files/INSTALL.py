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




import gtk
def responderAlDialogo(entry, dialog, response):
    dialog.response(response)
def obtenerTexto():
    
    dialogo = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    
    dialogo.set_markup('<b>Curavi v0.1</b>')
    
    entrada = gtk.Entry()
    entrada.set_visibility(False)
    
    entrada.connect("activate", responderAlDialogo, dialogo, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Password:"), False, 5, 5)
    hbox.pack_end(entrada)
    #some secondary text
    dialogo.format_secondary_markup("Esto sera usado para propositos de <i>identificacion</i>")
    #add it and show it
    dialogo.vbox.pack_end(hbox, True, True, 0)
    dialogo.show_all()
    #go go go
    dialogo.run()
    texto = entrada.get_text()
    dialogo.destroy()
    return texto
if __name__ == '__main__':
    file = open("files/pass", "w")
    file.write(obtenerTexto()+'\n')
    file.close()
