class VaultError(Exception):
    """Base exception class for vault operations"""
    def __init__(self, message: str, resolution: str):
        super().__init__(f"{message}\n💡 Resolution: {resolution}")

class EncryptionError(VaultError):
    """Encryption-specific errors"""
    def __init__(self, message: str):
        super().__init__(message, "Check file permissions and password strength")
