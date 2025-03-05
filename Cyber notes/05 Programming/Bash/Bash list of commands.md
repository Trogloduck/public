# List of commands

## Help

* `man`: display system documentation
* `whatis`: prints manual page description
* `info`: read _Info_ documents

## Navigation

* `cd`: change current directory
* `ls`: list directory content
* `pwd`: print the current directory
* `pushd`: go to a folder while keeping old location on _"cache"_
* `popd`: go back to an old location on _"cache"_

## File operation

* `cat`: display content of file
* `touch`: create a file or update timestamps
* `cp`: copy file
* `mkdir`: create directory
* `mv`: move/rename file
* `rm`: remove file/directory
* `rmdir`: remove empty directory
* `ln`: link files
* `head`: display first 10 lines
* `tail`: display last 10 lines

#### Text file operation

- `cut -f 1`: cut 1st field
- `cut -c1`: cut 1st column
- `grep 'keyword'`: filter specific keyword
- `| sort`: sort alphabetically
- `| sort -n`: sort numerically
- `| uniq`: eliminate duplicate lines
- `| wc -l`: display number of lines
- `| nl`: show line numbers (1 in front of line 1, 2 in front of line 2, etc.)
- `| sed -n '11p'` or `| awk 'NR == 11'`: print line 11
- `| sed -n '10,15p'`: print lines 10-15
- `| awk 'NR < 11'`: print lines <11

## System

* `date`: print the date and time
* `cal`: display a calendar
* `lsblk`: list connected drives

## Users

* `passwd`: change user password
* `usermod`: modify a user account
* `groupadd`: create a new group
* `whoami`: print current logged user

## Permissions

* `sudo`: execute a command as another user
* `su`: change the current user
* `chmod`: change file permissions
* `chown`: change the owner of a file
* `chgrp`: change the group of a file

## Compression

* `tar`: archive files
* `gzip`: compress and expand files

## Remote

* `ssh`: remote login
* `rsync`: remote file copying tool

## Process management

* `ps`: report process status
* `ps aux`: list every tunning process in the system
* `kill`: stop a process
* `top`: display a reptitively updated list of running processes
* `htop`: improved version of `top`
* `bg`: put a process on the background
* `fg`: bring a process on the foreground

## Package manager

* `apt-get`
* `snap`
* `pip`

## Text editor

* `vim`
* `nvim`
* `nano`
* `gedit`
