# Encrypted Backup Code Retriever

A secure tool for retrieving your predetermined backup code using secret inputs. The tool leverages standard cryptographic techniques (PBKDF2 + Fernet encryption) to ensure that only the correct combination of secret inputs will reveal the backup code.

## Overview

This repository contains a simple yet secure system for storing and retrieving backup codes:

1. **Salt Generation (`generate_salt.py`)**: Creates a cryptographic salt file
2. **Code Generation (`generate.py`)**: Encrypts your backup code using three secret inputs
3. **Code Retrieval (`retrieve_backup_code.py`)**: Decrypts and reveals the backup code when provided with the correct secret inputs

### How It Works

- **Generates** a cryptographic salt for added security
- **Encrypts** a backup code using a combination of 3 secret values and the salt
- **Derives** a cryptographic key from these secret values using PBKDF2 with SHA-256 (100,000 iterations)
- **Stores** the encrypted backup code in a file (`encrypted_backup_code.txt`)
- **Decrypts** and reveals the backup code only when all 3 correct secret inputs are provided

**Security Note:** The source code is public, but the backup code remains secure as it cannot be retrieved without knowing all three secret inputs exactly as they were originally provided.

## Features

- **Strong Cryptographic Security:** Uses PBKDF2-HMAC-SHA256 with 100,000 iterations for key derivation
- **Fernet Symmetric Encryption:** Military-grade AES encryption for protecting the backup code
- **Random Salt Generation:** Each setup uses a unique cryptographic salt
- **Deterministic Key Derivation:** Same inputs always produce the same encryption key
- **User-Friendly Interface:** Simple command-line prompts for entering secret inputs
- **File-Based Storage:** Encrypted backup code is stored in a separate file
- **Cross-Platform:** Works on Windows, macOS, and Linux

## Quick Start

### Prerequisites
- Python 3.12 or higher
- Internet connection for installing dependencies

### Setup Process

1. **Clone or Download:**  
   Download this repository to your local machine.

2. **Install Dependencies (Choose One):**
   
   **Option A: Using uv (Recommended)**
   ```bash
   # Install uv first (if not already installed)
   # Windows PowerShell (run as administrator):
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS/Linux:
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Then install dependencies:
   uv sync
   ```
   
   **Option B: Using pip**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Salt (One-Time Setup):**
   ```bash
   # Using uv:
   uv run python generate_salt.py
   
   # Using pip:
   python generate_salt.py
   ```
   This creates a `salt.txt` file that will be used for encryption.

4. **Configure Your Secrets:**
   Edit `generate.py` and modify these lines with your own values:
   ```python
   secret_part1 = "secret1"          # Replace with your first secret
   secret_part2 = "secret2"          # Replace with your second secret  
   secret_part3 = "secret3"          # Replace with your third secret
   backup_code = "BACKUPCODE-123456" # Replace with your actual backup code
   ```

5. **Generate Encrypted Backup Code:**
   ```bash
   # Using uv:
   uv run python generate.py
   
   # Using pip:
   python generate.py
   ```
   This creates an `encrypted_backup_code.txt` file containing your encrypted backup code.

6. **Retrieve Your Backup Code:**
   ```bash
   # Using uv:
   uv run python retrieve_backup_code.py
   
   # Using pip:
   python retrieve_backup_code.py
   ```
   Enter your three secret parts when prompted. If correct, your backup code will be displayed.

## Important Setup Notes

⚠️ **Critical Steps for Security:**

1. **Choose Strong Secret Parts:** Your three secret inputs should be:
   - Memorable to you but not easily guessable
   - Different from each other
   - At least 8 characters long each
   - Can include spaces, numbers, and special characters

2. **Order Matters:** The secrets must be entered in the exact same order they were used during generation.

3. **Case Sensitive:** All inputs are case-sensitive. "Secret" ≠ "secret"

4. **Backup Your Files:** After setup, you must securely store certain files:
   - Your three secret parts (stored securely and separately from files)
   - The `salt.txt` file (**CRITICAL** - without this, recovery is impossible)
   - The `encrypted_backup_code.txt` file (**REQUIRED** - contains your encrypted backup code)
   - The modified `generate.py` with your secrets (store securely, optional backup)

## Critical File Storage Requirements

### 🔒 **Files That MUST Be Stored Safely:**

**[`salt.txt`](salt.txt)** - **CRITICAL PRIORITY**
- Contains the cryptographic salt essential for decryption
- Without this file, your backup code cannot be recovered even with correct secrets
- Store in a secure location (encrypted drive, secure cloud storage, safe deposit box)

**[`encrypted_backup_code.txt`](encrypted_backup_code.txt)** - **REQUIRED**
- Contains your encrypted backup code
- Useless without the salt and secrets, but still required for recovery
- Store in a different secure location from `salt.txt`

### 📋 **Recommended Storage Strategy:**

