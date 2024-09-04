***kernel***: program at the core of operating system, generally with complete control over everything in the system, links interface with hardware
***shell***: program that allows the user to communicate with the kernel

On the shell: user@hotname:~$
‘~’:in the personal directory
‘$’: not a privileged user -- # would mean ‘root account’

Writing a command: cmd -o arg
    • The shell will execute the command ‘cmd’ with the option ‘o’ on the argument ‘arg’

$PS1 variable defines prompt when waiting for user input

$PATH variable lists all directories containing external commands (not built in the shell)

If a command is in a /directory that is not included in the variable $PATH, run the following command to not have to call the specific directory on each use of the command:
	export PATH=$PATH:/directory

Help with internal command: help cmd
Help with external command: cmd --help

For both, man cmd will give more details

Linux directory structure: FHS – Filesystem Hierarchy Standard
    • good for administration: know which type of files should be where
    • good for development: knows which files should go where when deploying and configuring programs

Types of directories:
    • shareable >< unshareable: can(‘t)/should(n’t) be shared
    • variable >< static: can(‘t) be changed without privileged

The root of the system is ‘/’, calling a directory starting with the root / is called absolute
Each directory has 2 special files named ‘.’ (for itself) and ‘..’ for its parent file, calling a directory relatively to its parent/itself is called relative

Mandatory files under root in FSH list
    • /bin: critical commands for proper functioning of system
    • /sbin: commands intended only for administrator for system management
    • /usr/bin: commands intended for all users of the system, privileged or not.
    • /usr/sbin: commands for administrator, not critical for the proper functioning of system

/proc contains all processes data, /sys kernel data

***DAC*** – Discretionary Access Control
Files, directories, processes, … are owned by proprietary account (‘user’) and proprietary group (‘group’)
Rights are defined for proprietary account of the object, proprietary group and others

This way of managing rights comes from Trusted Computer System Evaluation Criteria (orange book)

Rights are encoded in 3 bits: 2° read (r), 1° write (w), 0° execute (x); each for user (u), group (g) and others (o) so 9 bits

To modify rights: chmod u+rwx file giving user ‘u’ rights to read, write and execute ‘file’
rwx can be represented with binary system: r = 4, w = 2, x = 1
    • giving rwx rights to user, group and others on file: chmod 777 file