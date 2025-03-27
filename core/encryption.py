import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class AESEncryptor:
    def __init__(self, password: str, salt: bytes = None):
        self.password = password.encode()
        self.salt = salt or os.urandom(16)
        self.key = self._derive_key()

    def _derive_key(self) -> bytes:
        """Derive a 256-bit AES key using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=600000,
            backend=default_backend()
        )
        return kdf.derive(self.password)

    def encrypt_file(self, input_path: str, output_path: str) -> None:
        """Encrypt a file with AES-256-CBC."""
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()

        with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
            f_out.write(self.salt + iv)  # First 16 bytes = salt, next 16 = IV
            while chunk := f_in.read(4096):  # Process in 4KB chunks
                padded_chunk = padder.update(chunk)
                f_out.write(encryptor.update(padded_chunk))
            f_out.write(encryptor.update(padder.finalize()) + encryptor.finalize())

    def decrypt_file(self, input_path: str, output_path: str) -> None:
        """Decrypt a file."""
        with open(input_path, "rb") as f_in:
            salt_iv = f_in.read(32)  # Read first 32 bytes (salt + IV)
            salt = salt_iv[:16]
            iv = salt_iv[16:32]

            # Re-initialize with the correct salt from the encrypted file
            self.salt = salt
            self.key = self._derive_key()  # Re-derive key with correct salt

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            unpadder = padding.PKCS7(128).unpadder()

            with open(output_path, "wb") as f_out:
                while chunk := f_in.read(4096):
                    decrypted_chunk = decryptor.update(chunk)
                    f_out.write(unpadder.update(decrypted_chunk))