**Separate Storage Locations:**
- Store `salt.txt` and `encrypted_backup_code.txt` in **different secure locations**
- This ensures no single point of failure can compromise your backup code
- An attacker needs ALL THREE components: salt file + encrypted file + your three secrets

**Multiple Backup Copies:**
- Create multiple copies of both critical files
- Store copies in different physical locations
- Consider encrypted cloud storage with different providers
- Print copies and store in safe deposit boxes for ultimate security

**Security Principle:**
Your backup code requires three components to recover:
1. **Salt file** (`salt.txt`)
2. **Encrypted backup code** (`encrypted_backup_code.txt`)
3. **Your three secret phrases** (stored in your memory)

By storing the files separately, even if one location is compromised, your backup code remains secure.

## Troubleshooting

**"Invalid inputs provided" Error:**
- Double-check that all three secret parts are entered exactly as originally set in `generate.py`
- Verify the order of inputs matches the generation order
- Check for typos, extra spaces, or incorrect capitalization
- Ensure you've run `generate.py` after modifying the secrets

**"Salt file not found" Error:**
- Run `python generate_salt.py` first to create the salt file

**"Encrypted backup code file not found" Error:**
- Run `python generate.py` after setting up your secrets

**"ModuleNotFoundError" Error:**
- Run `pip install -r requirements.txt` or `uv sync`
- Ensure you're using Python 3.12 or higher

## Complete Example Workflow

Here's a step-by-step example:

```bash
# 1. Initial Setup
git clone <repository-url>
cd ciphered-backup
uv sync  # or pip install -r requirements.txt

# 2. Generate salt (one-time)
uv run python generate_salt.py
# Output: Salt generated and saved to 'salt.txt'

# 3. Edit generate.py with your secrets:
# secret_part1 = "MyDogName2023"
# secret_part2 = "Mom'sBirthday-June15"  
# secret_part3 = "FirstCarModel+Year"
# backup_code = "BACKUP-789123-XYZ"

# 4. Generate encrypted backup code
uv run python generate.py
# Output: Encrypted backup code saved to 'encrypted_backup_code.txt'

# 5. Test retrieval
uv run python retrieve_backup_code.py
# Enter secret part 1: MyDogName2023
# Enter secret part 2: Mom'sBirthday-June15
# Enter secret part 3: FirstCarModel+Year
# Your backup code is: BACKUP-789123-XYZ
```

## Security Guidelines

### Best Practices

- **Keep Secrets Separate:** Store your three secret parts in different secure locations
- **Use Strong Secrets:** Each secret should be unique and not easily guessable
- **Don't Share:** Never share your secret inputs with anyone
- **Regular Updates:** Consider updating your backup code and secrets periodically
- **Test Regularly:** Periodically verify you can retrieve your backup code
- **Secure Storage:** Keep backups of `salt.txt` and `encrypted_backup_code.txt` in secure locations

### Security Considerations

- **Random Salt:** The system generates a unique random salt for each setup, stored in `salt.txt`
- **Iterations:** Uses 100,000 PBKDF2 iterations, which provides good protection against brute force attacks
- **Algorithm:** Uses Fernet (AES-128 in CBC mode with HMAC-SHA256 for authentication)

### What This Tool Protects Against

- ✅ **Public Code Repository:** Your backup code is safe even if this code is public
- ✅ **Single Secret Compromise:** All three secrets are required to decrypt
- ✅ **Brute Force Attacks:** PBKDF2 with high iteration count makes this computationally expensive
- ✅ **Salt Reuse:** Each setup generates a unique salt

### What This Tool Does NOT Protect Against

- ❌ **Compromise of all three secrets**
- ❌ **Keyloggers or malware on your system**
- ❌ **Physical access to your computer while unlocked**
- ❌ **Loss of salt.txt file** (backup this file securely)

## Files in This Repository

- **`generate_salt.py`** - Generates a unique cryptographic salt (run once per setup)
- **`salt.txt`** - Contains the cryptographic salt (generated by generate_salt.py)
- **`generate.py`** - Script to create encrypted backup codes (modify this with your secrets)
- **`encrypted_backup_code.txt`** - Contains your encrypted backup code (generated by generate.py)
- **`retrieve_backup_code.py`** - Script to decrypt and retrieve backup codes
- **`requirements.txt`** - Python dependencies for pip users
- **`pyproject.toml`** - Project configuration and dependencies for uv users
- **`uv.lock`** - Locked dependency versions for reproducible builds
- **`main.py`** - [Optional] Additional entry point or utility script
- **`README.md`** - This documentation file

## Contributing

This is a simple cryptographic utility. If you find bugs or have suggestions for security improvements, please open an issue or submit a pull request.

## License

See LICENSE file for details.

## Disclaimer

This tool is provided as-is for educational and personal use. The authors are not responsible for any misuse, data loss, or security breaches. Always follow cryptographic best practices and consider consulting security professionals for production use cases.
