## CPU Load
- **Commands**: `top`, `htop`, `uptime`, `mpstat`
- **Metrics**: Current load, load averages, CPU usage per processor

## Memory Usage
- **Commands**: `free -h`, `vmstat`, `top`, `htop`
- **Metrics**: Total memory, used memory, free memory, buffers, cache

## Disk Usage
- **Commands**: `df -h`, `du -sh /path/to/directory`, `iostat`
- **Metrics**: Used and available disk space, disk I/O

## Network Traffic
- **Commands**: `ifconfig`, `ip a`, `netstat -i`, `iftop`, `nload`
- **Metrics**: Incoming and outgoing traffic, bandwidth usage, errors

## Processes
- **Commands**: `ps aux`, `top`, `htop`, `pgrep -lf <process_name>`
- **Metrics**: Running processes, resource consumption, zombie processes

## Log Files
- **Locations**: `/var/log/`
  - `/var/log/syslog`: General system log
  - `/var/log/auth.log`: Authentication and security logs
  - `/var/log/kern.log`: Kernel logs

## Last Connected Users
- **Command**: `last`
- **Metrics**: Listing of last logged-in users, their activities

## System Uptime
- **Command**: `uptime`
- **Metrics**: System uptime, current time, load averages

## Network Traffic Assessment
- **Commands**: `ifconfig`, `ip a`, `netstat -i`, `iftop`, `nload`, `tcpdump`, `sar -n DEV 1 1`
- **Metrics**: Network device activity, real-time bandwidth usage, packet captures

## Memory-Intensive Processes
- **Command**: `ps aux --sort=-%mem | head -n 10`
- **Metrics**: Top 10 most memory-intensive processes
