import base64, sys from cryptography.hazmat.primitives.kdf.pbkdf2 
import PBKDF2HMAC from cryptography.hazmat.primitives 
import hashes from cryptography.fernet import Fernet

SALT = b"novatech-lab-salt-2024"

def key_from_password(password: str) -> bytes: kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=SALT, iterations=100_000) return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt(infile, outfile, password): open(outfile, "wb").write(Fernet(key_from_password(password)).encrypt(open(infile, "rb").read()))

def decrypt(infile, outfile, password): open(outfile, "wb").write(Fernet(key_from_password(password)).decrypt(open(infile, "rb").read()))

if name == "main": op, inf, outf, pwd = sys.argv[1:5] # ex: python crypto.py encrypt fin.xlsx fin.crypto "V3rao@2024!" (encrypt if op == "encrypt" else decrypt)(inf, outf, pwd)
