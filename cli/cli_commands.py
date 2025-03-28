import click
import inquirer
import time
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from core.encryption import AESEncryptor
from utils.file_utils import secure_delete

console = Console()
error_console = Console(stderr=True, style="bold red")

@click.group()
@click.version_option("1.0.0")
def cli():
    """🔒 Secure File Vault - Guided Encryption/Decryption Tool"""
    console.print("\n[bold cyan]Welcome to Secure File Vault![/]\n")
    console.print("  • Use [bold]encrypt[/] to protect a file")
    console.print("  • Use [bold]decrypt[/] to recover a file")

def validate_file(ctx, param, value):
    path = Path(value)
    if not path.exists():
        error_console.print(f"❌ Error: File '{value}' not found!")
        ctx.abort()
    return str(path)

@cli.command()
@click.option("--input", "-i", callback=validate_file, help="File to encrypt")
def encrypt(input):
    """🔒 Encrypt a file with guided steps"""
    try:
        with Progress() as progress:
            if not input:
                input = click.prompt("📁 Enter file path to encrypt", type=click.Path(exists=True))
            
            # Password handling
            password = inquirer.prompt([
                inquirer.Password("pass", message="Enter encryption password", validate=lambda _, x: len(x) >= 8)
            ])["pass"]
            
            # Encryption process
            task = progress.add_task("[cyan]Encrypting...", total=100)
            encryptor = AESEncryptor(password)
            output = f"{input}.enc"
            
            for _ in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)
            
            encryptor.encrypt_file(input, output)
            secure_delete(input)
            
            console.print(f"\n✅ [bold green]Success![/] Encrypted file: [underline]{output}[/]")

    except Exception as e:
        error_console.print(f"❌ Encryption failed: {str(e)}")
        raise click.Abort()

# Similar decrypt command would follow
