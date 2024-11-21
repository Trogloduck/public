# Symmetric Encryption

"The code breakers" David Kahn

| C := E(K, m)                                                                                        | m := D(K, C)                                                                                       |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Cipher** `C` **is defined by** (`:=`) the encryption of the **message** `m` using the **key** `K` | **Message** `m` **is defined by** (`:=`) the decryption of the **cipher** `C`using the **key** `K` |

# Historic Examples

## Substitution cipher

Substitution table:
k :=

| a   | --> | c   |
| --- | --- | --- |
| b   | --> | a   |
| c   | --> | w   |
| ... |     |     |
C := E(K, "bac") = "acw"

*Caesar cipher: substitution with a fixed shift*

*Not really a cipher because there is not really a key*

Using a substitution table with the 26 letters, each of the letters can become one of the other 26 letters of the alphabet
- a --> 26 possible substitutes
- b --> 25 possible substitutes
- ...
=> The number of possible substitutions is 26! (26\*25\*24\*...)

$26! \approx 2^{88}$

=> 88 bits are necessary to describe a key in a substitution cipher

This is a fine key space but it's still easily breakable

### Breaking substitution cipher

1. Use the **frequency of letters** 
   *In English, the most frequently used letter is "e"*
   -- e appears 12.7% in standard English text; t: 9.1%; a: 8.1%
2. Use **frequencies of pairs of letters** (digrams)
   -- he, an, in, th are the most common digrams in English
3. Trigrams
4. ...
This is called a "***cipher text only attack***": just given the cipher text the encryption can be broken (i.e. this is bad encryption)

## Vigenere cipher
*$16^{th}$ century, Rome*

k = crypto

`m = whatanicedaytoday`

`k = cryptocryptocrypt`

`c = zzzjucludtunwgcqs`; c = m + k

*Each character of the message is encrypted by adding to its index the index of the corresponding character in the encryption key modulo 26*

### Breaking Vigenere cipher

1. Determine the length (x) of the key
2. Divide the cipher into groups of x
3. If we take the $1^{st}$ letter of each group and compare them all, we know they have all been encrypted using the shift based on the $1^{st}$ letter of the encryption key, so we can compare the frequency of those letters and the most frequent is likely to be e
4. $c = m + k \Leftrightarrow k = c - m$
   So, for the $1^{st}$ letter of the cipher m = e $\Rightarrow$ we can determine the $1^{st}$ letter of the key by subtracting e to the $1^{st}$ letter of the cipher
5. We do the same for i in range(x+1)

Run this algorithm assuming the key length is 1, 2, 3, ... until the message makes sense

## Rotor Machines
*$19^{th}$ century*

