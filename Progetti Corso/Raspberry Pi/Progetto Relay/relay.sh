sudo chmod 755 relaybot.service
sudo cp relaybot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable relaybot.service
sudo systemctl start relaybot.service
sudo systemctl status relaybot.service
