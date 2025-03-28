import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class AESEncryptor:
    def __init__(self, password: str, salt: bytes = None):
        self.salt = salt or os.urandom(16)
        self.key = self._derive_key(password.encode())
    
    def _derive_key(self, password: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=600000,
            backend=default_backend()
        )
        return kdf.derive(password)
    
    def encrypt_file(self, input_path: str, output_path: str) -> None:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()

        with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
            f_out.write(self.salt + iv)
            while chunk := f_in.read(4096):
                padded = padder.update(chunk)
                f_out.write(encryptor.update(padded))
            f_out.write(encryptor.update(padder.finalize()) + encryptor.finalize())
