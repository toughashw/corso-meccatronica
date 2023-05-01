# Steps Installazione e prima configurazione Raspberry Pi

> Steps Installazione
- Download Sistema Operativo Raspy Linux (https://www.raspberrypi.com/software/operating-systems/)
- Preparazione MicroSD e caricamento Immagine Sistema Operativo (https://www.balena.io/etcher)
- Preparazione file ssh e wpa_supplicant.conf e caricamento su MicroSD 
- Installazione Sistema Operativo 
- Individuazione hostmane/indirizzo IP (https://angryip.org)
- Primo accesso via SSH 
```
ssh <raspberrydefaultuser>@<raspberryipaddress>
default hostname: pi | password: raspberry
```

- Installazione e Configurazione VNC 
```
sudo raspi-config
```
```
sudo apt-get update -y && sudo apt-get upgrade -y
```
```
sudo apt-get install realvnc-vnc-server
sudo apt-get install realvnc-vnc-viewer
```
