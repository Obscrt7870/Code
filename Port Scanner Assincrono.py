import asyncio
import socket

async def check_port(ip: str, port: int, timeout: float = 1.0):
    conn = asyncio.open_connection(ip, port)
    try: 
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        print(f"[+] Porta {port:5d}/TCP aberta")
        writer.close()
        await writer.wait_closed()
    except (asyncio.TimeoutError, OSError):
        pass

async def main(target: str, ports: list[int]):
    print(f"Escaneando {target}...")
    tasks = [check_port(target, port) for port in ports]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    TARGET_HOST = "127.0.0.1"
    COMMON_PORTS = [21, 22, 80, 443, 3306, 5432, 8080]
    
    asyncio.run(main(TARGET_HOST, COMMON_PORTS))
