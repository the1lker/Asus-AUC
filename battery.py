import os

def set_battery_limit():
    print("\n--- BATARYA ŞARJ LİMİTİ AYARLA ---")
    print("1) %60 (Uzun süreli priz kullanımı için ideal)")
    print("2) %80 (Günlük kullanım için dengeli)")
    print("3) %100 (Tam kapasite)")
    
    choice = input("Seçiminiz (1/2/3): ").strip()
    limit_map = {"1": "60", "2": "80", "3": "100"}
    
    if choice in limit_map:
        target_limit = limit_map[choice]
        battery_path = "/sys/class/power_supply/BAT0/charge_control_limit_max"
        if not os.path.exists(battery_path):
            battery_path = "/sys/class/power_supply/BAT1/charge_control_limit_max"
            
        try:
            command = f"echo {target_limit} | sudo tee {battery_path}"
            result = os.system(command)
            if result == 0:
                print(f"[BAŞARILI] Batarya şarj limiti başarıyla %{target_limit} olarak ayarlandı.")
            else:
                print("[HATA] Komut çalıştırılamadı. Root yetkisi gerekebilir (sudo ile çalıştırın).")
        except Exception as e:
            print(f"[HATA] Bir sorun oluştu: {e}")
    else:
        print("[!] Geçersiz seçim.")