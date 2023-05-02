# Fundamentals of SSH
> Discover Raspberry IP Address under LAN
- [Angry IP Scanner] (https://github.com/angryip/ipscan/releases/download/3.8.2/ipscan-3.8.2-setup.exe)

> Install Nmap - Discover Raspy IP Address on LAN/WLAN
```
sudo apt update
```
```
sudo apt install -y nmap
```

> Discover IPAddress & MacAddress
```
ifconfig 
```

> Discover IPAddress
```
hostname -I
```

> SSH Connection
```
ssh <raspberrydefaultuser>@<raspberryipaddress>
default hostname: pi | password: raspberry
```
> SSH Re-Build Key
```
sudo ssh-keygen -R "hostname/ipaddress"
```
```
sudo ssh <raspberrydefaultuser>@<raspberryipaddress>
```

# Fundamentals of SUDO
> Aggiornamento lista pacchetti
```
sudo update
```
> Aggiornamento pacchetti installati 
```
sudo upgrade
```

> Installare Pacchetti
```
sudo apt-get install <nomepacchetto>
```

> Rimuovere Pacchetti
```
sudo apt-get remove <nomepacchetto>
```

# Aggiungere e rimuovere utenti
> Add Users
```
sudo adduser <nomeutente>
```
> Remove Users
```
sudo userdel-r <nomeutente>
```

# Fundamentals of Directory & Files

> Creare nuova directory 
```
sudo mkdir <nomecartella>
```
> Creare nuovo file  
```
sudo touch <nomefile>
```

> Copiare directory
```
sudo cp -r percorsoorigine percorsodestinatione
```

> Cancellare directory
```
sudo rm -rf  percorsoorigine percorsodestinatione
```

> Rinominare directory e files
```
sudo mv  percorsoorigine/nomefile percorsoestinatione/nomefile
```
> Editor di Codice
```
sudo nano <nomefile>
```

# Fundamentals of BASH
> Permessi CHMOD
```
sudo chmod +x <nomefile.sh>
```
> Lanciare Script
```
sudo ./<nomefile.sh>
```

# Raspberry Service on Boot  
```
sudo cp nomeservizio.service /etc/systemd/system/
```
```
cd /etc/systemd/system/
```
```
sudo chmod 644 nomeservizio.service
```
```
sudo systemctl daemon-reload
```
```
sudo systemctl enable nomeservizio.service
sudo systemctl status nomeservizio.service
sudo systemctl start nomeservizio.service
sudo systemctl stop nomeservizio.service
sudo systemctl restart nomeservizio.service
```

# Fundamentals of NPM
> Rimuovere Pacchetti
```
sudo npm install <nomepacchetto>
```
# Fundamentals of GIT
> Git add
```
git add -A
```
> Git commit 
```
git commit -m "Testo Commit"
```
> Git push
```
git push origin <nomebranch>
```
> Git Fetch/Checkout
```
git fetch && git checkout <nomebranch>
```