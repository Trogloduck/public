# Linux VM Network - Summary
## Introduction
Project Overview: The goal was to set up a Linux server and workstation for a local library with limited funds. This project demonstrates the benefits of using open-source Linux over licensed software, presenting Linux as an affordable and flexible solution ideal for public or budget-conscious environments.

## Project Features
### Server Setup
Configured without a GUI, the server includes:

- DHCP Server (isc-dhcp-server): Automatically assigns IP addresses to clients.
- DNS Server (Bind9): Resolves internal resources and redirects external queries.
- Web Server (NGINX): Hosts a local webpage for easy library access.
- Remote Management (SSH): Enables secure remote access for managing the server.

### Workstation Setup
Configured with a desktop environment, the workstation includes:

- LibreOffice, GIMP, Mullvad Browser: Applications for user productivity.
- Automatic IP Addressing: Utilizes DHCP from the server.
- Separate /home Partition: Ensures data organization and persistence across OS updates.

## Conclusion
During the project, we were able to implement several of the required features. However, some features did not work as expected or caused other features to malfunction. Additional time is needed to finalize and polish the project.
