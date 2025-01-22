***bit*** is binary: 0 or 1 (A) 

***byte***: 8 bits (A, B, C, D, E, F, G, H)

*A byte is generally 8 bits today, but historically it could vary* 
*An octet is explicitly 8 bits, without any historical or contextual ambiguity* 

0000 0000 = 0 ; 0000 0001 = 1 ; 0000 0010 = 2 ; 0000 0011 = 3 ; … ; 1111 1111 = 255
    • 256 combinations (2^8)

With 2 bytes, you have 65 536 combinations (2^16 – 16 bits)

*(An IPv4 address is composed of 4 bytes)*

HGFE DCBA : A x 1 + B x 2 + C x 4 + D x 8 + E x 16 + F x 32 + G x 64 + H x 128
    • it follows a base 2

For letters, ASCII (American Standard Code for Information Interchange) is the most common

| Decimal (base 10) / letter | Binary (base 2) / ASCII |
| -------------------------- | ----------------------- |
| 2                          | 0000 0010               |
| 10                         | 0000 1010               |
| e                          | 0110 0101*              |

\* to convert in ASCII, we start with 101 (e – 5 = 2^2 + 2^0), then do the following operations:
    • 101%2 = 1
    • 50%2 = 0
    • 25%2 = 1
    • 12%2 = 0
    • 6%2 = 0
    • 3%2 = 1
    • 1%2 = 1
Remainders in reverse order → 0110 0101