import hashlib
 
def calculate_hashes(filepath: str):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    print(f"Arquivo: {filepath}")
    print(f"  MD5:    {md5.hexdigest()}")
    print(f"  SHA1:   {sha1.hexdigest()}")
    print(f"  SHA256: {sha256.hexdigest()}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        calculate_hashes(sys.argv[1])
    else:
        print("Uso: python script.py <caminho_do_arquivo>")
