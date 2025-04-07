from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from pathlib import Path

key = Path("password/key.txt").read_text().strip().encode()
nonce = Path("password/nonce.txt").read_text().strip().encode()

input_dir = Path("locked")
output_dir = Path("result")

output_dir.mkdir(exist_ok=True)

def bin_to_bytes(bin_data):
    bin_str = bin_data.decode()
    return bytes(int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8))

chacha = ChaCha20Poly1305(key)

for file in input_dir.glob("*.zxd"):
    encrypted = file.read_bytes()

    for _ in range(3):
        encrypted = bin_to_bytes(encrypted)

    plaintext = chacha.decrypt(nonce, encrypted, None)

    output_file = output_dir / file.stem
    output_file.write_bytes(plaintext)

    print(f"✅ Didekripsi: {file.name} -> {output_file}")
