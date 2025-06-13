# Encrypted Backup Retriever

A secure tool for retrieving your predetermined backup code using secret inputs. The tool leverages standard cryptographic techniques to ensure that only the correct inputs will reveal the backup code.

## Overview

This repository contains a program that:
- **Encrypts** a backup code using a combination of secret values.
- **Derives** an encryption key from these secret values.
- **Decrypts** and reveals the backup code when the correct inputs are provided.

**Note:** The source code is public, but the backup code remains secure as it cannot be retrieved without the correct secret inputs.

## Features

- **Deterministic Key Derivation:** Uses a well-known key derivation function.
- **Symmetric Encryption:** The backup code is securely encrypted.
- **User-Friendly:** Simply input your secret parts to retrieve your backup code.

## Usage

1. **Setup:**  
   Ensure you have Python 3 installed along with the required dependencies. You can install the dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
   *(The `requirements.txt` file should list the necessary libraries, such as `cryptography`.)*

2. **Retrieving the Backup Code:**  
   Run the program:
   ```bash
   python retrieve_backup_code.py
   ```
   You will be prompted to enter your secret parts. If all inputs are correct, your backup code will be displayed.

## Security Notice

- The security of this tool relies on the secrecy of your input values.  
- **Do not** share your secret inputs with anyone.
- Ensure your secret inputs are stored securely and are not guessable.

## Disclaimer

This tool is provided as-is. The author is not responsible for any misuse or unintended consequences of its use. Always follow best practices for securing sensitive information.
