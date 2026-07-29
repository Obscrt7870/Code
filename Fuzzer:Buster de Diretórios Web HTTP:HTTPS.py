import asyncio
import aiohttp

TARGET_URL = "http://127.0.0.1:8000"
WORDLIST = ["admin", "login", "uploads", "backup.zip", "config.php", "db.sqldump"]

async def fetch(session: aiohttp.ClientSession, path: str):
    url = f"{TARGET_URL.rstrip('/')}/{path}"
    try:
        async with session.get(url, timeout=3) as resp:
            if resp.status != 404:
                print(f"[{resp.status}] Encontrado: /{path}")
    except Exception:
        pass

async def main():
    print(f"[*] Iniciando fuzzing em {TARGET_URL}...")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, word) for word in WORDLIST]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())