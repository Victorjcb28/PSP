#Probado en Ubuntu 16.04

#Instalar wxglade
sudo apt-get update <br>
sudo apt-get install wxglade

#Wine
sudo dpkg --add-architecture i386<br>
sudo add-apt-repository ppa:wine/wine-builds<br>
sudo apt-get update<br>
sudo apt-get install --install-recommends wine-staging<br>
sudo apt-get install winehq-staging

#sqlite
1)Abrir con click derecho -> wine -> descargar mono<br>
2)Instalar Gecko (automaticamente)
