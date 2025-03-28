from cryptography.fernet import Fernet

class KeyManager:
    @staticmethod
    def generate_key() -> bytes:
        return Fernet.generate_key()
