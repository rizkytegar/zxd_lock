from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import binascii

cipher_hex = "632EA096F27B6662A2386DE9F73C5698B51D4E080172B749602FED580A8EFA5F484"
key = b"gnzLCH7vxt4R8HyxFWipUPIFpcSTw9Ir"
nonce = b"gnzLCH7vxt4R"

ciphertext = binascii.unhexlify(cipher_hex)

chacha = ChaCha20Poly1305(key)
plaintext = chacha.decrypt(nonce, ciphertext, None)

print("✅ Berhasil dekripsi:", plaintext.decode())
