In [[06 Networking]], subnetting is subdividing a network into smaller networks within itself

- **Host** address: IP address of a device within a subnet
	Ex: 192.168.1.100
- **Network** address/ID: IP address identifying the start of a network, used to identify network’s existence, 1st possible address in subnet
	Ex: 192.168.1.0 or 192.168.1.x (x depending on how many IPs in previous subnet)
- ***Default gateway***: special IP address assigned to device able to send information on another network (AKA broadcasting to router), usually 1st or last usable IP address
	Ex: 192.168.1.1 or 192.168.1.254 in a CIDR block /24
- ***Broadcast IP***: last possible address in subnet (192.168.1.255 for CIDR block /24)
- ***Subnet mask***: determines which part of the IP identifies the network/host
	Ex: subnet mask of 255.255.255.0 with an IP address of 162.198.1.5 --> network is 162.198.1, host is 5
- ***[CIDR](#^cidr-explanation)/Subnet***: /24 --> 255.255.255.0; /25 --> 255.255.255.128 (256 - 128); /24 --> 255.255.255.224 (256 - 32); ...
- ***Next network***: IP of following subnet
	Ex: 192.168.1.128 for CIDR block /25
---

**CIDR** (Classless Inter-Domain Routing) block: set of IP addresses that share same network prefix and number of bits. Notation:
^cidr-explanation
- /24: 256 IP addresses
- /25: 128 IP addresses
- /24: 64 IP addresses
- ...

___

Subnetting cheat sheet:

| $n$                            | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| **Group size** -- $2^n$        | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| **Subnet mask** -- $256 - 2^n$ | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |
| **CIDR**                       | /25 | /26 | /27 | /28 | /29 | /30 | /31 | /32 |
![[Pasted image 20240912143954.png]]

If at some point we reach 256, we increase the next octet:
![[Pasted image 20240912150855.png]]
___

Determining number of subnets/hosts based on subnet mask:

|                      | Formula            | Explanation                                                                                                  |
| -------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Subnets**          | $2^S$ or $2^S$ - 2 | S: number of bits allocated for subnetting<br>\- 2: 1st and last may be reserved (// hosts)                  |
| **Hosts per Subnet** | $2^H - 2$          | H: number of bits allocated for host section of IP addresses \- 2: 1st IP for network, last for broadcasting |

Custom subnet mask: to limit number of hosts
Based on number of hosts we want (T -- target):
$2^H - 2  >= T$
<=>
$2^H >= T + 2$
We then choose the smallest possible value for H

Ex: create custom subnet mask for network able to have 14 subnets and 14 usable hosts

| **Step**                         | **Calculation/Details**        | **Result**      |
| -------------------------------- | ------------------------------ | --------------- |
| **1. Host Requirements**         | \# usable hosts per subnet: 14 |                 |
| - Number of host bits needed     | $2^H - 2  >= 14$               |                 |
| - Detail                         | $2^H >= 16$                    | 4 bits          |
| **2. Subnet Requirements**       | \# subnets: 14                 |                 |
| - Number of subnet bits needed   | $2^S >= 14$                    | 4 bits          |
| **3. Calculate Total Bits Used** | IPv4 address is 32 bits total  |                 |
| - Network bits                   | 32 - (S + H)                   | 24 bits         |
| **4. Determine Subnet Mask**     | 256 - (H + 2) = 256 - 16       | 255.255.255.240 |
([[Bonus]])

Different ranges of host IPs:

<table border="1"; style="width: 100%; border: 1px solid black;">
  <tr>
    <th rowspan="2"; style="vertical-align: middle">Network IP /
    Number of subnet</th>
    <th rowspan="2"; style="vertical-align: middle">4 subnet bits</th>
    <th colspan="2"; style="text-align: center;">4 host bits</th>
  </tr>
  <tr>
	  <th>Lower bound</th>
	  <th>Upper bound</th>
</tr>
  <tr>
    <td>192.10.10.0</td>
    <td>0000</td>
    <td>0000</td>
    <td>1111</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0000</td>
    <td>192.10.10.0</td>
    <td>192.10.10.15</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0001</td>
    <td>192.10.10.16</td>
    <td>192.10.10.31</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0010</td>
    <td>192.10.10.32</td>
    <td>192.10.10.47</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0011</td>
    <td>192.10.10.48</td>
    <td>192.10.10.63</td>
  </tr>
  <tr>
    <td>4</td>
    <td>0100</td>
    <td>192.10.10.64</td>
    <td>192.10.10.79</td>
  </tr>
  <tr>
    <td>5</td>
    <td>0101</td>
    <td>192.10.10.80</td>
    <td>192.10.10.95</td>
  </tr>
  <tr>
    <td>6</td>
    <td>0110</td>
    <td>192.10.10.96</td>
    <td>192.10.10.111</td>
  </tr>
  <tr>
    <td>7</td>
    <td>0111</td>
    <td>192.10.10.112</td>
    <td>192.10.10.127</td>
  </tr>
  <tr>
    <td>8</td>
    <td>1000</td>
    <td>192.10.10.128</td>
    <td>192.10.10.143</td>
  </tr>
  <tr>
    <td>9</td>
    <td>1001</td>
    <td>192.10.10.144</td>
    <td>192.10.10.159</td>
  </tr>
  <tr>
    <td>10</td>
    <td>1010</td>
    <td>192.10.10.160</td>
    <td>192.10.10.175</td>
  </tr>
  <tr>
    <td>11</td>
    <td>1011</td>
    <td>192.10.10.176</td>
    <td>192.10.10.191</td>
  </tr>
  <tr>
    <td>12</td>
    <td>1100</td>
    <td>192.10.10.192</td>
    <td>192.10.10.207</td>
  </tr>
  <tr>
    <td>13</td>
    <td>1101</td>
    <td>192.10.10.208</td>
    <td>192.10.10.223</td>
  </tr>
  <tr>
    <td>14</td>
    <td>1110</td>
    <td>192.10.10.224</td>
    <td>192.10.10.239</td>
  </tr>
  <tr>
    <td>15</td>
    <td>1111</td>
    <td>192.10.10.240</td>
    <td>192.10.10.255</td>
  </tr>
</table>

___

IP \* subnet mask = network IP (in binary):
(the multiplication is called "ANDING", why? nobody knows)

Ex:

|                       | Decimal       | Binary                                        |
| --------------------- | ------------- | --------------------------------------------- |
| **IP Address**        | 192.10.10.33  | 1100 0000 . 0110 0100 . 0000 1010 . 0010 0001 |
| **Subnet Mask**       | 255.255.255.0 | 1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 |
| *Multiply bit by bit* |               |                                               |
| **Network IP**        | 192.10.10.0   | 1100 0000 . 0110 0100 . 0000 1010 . 0000 0000 |



pg 60 of Ip-addressing-and-subnetting-workbook
