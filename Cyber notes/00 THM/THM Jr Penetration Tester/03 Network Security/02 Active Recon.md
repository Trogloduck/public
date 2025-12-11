https://tryhackme.com/room/activerecon

### Table of contents
- [[#Intro]]
- [[#Web Browser]]
- [[#`ping`]]
- [[#`traceroute`]]
- [[#`telnet`]]
- [[#`netcat`]]

___
### Intro
[[#Table of contents|Back to the top]]

Contact with target
- Social engineering: email, phone call, physical
- Connection to target system (SSH through firewall, website)

___
### Web Browser
[[#Table of contents|Back to the top]]

HTTP --> 80; HTTPS --> 443 -- default ports --> not shown in address bar

`CTRL + SHIFT + I` --> Inspector

Tools
- Burp --> FoxyProxy
- **[User-Agent Switcher and Manager](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/):** pretend to access webpage from different OS (from mobile for instance)
- **[Wappalyzer](https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/):** technologies used on website

___
### `ping`
[[#Table of contents|Back to the top]]

ICMP (Internet Control Message Protocol), echo / type 8
`man ping`
`ping -c number_of_pings_to_send IP_ADDRESS` (`-n` on windows)

MS Windows Firewall blocks pings by default

___
### `traceroute`
[[#Table of contents|Back to the top]]

`traceroute IP_ADDRESS` (`tracert` on shitdows)

**TTL** (Time To Live): ***number of*** routers/***hops*** packet can pass through before being dropped --> not really time

Router receives packet --> decreases TTL by one before passing to next

TTL = 0 --> ICMP Time-to-Live exceeded sent to sender

On Linux, TTL = 1 is used to reveal IP address of 1st router, then TTL = 2 and so on

___
### `telnet`
[[#Table of contents|Back to the top]]
*Teletype Network, interact remotely via CLI*

**Default port: 23**

All data in cleartext, TCP, secure alternative: SSH (Secure Shell)

`telnet IP_ADDRESS PORT_NUMBER`

If we connect to a webserver --> port 80, then try `GET / HTTP/1.1` in order to learn about the server

___
### `netcat`
[[#Table of contents|Back to the top]]

TCP and UDP, connects to listening port / listens on a port
`nc IP_ADDRESS PORT_NUMBER`