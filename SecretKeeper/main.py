import time
import os
from cript import encrypt_file, generate_key
from decript import decrypt_file

def main():
    print("Welcome to SecretKeeper.")
    print("A file encryption/decryption program.")
    
    if not os.path.exists("secret.key"):
        print("Generating a new key...")
        time.sleep(2)
        generate_key()

    choice = input("Do you want to encrypt (c) or decrypt (d) a file? ").lower()

    file_name = input("Enter the name of the file (with extension): ")

    if choice == 'c':
        encrypt_file(file_name)
        print("File encrypted successfully!")
        input()
    elif choice == 'd':
        decrypt_file(file_name)
        print("File decrypted successfully!")
        input()
    else:
        print("Invalid choice!")
        input()

if __name__ == "__main__":
    main()
