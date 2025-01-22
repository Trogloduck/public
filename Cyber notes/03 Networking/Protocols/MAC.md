< [[2. Data link]]

Media Access Control can’t change and is unique (in theory), burnt in the *NIC* (Network Interface Card), referred to as *physical identifier*

MAC addresses can be *spoofed* (someone pretends to be someone else)

Written in hexadecimal:

| Decimal | Hexadecimal | Binary |
| ------- | ----------- | ------ |
| 0       | 0           | 0000   |
| 1       | 1           | 0001   |
| 2       | 2           | 0010   |
| 3       | 3           | 0011   |
| 4       | 4           | 0100   |
| 5       | 5           | 0101   |
| 6       | 6           | 0110   |
| 7       | 7           | 0111   |
| 8       | 8           | 1000   |
| 9       | 9           | 1001   |
| 10      | A           | 1010   |
| 11      | B           | 1011   |
| 12      | C           | 1100   |
| 13      | D           | 1101   |
| 14      | E           | 1110   |
| 15      | F           | 1111   |

Ex: 

| Hexadecimal       | Calculation                       | Decimal          |
| ----------------- | --------------------------------- | ---------------- |
| 00-05-9A-3C-78-00 | ...                               | 0.5.154.60.120.0 |
| 00                | 0\*$16^1$ + 0\*$16^0$             | 0                |
| 05                | 0\*$16^1$ + 5\*$16^0$             | 5                |
| 9A                | 9\*$16^1$ + 10\*$16^0$ = 144 + 10 | 154              |
| 3C                | 3\*$16^1$ + 12\*$16^0$ = 48 + 12  | 60               |
| 78                | 7\*$16^1$ + 8\*$16^0$ = 112 + 8   | 120              |
| 00                | 0\*$16^1$ + 0\*$16^0$             | 0                |

MAC Address is composed of ***48 bits***
- ***OUI***: Organizationally Unique Identifier, ***24*** first bits, identifies ***manufacturer***
- ***Device Identifier***: ***24*** last bits, identifies device
