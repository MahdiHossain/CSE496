N = 77483692467084448965814418730866278616923517800664484047176015901835675610073
e = 65537
d = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321

def rsa_decrypt(ciphertext, d, N):
    decrypted = pow(ciphertext, d, N)
    return decrypted

decrypted_message = rsa_decrypt(c, d, N)
print("Decrypted message:", decrypted_message)