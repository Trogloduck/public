**On server**

install ssh if not installed

enable and start
`sudo systemctl start ssh`
`sudo systemctl enable ssh`
`sudo systemctl status ssh`

allow ssh through the firewall
`sudo ufw allow ssh`
`sudo ufw reload`
`sudo ufw status`


**On client**

`ssh [user]@[ip of the ssh server]`

enter the password of the user
enjoy!