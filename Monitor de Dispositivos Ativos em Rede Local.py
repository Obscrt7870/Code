import asyncio
import subprocess
import platform
 
async def ping_host(ip: str):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", param, "1", "-w", "1000", ip]
    
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    await proc.communicate()
    
    if proc.returncode == 0:
        print(f"[+] Host ativo: {ip}")

async def main(network_prefix: str):
    print(f"[*] Escaneando sub-rede {network_prefix}.0/24...")
    tasks = [ping_host(f"{network_prefix}.{i}") for i in range(1, 255)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Altere para a sua faixa de rede local
    asyncio.run(main("192.168.1"))
