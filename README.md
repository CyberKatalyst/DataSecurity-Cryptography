# Cryptography Scripts Description

## affineCeasar.py

**Description :** 

This Python script decrypts a given ciphertext encrypted using the Affine Caesar Cipher. 

The Affine Caesar Cipher is a type of substitution cipher where each letter in the plaintext is replaced using a mathematical formula:

![image](https://github.com/user-attachments/assets/ab156242-e6fe-4d41-9f00-e1e6b2357455)

To decrypt, the script calculates the modular inverse of 𝑎 a and applies the decryption formula:

![image](https://github.com/user-attachments/assets/7e69e2f9-13f7-4915-8065-9b19cedb01d4)

The script is specifically designed to assist in decrypting ciphertext when part of the plaintext is known (a crib), or through brute force when no hint is provided.

---

