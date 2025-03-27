# Secure File Vault 🔒

![CLI Demo](https://via.placeholder.com/800x400.png?text=Encryption+CLI+Demo) *(Add real demo GIF later)*

A military-grade file encryption tool with guided workflows and secure deletion, implementing AES-256-CBC encryption.

## 🚀 Features

- **AES-256 Encryption** - FIPS 197 compliant cryptography
- **Guided CLI Interface** - Interactive prompts and progress visualization
- **Secure File Shredding** - 3-pass DoD 5220.22-M compliant deletion
- **Password Security** - PBKDF2 key derivation (600k iterations)
- **Cross-Platform** - Windows/macOS/Linux support
- **Tamper Detection** - File integrity verification

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

```bash
# Clone repository
git clone https://github.com/yourusername/secure-file-vault.git
cd secure-file-vault

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## 🛠️ Usage

### Basic Commands

```bash
# Encrypt a file
python vault.py encrypt -i secret.txt

# Decrypt a file
python vault.py decrypt -i secret.txt.enc
```

### Guided Workflow

```bash
$ python vault.py encrypt
[bold cyan]Welcome to Secure File Vault![/]

📁 Enter file path to encrypt: secret.txt
🔐 Enter encryption password: ***********
🔐 Confirm password: ***********

[Encrypting...] ████████████████ 100%

🚀 Success! Encrypted file: secret.txt.enc
⚠️  Keep your password safe! Recovery impossible without it.
```

### Advanced Options

```bash
# Custom output path
python vault.py encrypt -i secret.txt -o custom.enc

# Batch process directory
python vault.py batch-encrypt ~/sensitive_docs
```

## 🐂 Project Structure

```
secure-file-vault/
├── cli/               # Command-line interface
│   ├── cli_commands.py
│   └── __init__.py
├── core/              # Cryptographic operations
│   ├── encryption.py
│   ├── key_manager.py
│   └── __init__.py
├── utils/             # Security utilities
│   ├── file_utils.py
│   ├── exceptions.py
│   └── __init__.py
├── tests/             # Unit/integration tests
│   ├── test_encryption.py
│   └── __init__.py
├── requirements.txt   # Dependencies
└── vault.py           # Main entry point
```

## 🔒 Security Implementation

### Cryptographic Components
- **AES-256-CBC** - 256-bit key, 128-bit blocks
- **PBKDF2-HMAC-SHA256** - Key stretching (600,000 iterations)
- **PKCS7 Padding** - Secure message padding scheme
- **Random IVs** - 16-byte initialization vectors

### Secure Deletion Process
- Overwrite file 3x with random data
- Rename file with random string
- Truncate file size
- Delete file permanently

## 🧪 Bash Scripting Control Structures

### If-Else Statement Examples

```bash
# Checking for File Existence and Type
if [ -e "$file_path" ]; then
    if [ -d "$file_path" ]; then
        echo "It's a directory."
    elif [ -f "$file_path" ]; then
        echo "It's a regular file."
    else
        echo "It's another type of file."
    fi
else
    echo "File does not exist."
fi
```

```bash
# Network Connectivity Check
ping -c 1 google.com &> /dev/null
if [ $? -eq 0 ]; then
    echo "Internet is connected."
else
    echo "No internet connection."
fi
```

### Case Statement Example

```bash
# Days of the Week
case $day in
    1) echo "Sunday" ;;
    2) echo "Monday" ;;
    3) echo "Tuesday" ;;
    4) echo "Wednesday" ;;
    5) echo "Thursday" ;;
    6) echo "Friday" ;;
    7) echo "Saturday" ;;
    *) echo "Invalid number" ;;
esac
```

### For Loop Example

```bash
# Listing Files in Directory
for file in *; do
    echo "$file"
done
```

### While Loop Example

```bash
# Countdown Timer
count=10
while [ $count -gt 0 ]; do
    echo "$count"
    count=$((count - 1))
    sleep 1
done
echo "Countdown finished!"
```

## 🧪 Testing

Run comprehensive test suite:

```bash
pytest tests/ -v
```

Sample test cases:
- Round-trip encryption/decryption
- Password verification tests
- File tampering detection
- Memory safety checks

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📚 License

Distributed under MIT License. See `LICENSE` for details.

## 🛡️ Support

For issues/feature requests:
- Open GitHub Issue

**Security Notice:** Always store passwords in a secure manager like Bitwarden or 1Password.

**Disclaimer:** Use at your own risk. Developers not liable for data loss.

## 🔍 Key Elements to Customize
1. Add real demo GIF/video
2. Update GitHub URLs
3. Add contributor guidelines
4. Include CI/CD badges
5. Add API documentation links if applicable

