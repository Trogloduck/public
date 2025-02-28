# To Deliver

| Deliverable   | Format  |
| ------------- | ------- |
| Documentation | .md     |
| Summary       | \> 1 pg |
| Live demo     |         |
# Network components

- Server (no GUI)
	- Services
	    - DHCP (one scope serving the local internal network) #isc-dhcp-server
	    - DNS (resolve internal resources, a redirector is used for external resources) #bind
	    - WEB server (install and configure an Nginx web server to host a local webpage) #nginx
	- **Required**
		- Weekly backup the configuration files for each service into one single compressed archive #cron
		- The server is remotely manageable (SSH) #ssh
	- **Optional**
		- Backups are placed on a partition located on separate disk, this partition must be mounted for the backup, then unmounted #rsync 

- Workstation with desktop environment
	- Apps
	    - LibreOffice
	    - Gimp
	    - Mullvad browser
    - **Required**
        - This workstation uses automatic addressing
        - The `/home` folder is located on a separate partition, same disk
    - **Optional**
        - Propose and implement a solution to remotely help a user