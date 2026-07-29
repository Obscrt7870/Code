import bcrypt

def hash_password(password: str) -> bytes:
    # Gera um salt e calcula o hash
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

if __name__ == "__main__":
    pwd = "SenhaForte@2026!"
    
    hashed = hash_password(pwd)
    print(f"Senha original: {pwd}")
    print(f"Hash BCRYPT:    {hashed.decode('utf-8')}")
    
    is_valid = verify_password(pwd, hashed)
    print(f"[+] Validação correta? {is_valid}")