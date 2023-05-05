# Avvio script tramite servizi Raspberry  
```
sudo touch twinled.service 
```
```
sudo chmod 755 twinled.service
```
```
sudo cp twinled.service /etc/systemd/system/
```
```
cd /etc/systemd/system/
```

```
sudo systemctl daemon-reload
```
```
sudo systemctl enable twinled.service
sudo systemctl start twinled.service
sudo systemctl status twinled.service
```