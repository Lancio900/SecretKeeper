from cryptography.fernet import Fernet # type: ignore

def load_key():
    """Carica la chiave dal file."""
    return open("secret.key", "rb").read()

def decrypt_file(file_name):
    """Decripta il file specificato."""
    key = load_key()
    f = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(file_name, "wb") as file:
        file.write(decrypted_data)

    print(f"{file_name} decriptato con successo!")
