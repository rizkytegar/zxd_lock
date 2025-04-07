from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from pathlib import Path

# Path file terenkripsi
cipher_path = Path("/__temp__/v01/example.zxd.lock")
ciphertext = cipher_path.read_bytes()

# Key dan nonce yang diberikan
key = b"gnzLCH7vxt4R8HyxFWipUPIFpcSTw9Ir"
nonce = b"gnzLCH7vxt4R"

# Dekripsi
try:
    chacha = ChaCha20Poly1305(key)
    plaintext = chacha.decrypt(nonce, ciphertext, None)

    print("✅ Dekripsi berhasil")
    Path("decrypted_output.bin").write_bytes(plaintext)
except Exception as e:
    print(f"❌ Gagal dekripsi: {e}")
