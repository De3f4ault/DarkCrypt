from core.encryption import AESEncryptor
from utils.file_utils import secure_delete

def encrypt_file(file_path: str, password: str) -> str:
    """Encrypt a file and return status message"""
    try:
        encryptor = AESEncryptor(password)
        output_path = f"{file_path}.enc"
        encryptor.encrypt_file(file_path, output_path)
        secure_delete(file_path)
        return f"✅ Encrypted: {output_path}"
    except Exception as e:
        return f"❌ Encryption failed: {str(e)}"

def decrypt_file(file_path: str, password: str) -> str:
    """Decrypt a file and return status message"""
    try:
        encryptor = AESEncryptor(password)
        output_path = file_path[:-4] if file_path.endswith(".enc") else f"{file_path}.dec"
        encryptor.decrypt_file(file_path, output_path)
        return f"✅ Decrypted: {output_path}"
    except Exception as e:
        return f"❌ Decryption failed: {str(e)}"
