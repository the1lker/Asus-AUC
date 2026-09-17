#!/usr/bin/env python3
# main.py içeriğinin geri kalanı buraya...

from battery import set_battery_limit
from hardware import get_cpu_info, get_gpu_info, get_ram_info, get_ssd_info
from ram_manager import ram_menu


def main_menu():
  while True:
    print("========================================")
    print("       ASUS LINUX SİSTEM KONTROLÜ       ")
    print("========================================")
    print("1) Tüm Donanım Raporunu Göster (CPU, RAM, GPU, SSD)")
    print("2) Batarya Şarj Limiti Ayarla")
    print("3) RAM Kullanan Uygulamaları Listele ve Yönet")
    print("4) Çıkış")

    choice = input("\nİşlem Seçiniz (1-4): ").strip()

    if choice == "1":
      print("\n" + "=" * 40)
      get_cpu_info()
      get_ram_info()
      get_gpu_info()
      get_ssd_info()
      print("=" * 40 + "\n")
    elif choice == "2":
      set_battery_limit()
      print()
    elif choice == "3":
      ram_menu()
    elif choice == "4":
      print("Çıkış yapılıyor...")
      break
    else:
      print("Geçersiz seçim, tekrar deneyin.\n")


if __name__ == "__main__":
  main_menu()