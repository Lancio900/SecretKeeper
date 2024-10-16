from cryptography.fernet import Fernet #type: ignore

def generate_key():
    """Genera una chiave e la salva in un file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carica la chiave dal file."""
    return open("secret.key", "rb").read()

def encrypt_file(file_name):
    """Cripta il file specificato."""
    key = load_key()
    f = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)

    print(f"{file_name} criptato con successo!")
