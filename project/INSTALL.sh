#Instalador de Curavi
#Kevin Rafael Sarmiento Mendoza
#mkdir07[at]gmail[dot]com

echo "  ____                      _    ___        _ "
echo " / ___|   _ _ __ __ ___   _(_)  / _ \      / |"
echo "| |  | | | | '__/ _\` \ \ / / | | | | |     | |"
echo "| |__| |_| | | | (_| |\ V /| | | |_| |  _  | |"
echo " \____\__,_|_|  \__,_| \_/ |_|  \___/  (_) |_|"

echo;
echo "Bienvenido a la instalacion de Curavi"
files/INSTALL.py
echo "Copiando Imagenes..."
cat files/pass | sudo -S cp files/images/*.png /usr/share/pixmaps
sleep 1
echo;
echo "Creando Directorio..."
cat files/pass | sudo -S mkdir /usr/local/Curavi/
sleep 1
echo "Copiando Applet..."
cat files/pass | sudo -S cp files/applet.py /usr/local/Curavi/
sleep 1
echo "Iniciando Permisos..."
cat files/pass | sudo -S cp files/pass /usr/local/Curavi/
sleep 1
echo "Copiando Bonobo Server..."
cat files/pass | sudo -S cp files/GNOME_CuraviApplet.server /usr/lib/bonobo/servers
sleep 1
echo "Finalizando instalacion..."
cat files/pass | sudo -S rm files/pass
gedit README
exit 0


