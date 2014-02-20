#Des-Instalador de Curavi
#Kevin Rafael Sarmiento Mendoza
#mkdir07[at]gmail[dot]com

echo "  ____                      _    ___        _ "
echo " / ___|   _ _ __ __ ___   _(_)  / _ \      / |"
echo "| |  | | | | '__/ _\` \ \ / / | | | | |     | |"
echo "| |__| |_| | | | (_| |\ V /| | | |_| |  _  | |"
echo " \____\__,_|_|  \__,_| \_/ |_|  \___/  (_) |_|"

echo;
echo "Desinstalando Curavi"
files/INSTALL.py
echo "Eliminando Imagenes..."
cat files/pass | sudo -S rm /usr/share/pixmaps/Danger.png /usr/share/pixmaps/Warning.png /usr/share/pixmaps/Ok.png /usr/share/pixmaps/Seek.png /usr/share/pixmaps/AcercaDe.png /usr/share/pixmaps/CuraviApplet.png
sleep 1
echo;
echo "Eliminando Archivos..."
cat files/pass | sudo -S rm /usr/local/Curavi/*
sleep 1
echo "Eliminando Directorio..."
cat files/pass | sudo -S rmdir /usr/local/Curavi/
sleep 1
echo "Eliminando Bonobo Server..."
cat files/pass | sudo -S rm /usr/lib/bonobo/servers/GNOME_CuraviApplet.server
echo "Curavi Applet ha sido desinstalado de su sistema"
exit 0


