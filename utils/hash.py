from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()

def verify_password(password: str, hash: str):
        return password_hasher.verify(password, hash)

def create_hash(password: str):
    password_hash = password_hasher.hash(password)
    return password_hash
