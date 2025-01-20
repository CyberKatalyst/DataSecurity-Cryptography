# Description: Algorithm for affine Ceaser cipher decryption
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  u  V  W  X  Y  Z

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# To find the indexes of the plaintext and ciphertext
def index_finder(cipher_text, plain_text, length):
    if len(plain_text) > len(cipher_text):
        raise ValueError('plain_text cannot be longer than cipher_text!')
    alphabet_index_dict = {
        idx: [alphabet.index(cipher_text[idx].upper()), alphabet.index(plain_text[idx].upper())]
        for idx in range(length)
    }
    return alphabet_index_dict


# Returns the modular inverse of a number
def modular_inverse(a, mod):
    a %= mod
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None


# The function returns the decrypted text where a and b are the keys
def affine_ceaser_decryption(cipher_text, a, b):
    aInv = modular_inverse(a, 26)
    if aInv is None:
        return None
    return ''.join([alphabet[(aInv * (alphabet.index(r) - b)) % 26] for r in cipher_text.upper()])


# The function prints the possible decrypted texts and keys and returns the decrypted text
def decryption_letter(cipher_text, cipher_text_index=None, plain_text_index=None, cipher_text_index_1=None, plain_text_index_1=None):
    for a in range(1, 26, 2):
        for b in range(26):
            if (plain_text_index * a + b) % 26 == cipher_text_index and (
                    cipher_text_index_1 is None or (plain_text_index_1 * a + b) % 26 == cipher_text_index_1):
                decrypted_text = affine_ceaser_decryption(ciphertext, a, b)
                if decrypted_text:
                    print(f'key a = {a}, key b = {b}: {decrypted_text}')
                    print("______________________________________________________________________________________\n")


# For loop to see all possible variants for the Ceaser
def brute_force_cipher():
    results = [
        f'key a = {a}, key b = {b}: {affine_ceaser_decryption(cipher_text, a, b)}'
        for a in range(1, 26, 2)
        for b in range(26)
    ]
    print('\n'.join(results))


if __name__ == '__main__':
    # if plaintext starts with enter it here
    beginning_of_plain_text = "T"
    # Enter the ciphertext here
    cipher_text = """CATGZ DBORH OTJRZ DTCAL OPZEX GFKCZ PGBKA FTPCA TXBTR BGXLK ATGBO ILCRY BGLBC LZOR  """
    
    if len(cipher_text) > 0:
        ciphertext = cipher_text.replace("\n", "").replace(" ", "")
        length_of_plain_text = len(beginning_of_plain_text)

        if length_of_plain_text == 1:
            indexes = index_finder(ciphertext, beginning_of_plain_text, 1)
        elif length_of_plain_text >= 2:
            indexes = index_finder(ciphertext, beginning_of_plain_text, 2)
        else:
            indexes = {}

        print("\nThe possible combinations of key and decrypted texts are:\n")
        if len(indexes) == 1:
            decryption_letter(ciphertext, indexes[0][0], indexes[0][1])
        elif len(indexes) == 2:
            decryption_letter(ciphertext, indexes[0][0], indexes[0][1], indexes[1][0], indexes[1][1])
        elif len(indexes) == 0:
            brute_force_cipher()
    else:
        print("\nPlease provide a cipher in correct format.\n")
