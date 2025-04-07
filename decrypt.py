from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from pathlib import Path

key = b"gnzLCH7vxt4R8HyxFWipUPIFpcSTw9Ir"
nonce = b"gnzLCH7vxt4R"

ciphertext = Path("example.zxd").read_bytes()

chacha = ChaCha20Poly1305(key)
plaintext = chacha.decrypt(nonce, ciphertext, None)

print("✅ Berhasil dekripsi:", plaintext.decode())
