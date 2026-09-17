import os
import psutil

def get_cpu_model():
    try:
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if "model name" in line:
                    return line.split(":")[1].strip()
    except Exception:
        pass
    return "CPU modeli okunamadı"

def get_cpu_info():
    print("--- CPU BİLGİLERİ ---")
    print(f"İşlemci Model: {get_cpu_model()}")
    print(f"Fiziksel Çekirdek Sayısı: {psutil.cpu_count(logical=False)}")
    print(f"Toplam Çekirdek (Mantıksal): {psutil.cpu_count(logical=True)}")
    print(f"Anlık CPU Kullanım Oranı: %{psutil.cpu_percent(interval=1)}")
    print(f"Anlık Frekans: {psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else "Frekans bilgisi alınamadı.")
    print()

def get_ram_info():
    print("--- RAM BİLGİLERİ ---")
    mem = psutil.virtual_memory()
    total_gb = mem.total / (1024 ** 3)
    available_gb = mem.available / (1024 ** 3)
    used_gb = mem.used / (1024 ** 3)
    
    print(f"Toplam RAM: {total_gb:.2f} GB")
    print(f"Kullanılan RAM: {used_gb:.2f} GB (%{mem.percent})")
    print(f"Boş (Available) RAM: {available_gb:.2f} GB")
    print()

def get_gpu_info():
    print("--- GPU BİLGİLERİ ---")
    gpu_found = False
    try:
        lspci_output = os.popen("lspci | grep -i vga").read()
        if lspci_output:
            print(f"Grafik Denetleyicileri:\n{lspci_output.strip()}")
            gpu_found = True
    except Exception:
        pass
    
    if os.system("which nvidia-smi > /dev/null 2>&1") == 0:
        gpu_name = os.popen("nvidia-smi --query-gpu=name --format=csv,noheader").read().strip()
        gpu_util = os.popen("nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader").read().strip()
        gpu_mem = os.popen("nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader").read().strip()
        print(f"NVIDIA GPU Model: {gpu_name}")
        print(f"GPU Kullanımı: {gpu_util}")
        print(f"GPU VRAM Kullanımı (Kullanılan / Toplam): {gpu_mem}")
        gpu_found = True
        
    if not gpu_found:
        print("Harici GPU bilgisi bulunamadı veya sürücü aktif değil.")
    print()

def get_ssd_info():
    print("--- SSD / DEPOLAMA BİLGİLERİ ---")
    disk = psutil.disk_usage('/')
    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    
    print(f"Ana Disk (/) Toplam Alan: {total_gb:.2f} GB")
    print(f"Kullanılan Alan: {used_gb:.2f} GB (%{disk.percent})")
    print(f"Boş Alan: {free_gb:.2f} GB")
    print()