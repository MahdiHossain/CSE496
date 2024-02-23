import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

cipher_text = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

def b16_decode(solve):
    dec = ""
    for idx in range(0, len(solve), 2):
        c1 = solve[idx]
        c2 = solve[idx + 1]
        c1 = ALPHABET.index(c1)
        c2 = ALPHABET.index(c2)
        binary1 = "{0:04b}".format(c1)
        binary2 = "{0:04b}".format(c2)
        binary = int(binary1 + binary2, 2)
        dec += chr(binary)
    return dec

def unshift(c, k):
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

for letter in ALPHABET:
    dec = ""
    for i, c in enumerate(cipher_text):
        dec += unshift(c, letter)
    dec = b16_decode(dec)
    print(dec)