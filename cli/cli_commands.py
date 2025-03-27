import click
from core.encryption import AESEncryptor
from utils.file_utils import secure_delete

@click.group()
def cli():
    """Encrypted File Vault CLI Tool 🔒"""

@cli.command()
@click.option("--input", "-i", required=True, help="File to encrypt")
@click.option("--output", "-o", help="Output file (default: input.enc)")
@click.option("--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True, help="Encryption password")
def encrypt(input, output, password):
    """Encrypt a file"""
    output = output or f"{input}.enc"
    encryptor = AESEncryptor(password)
    encryptor.encrypt_file(input, output)
    secure_delete(input)  # Securely delete original
    click.echo(f"✅ Encrypted: {input} → {output}")

@cli.command()
@click.option("--input", "-i", required=True, help="File to decrypt")
@click.option("--output", "-o", help="Output file (default: input.dec)")
@click.option("--password", "-p", prompt=True, hide_input=True, help="Decryption password")
def decrypt(input, output, password):
    """Decrypt a file"""
    output = output or f"{input}.dec"

    # Read the salt from the encrypted file
    with open(input, "rb") as f:
        salt = f.read(16)  # First 16 bytes = salt

    # Initialize encryptor with the extracted salt
    encryptor = AESEncryptor(password, salt=salt)
    encryptor.decrypt_file(input, output)
    click.echo(f"✅ Decrypted: {input} → {output}")

if __name__ == "__main__":
    cli()
