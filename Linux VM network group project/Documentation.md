# Linux VM network - DOCUMENTATION

*Henri Hubert, Pavithra Mohan, Tom Macdonald*

*As part of a 7-month training program at BeCode, we undertook a group project to create a network composed of two virtual machines (VMs): a Kali Linux client with LibreOffice, Gimp and Mullvad browser installed and a Linux server providing DHCP, DNS, web server, and SSH connection services.*
___
Table of contents
- [Introduction](#1-introduction)
- [Project Infrastructure](#2-project-infrastructure)
- [Key Functionalities](#3-key-functionalities)
- [Project Demonstration](#4-project-demonstration)
- [DHCP](#dhcp)
- [DNS](#dns)
- [Web server](#web-server)
- [Backups](#backups-cron)
- [SSH](#ssh)
___

## 1. Introduction
### Project Overview
The goal was to set up a Linux server and workstation for a local library with limited funds, demonstrating the benefits of using open-source Linux over licensed software.  
**Context:** Linux is an affordable and flexible solution ideal for public or budget-conscious environments.

## 2. Project Infrastructure
### Server Setup
- **Ubuntu Server:** A non-GUI (Graphical User Interface) environment, typically used for backend services like DHCP, DNS, SSH, and web servers.
- **Kali Linux Workstation:** A client with a GUI, ideal for installing and running applications that require a graphical interface for productivity and browsing.

### Components of the Server Setup:
- **DHCP Server (isc-dhcp-server):** Automatically assigns IP addresses to clients.
- **DNS Server (Bind):** Resolves internal resources and redirects external queries.
- **Web Server (Nginx):** Hosts a local webpage for easy library access.
- **Remote Management (SSH):** Enables remote access to manage the server securely.

### Components of the Workstation Setup:
- **Applications Installed:**
  - **LibreOffice:** Office productivity suite.
  - **Gimp:** Image editing software.
  - **Mullvad Browser:** For privacy-focused browsing.
- **Automatic IP Addressing:** Using DHCP from the server.
- **Separate /home Partition:** Ensures data organization and persistence across OS updates.

## 3. Key Functionalities
### Backup System:
- **Configuration Backup:** Scheduled weekly backups of configuration files using cron, stored in a compressed archive.
- **Optional Feature:** Additional storage on a separate partition mounted only during backups.

### Security and Accessibility:
- **Internal Network Isolation:** The virtual DHCP network avoids interference with the external LAN.
- **Remote Assistance (Optional):** Discuss any implemented solutions for helping users remotely, if applicable.

## 4. Project Demonstration
### Demo Plan
1. **Server Setup and Configuration Files:**
   - Demonstrate server setup and highlight key configuration files.
2. **Workstation Setup:**
   - Show the installed applications and network connectivity.
3. **Backup and Recovery Process:**
   - Demonstrate how the backup system is configured and how to recover configurations.
4. **Navigating the Web Server's Local Page:**
   - Show the local webpage hosted by the Nginx server.
___
### DHCP

Update the package: 

`sudo apt update`

Installation:

`sudo apt install isc-dhcp-server`

Check the status:

`sudo systemctl status isc-dhcp-server`

Check the interface:

`ip a`

`enp0s3`: This is the interface name for the internal network.

`enp0s8`: This is the interface name for the NAT network

Config dhcp:

`sudo nano /etc/dhcp/dhcpd.conf`

Edit in the config file:

```
subnet 10.0.2.0 netmask 255.255.255.0 {

 range 10.0.2.10 10.0.2.100; # Range of IPs for DHCP
 option routers 10.0.2.1; # Default gateway
 option domain-name-servers 10.0.2.1, 8.8.8.8; # DNS servers for the subnet
 option domain-name "example.local"; # Local domain 

}
```

save the configuration by ctrl+o, ctrl+x to exit 

Now we have to make sure the dhcp listens to the right port:

`sudo nano /etc/default/isc-dhcp-server`

Change INTERFACESv4 to enp0s3 (the internal network):

`INTERFACESv4="enp0s3"`

We need to force the "router" IP on the enp0s3 port and make sure that the NAT gets an automatic IP from the VirtualBox DHCP:

`sudo nano /etc/netplan/50-cloud-init.yaml`

```
network:
	ethernets:
		enp0s3:
			dhcp4: no
			addresses:
			 - 10.0.2.1/24
			nameservers:
			  addresses:
			   - 10.0.2.1
		enp0s8:
			dhcp4: yes
	version: 2
```

Apply the changes:

`sudo netplan apply`

Test the configuration:

`sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf`

Restart : (this command should not give any error, it means your config is right)

`sudo systemctl restart isc-dhcp-server`

Don't hesitate to use the `ip addr` command to check if the IP's are right

If you encounter any error message: use the below command to troubleshoot

`sudo journalctl -xe`

You can now launch your Kali-Linux machine and start the terminal. If you type `ip addr`, you should see that you don't have any IP yet. That is because we have to do a request to the dhcp server to get one.

`sudo dhclient`

You should now have a working IP in the range of the dhcp

Kali-Linux(ping your gateway IP)

┌──(kali㉿kali)-[~]

└─$ `ip route`

`default via 10.0.2.2 dev eth0 `

`default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 `

`10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100 `

Explanation:

default via 10.0.2.2 dev eth0:

- This line indicates that the default gateway for your system is 10.0.2.2, and it is accessible through the eth0 network interface. This means that if your system needs to send packets to a destination that is not on the local network, it will route those packets through this gateway.

default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100:

- This is similar to the first line, but it specifies that this route was obtained via DHCP. The src 10.0.2.15 indicates that your machine's IP address on the eth0 interface is 10.0.2.15. The metric 100 is a value that the routing protocol uses to determine the preference of routes; lower values are preferred over higher ones.

10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100:

- This line indicates that there is a direct route to the 10.0.2.0/24 subnet (which includes all addresses from 10.0.2.0 to 10.0.2.255) via the eth0 interface. The proto kernel indicates that this route was added by the kernel when the interface was configured. The scope link means that this route is only valid for local traffic on that link.
___
### DNS

**On the server**

Install bind and net-tools

`sudo apt-get install bind9`

`sudo apt-get install net-tools`

Check the IP of the server thanks to net-tools

`ifconfig`

After using the command `sudo nano /etc/bind/named.conf.options`, setup forwarders (google 8.8.8.8 and google backup 8.8.4.4):

```
forwarders {

8.8.8.8;

8.8.4.4;

};
```

Enable firewall and allow bind9

`sudo ufw enable`

`sudo ufw allow bind9`

`sudo ufw reload`

`sudo ufw status`

Status should indicate “active” and Bind9: “ALLOW”

Restart service and check if it worked

`sudo systemctl reload bind9`

`sudo systemctl status bind9`

Active section should indicate “active (running)” and Status section: “running”

**On the client**

Using the command `sudo dhclient` to request an IP address from the DHCP server will also inform the client which DNS server to use (in this case, ours).
___
### Web server

1. Update packages:

`sudo apt update`

2. Install nginx:

`sudo apt install nginx -y`

3. Make sure nginx starts and that it will start working when you turn the server on:

`sudo systemctl start nginx`

`sudo systemctl enable nginx`

4. Go to the directory to start making your page:

`cd /etc/nginx/sites-available/`

5. Create your web page config file in this directory and start writing in it:

`sudo nano /etc/nginx/sites-available/my_website`

6. Write the config lines for the page in the nano:

```
server {
    listen 80;
    server_name your_domain_or_IP;
    root /var/www/my_website;
    index index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
}
```

7. Create a directory for you webpage:

`sudo mkdir -p /var/www/my_website`

8. Give yourself the permissions to modify it and have access to it:

`sudo chown -R $USER:$USER /var/www/my_website`

`sudo chmod -R 755 /var/www/my_website`

9. Check in /var/www/my_website if the file index.html exists and if it doesn’t, create it:

`cd /var/www/my_website`

`ls`

`touch index.html`

10. Modify the index.html file with your html file:

`nano index.html`

`<html><body><h1>Hello World!</h1></body></html>`

11. Create a symbolic link to enable the new webpage:

`sudo ln -s /etc/nginx/sites-available/my_website /etc/nginx/sites-enabled/`

12. Check the nginx configuration:

`sudo ln -s /etc/nginx/sites-available/my_website /etc/nginx/sites-enabled/`

13. Restart nginx for it to work:

`sudo systemctl reload nginx`

14. To connect to the webpage:
	a. connect with you machine to the server with ssh

`ssh username@server_ip_adress`

Open your web navigator and type the ip address of your server as the url

15. If it is still not working:
	1. delete the default file in /var/www/
	2. delete the default file in /etc/nginx/sites-enabled/
	3. restart nginx
___
### Backups (cron)

#### Define Backup Requirements:

**Services to Back Up:** We focused on backing up the configuration files for the DHCP and DNS services, with plans to add Nginx later.
**Backup Destination:** We decided to use a dedicated backup directory, /mnt/backup, for storing backup files.

#### Setup the Backup Directory:

**Mounting the Backup Partition:**
You mounted a partition (like /dev/sda2) to /mnt/backup to ensure that there was enough space and separation for backup files.

You used the command:

`sudo mount /dev/sda2 /mnt/backup`

**Create the Backup Script:**

Script Creation: We created a backup script named backup_config.sh in your home directory using nano.

`nano ~/backup_config.sh`

`#!/bin/bash`

Backup destination directory

`BACKUP_DIR="/mnt/backup"`

Create a timestamp for the backup file name

`TIMESTAMP=$(date +"%Y%m%d%H%M")`

`BACKUP_FILE="$BACKUP_DIR/config_backup_$TIMESTAMP.tar.gz"`

**Ensure the backup directory exists**

```
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Backup directory $BACKUP_DIR does not exist. Please mount the partition."
    exit 1
fi
```


#### Create the backup of configuration files

Update the paths below based on your actual configuration files
`tar -czvf "$BACKUP_FILE" /etc/dhcp/dhcpd.conf /etc/bind/named.conf`

Check if the backup was successful
```
if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
```

Save and exit

**Run the backup Script:**

`sudo ~/backup_config.sh`

**Verify the Backup**

`ls -l /mnt/backup`

**CRON:**

Cron is a time-based job scheduler in Unix-like operating systems, including Linux. It allows you to run scripts or commands automatically at specified intervals (e.g., hourly, daily, weekly). Using cron, you can schedule your backup script to run automatically without needing to manually execute it each time.

`crontab -e`

**Run the backup every Sunday at 2:00 AM, you would add the following line:**

`0 2 * * 0 /bin/bash /home/pavithra/backup_config.sh`

**Run the crontab**

`crontab -l`

By setting up a cron job, your backup script will run automatically at the specified time, ensuring that you have regular backups of your configuration files without manual intervention. 
___
### SSH connection
**On server**

Make sure SSH is installed

Enable and start

`sudo systemctl start ssh`

`sudo systemctl enable ssh`

`sudo systemctl status ssh`
 
Allow ssh through the firewall

`sudo ufw allow ssh`

`sudo ufw reload
`
`sudo ufw status`
 
**On client**

`ssh [user]@[ip of the ssh server]`
___
## Get internet on the client via the server

#### In the server

Enable IP forwarding in the server so the server will be able to send packet from the NAT to the internal network:

`sudo nano /etc/sysctl.conf`

`net.ipv4.ip_forward=1` (you just have to uncomment this line)

Save and apply the changes: 

`sudo sysctl -p`

Now, we need to add some elements to the iptable:

`sudo iptables -t nat -A POSTROUTING -o enp0s8 -j MASQUERADE`

This will add to the NAT table a line saying that it can communicate through the enp0s3 interface since it is the interface connected to the internet.

`sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT`

`sudo nano /etc/sysctl.conf`

--> clear


Add those lines of command to the start-up config:

`sudo apt-get install iptables-persistent`

Normally, it should ask you if you want to save the config once you installed it but if it doesn't, run this command line:

`sudo iptables-save | sudo tee /etc/iptables/rules.v4`

#### In the Kali VM

Check the route:

`ip route`

If the default route isn't your server, you should add it: 

`sudo ip route add default via 10.0.2.1`

Now you should be able to ping whatever you want and have access to internet!

___
## Online resources:

- [How to Network Two Virtual Machines With VirtualBox](https://www.makeuseof.com/how-network-two-virtual-machines-with-virtualbox/) 
- [Setting up a Bind DNS server on Ubuntu server](https://youtu.be/DuVNclBfykw)
- [How to change DNS Server on Kali Linux | Troubleshoot DNS on Kali](https://youtu.be/Ya0AZDPgvNk)
- [Linux DNS Server Configuration for Beginners](https://youtu.be/I8lawEbZKxA)
- [Linux DNS Server - YouTube](https://www.youtube.com/playlist?list=PL291a0KYQZSK6E_1j9xkkieCOi_867pyc)
- [How to add a new user on a Linux server (with SSH access)](https://youtu.be/86EYEuJWfeE)
- [How to enable SSH on Linux Ubuntu](https://youtu.be/Wlmne44M6fQ)
