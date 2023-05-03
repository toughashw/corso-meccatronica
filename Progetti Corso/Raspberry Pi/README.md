# Steps Installazione e prima configurazione Raspberry Pi
(https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-11-08/2021-10-30-raspios-bullseye-armhf-full.zip)

> Steps Installazione
- Download Sistema Operativo Raspy Linux (https://www.raspberrypi.com/software/operating-systems/)
- Preparazione MicroSD e caricamento Immagine Sistema Operativo (https://www.balena.io/etcher)
- Preparazione file ssh e wpa_supplicant.conf e caricamento su MicroSD 
- Installazione Sistema Operativo 
- Individuazione hostmane/indirizzo IP (https://angryip.org)
- Primo accesso via SSH 
```
ssh pi>@ip/hostname
default user: pi | default password: raspberry | default hostname: raspberrypi
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

- Installazione GIT e controllo versione
```
sudo apt-get install git -y
```
```
git --version
```

- Installazione GIT e controllo versione
```
sudo apt-get install git -y
```
```
git --version
```

- Installazione Python e controllo versione
```
sudo apt-get install python
```
```
sudo apt-get install python3
```
```
python --version
```
- Installazione PIP e controllo versione
```
sudo apt install python3-pip
```
```
pip3 --version
```

- Comandi GPIO e controllo manuale
```
pinout
```
- WiringPI
```
sudo apt-get install wiringpi
```
(http://wiringpi.com/the-gpio-utility/)