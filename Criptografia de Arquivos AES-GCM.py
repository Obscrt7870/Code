import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_data(data: bytes, key: bytes) -> tuple[bytes, bytes]:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # Nonce de 96 bits recomendado para GCM
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce, ciphertext

def decrypt_data(nonce: bytes, ciphertext: bytes, key: bytes) -> bytes:
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)

if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256)
    message = b"Informacao confidencial de auditoria"

    nonce, encrypted = encrypt_data(message, key)
    print(f"Cifrado (hex): {encrypted.hex()}")

    decrypted = decrypt_data(nonce, encrypted, key)
    print(f"Decifrado:    {decrypted.decode()}")