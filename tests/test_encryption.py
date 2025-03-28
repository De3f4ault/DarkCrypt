import pytest
from core.encryption import AESEncryptor
import os

def test_encryption_roundtrip(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("secret data")
    
    encryptor = AESEncryptor("password123")
    encrypted = tmp_path / "test.enc"
    decryptor = AESEncryptor("password123")
    
    encryptor.encrypt_file(str(test_file), str(encrypted))
    decryptor.decrypt_file(str(encrypted), str(tmp_path / "decrypted.txt"))
    
    assert (tmp_path / "decrypted.txt").read_text() == "secret data"
