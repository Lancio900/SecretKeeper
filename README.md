# SecretKeeper

**SecretKeeper** is a simple file encryption and decryption program written in Python. It allows users to securely encrypt files using a generated key, ensuring that only individuals with the key can access the original content.

## Features

- **File Encryption**: Encrypt your files to protect sensitive information.
- **File Decryption**: Decrypt files using the same key to access the original content.
- **Key Management**: Automatically generates and saves a unique encryption key if one does not exist.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies by running:

   ```bash
   pip install cryptography

## Example

Welcome to SecretKeeper.
A file encryption/decryption program.
Generating a new key...
Do you want to encrypt (c) or decrypt (d) a file? c
Enter the name of the file (with extension): example.txt
File encrypted successfully!
