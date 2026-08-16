import subprocess
import psutil
import time

def limpar_terminal():
    subprocess.run("clear")

def menu_logo():
    print("""
╔═════════════════════════════╗
║       Nicolinux-nStats      ║
║     Monitor de Recursos     ║
╚═════════════════════════════╝
""")

while True:
    cpu_uso = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq(percpu=True)
    cpu_fisica = psutil.cpu_count(logical=False)
    cpu_logica = psutil.cpu_count(logical=True)

    memoria = psutil.virtual_memory()
    ram_uso = memoria.percent
    ram_usada = memoria.used / (1024 ** 3)
    ram_disponivel = memoria.available / (1024 ** 3)
    
    disco = psutil.disk_usage("/")

    limpar_terminal()
    menu_logo()

    print(f"Uso da CPU: {cpu_uso:.1f}%")
    
    for i, freq in enumerate(cpu_freq):
        print(f"CPU {i}: {freq.current / 1000:.2f} GHz")
        
    print(f"Núcleos físicos: {cpu_fisica}")
    print(f"Núcleos lógicos: {cpu_logica}")

    print(f"\nUso de RAM: {ram_uso:.1f}%")
    print(f"RAM usada: {ram_usada:.1f} GB")
    print(f"RAM disponível: {ram_disponivel:.1f} GB")

    print(f"\nUso do disco: {disco.percent}%")
    print(f"Espaço usado: {disco.used / (1024 ** 3):.1f} GB")
    print(f"Espaço livre: {disco.free / (1024 ** 3):.1f} GB")
    print(f"Espaço total: {disco.total / (1024 ** 3):.1f} GB")
    print("-" * 30)

    time.sleep(3)
