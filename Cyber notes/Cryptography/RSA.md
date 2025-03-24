#### Encryption - Decryption process

**Public key**: (e, N)
**Private key**: (d, N)
M: message; C: cipher text

**Encryption**: C = M$^e$ mod N
**Decryption**: M = C$^d$ mod N

##### Practical example

**Public key**: (3, 33)
**Private key**: (7, 33)
M = 4

**Encryption**: C = 4$^3$ mod 33 = 64 mod 33 = 31
**Decryption**: M = 31$^7$ mod 33 = 27512614111 mod 33 = 4
___
#### Key generation

1. Pick 2 **prime numbers**, $p$ and $q$
2. $N = p  \times q$
3. $\phi (N) = (p - 1) \times (q - 1)$
4. $1 < e < \phi (N)$  ;  e is **coprime** with $\phi (N)$
5. $d \times e$ mod $\phi (N) = 1$

**Public key**: (e, N)
**Private key**: (d, N)

##### Practical example

| Step | Abstract                                                | Practical                                                                                                                               |
| ---- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Pick 2 **prime numbers**, $p$ and $q$                   | $q = 3$ and $p = 11$                                                                                                                    |
| 2    | $N = p  \times q$                                       | $N = 3  \times 11 = 33$                                                                                                                 |
| 3    | $\phi (N) = (p - 1) \times (q - 1)$                     | $\phi (33) = (3 - 1) \times (11 - 1) = 20$                                                                                              |
| 4    | $1 < e < \phi (N)$  ;  e is **coprime** with $\phi (N)$ | $1 < e < \phi (33)$  ;  $e$ is **coprime** with $\phi (33)$  :<br>$1 < e < 20$  ;  $e$ is **coprime** with $20$<br>Let's choose $e = 3$ |
| 5    | $d \times e$  mod $\phi (N) = 1$                        | $d \times e$ mod $\phi (33) = 1$  :<br>$d \times 3$ mod $20 = 1$<br>Let's choose $d = 7$                                                |

___
#### Difficulties

- Factoring large prime numbers
- Solving discrete logarithms