import os
import hashlib
import json

HASH_DB = "integrity_db.json"

def get_dir_hashes(directory: str) -> dict:
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                hasher = hashlib.sha256()
                with open(path, 'rb') as f:
                    while chunk := f.read(8192):
                        hasher.update(chunk)
                file_hashes[path] = hasher.hexdigest()
            except OSError:
                pass
    return file_hashes

def check_integrity(target_dir: str):
    current_hashes = get_dir_hashes(target_dir)

    if not os.path.exists(HASH_DB):
        print("[*] Criando banco de dados de integridade inicial...")
        with open(HASH_DB, "w") as f:
            json.dump(current_hashes, f, indent=2)
        print("[+] Base inicial registrada.")
        return

    with open(HASH_DB, "r") as f:
        stored_hashes = json.load(f)

    for path, h in current_hashes.items():
        if path not in stored_hashes:
            print(f"[!] NOVO ARQUIVO: {path}")
        elif stored_hashes[path] != h:
            print(f"[!] ARQUIVO MODIFICADO: {path}")

    for path in stored_hashes:
        if path not in current_hashes:
            print(f"[!] ARQUIVO REMOVIDO: {path}")

if __name__ == "__main__":
    check_integrity("./")