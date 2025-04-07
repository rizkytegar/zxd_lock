from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from pathlib import Path
import binascii

key = b"gnzLCH7vxt4R8HyxFWipUPIFpcSTw9Ir"
nonce = b"gnzLCH7vxt4R"

data = Path("example.zxd").read_bytes()

try:
    ciphertext = binascii.unhexlify(data.strip())
except Exception:
    ciphertext = data  # asumsi data sudah biner

chacha = ChaCha20Poly1305(key)
plaintext = chacha.decrypt(nonce, ciphertext, None)

print("✅ Berhasil dekripsi:", plaintext.decode())
