from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from pathlib import Path
import shutil

key = Path("password/key.txt").read_text().strip().encode()
nonce = Path("password/nonce.txt").read_text().strip().encode()

input_dir = Path("example")
temp_dir = Path("encrypted")
result_dir = Path("locked")

temp_dir.mkdir(exist_ok=True)
result_dir.mkdir(exist_ok=True)

chacha = ChaCha20Poly1305(key)

def bytes_to_bin(data):
    return ''.join(format(byte, '08b') for byte in data).encode()

for file in input_dir.glob("*"):
    if file.is_file():
        data = file.read_bytes()

        encrypted = chacha.encrypt(nonce, data, None)

        for _ in range(3):
            encrypted = bytes_to_bin(encrypted)

        encrypted_path = temp_dir / (file.name + ".zxd")
        encrypted_path.write_bytes(encrypted)

        final_path = result_dir / encrypted_path.name
        shutil.move(str(encrypted_path), final_path)

        print(f"✅ Enkripsi selesai dan dipindah: {file.name} -> {final_path}")
