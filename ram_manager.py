import getpass
import os
import signal
import psutil

def ram_menu():
    BLACKLIST = {
        "gnome-shell", "xwayland", "wayland", "kwin", 
        "plasmashell", "Xorg", "systemd", "pipewire"
    }

    while True:
        print("\n" + "=" * 40)
        print("          RAM KULLANAN UYGULAMALAR          ")
        print("=" * 40)

        current_user = getpass.getuser()
        procs = []

        for p in psutil.process_iter(['pid', 'name', 'memory_info', 'username']):
            try:
                if p.info['username'] == current_user and p.info['memory_info']:
                    p_name = p.info['name']
                    if p_name.lower() not in [b.lower() for b in BLACKLIST]:
                        mem_mb = p.info['memory_info'].rss / (1024 * 1024)
                        procs.append({
                            'pid': p.info['pid'],
                            'name': p_name,
                            'mem_mb': mem_mb
                        })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        procs = sorted(procs, key=lambda x: x['mem_mb'], reverse=True)[:20]

        if not procs:
            print("Çalışan uygun kullanıcı uygulaması bulunamadı.")
            return

        for i, proc in enumerate(procs, 1):
            print(f"{i}) {proc['name']} (PID: {proc['pid']}) — {proc['mem_mb']:.2f} MB")

        back_option = len(procs) + 1
        print(f"{back_option}) Ana Menüye Dön")

        choice = input(f"\nKapatmak istediğiniz uygulamanın numarasını girin (1-{len(procs)}): ").strip()

        if choice.isdigit():
            choice_num = int(choice)
            if choice_num == back_option:
                break
            elif 1 <= choice_num <= len(procs):
                target_proc = procs[choice_num - 1]
                target_pid = target_proc['pid']
                app_name = target_proc['name']
                
                try:
                    print(f"\n[BİLGİ] {app_name} (PID: {target_pid}) güvenli bir şekilde kapatılıyor...")
                    os.kill(target_pid, signal.SIGTERM)
                    print(f"[BAŞARILI] İşlem sonlandırıldı.")
                except Exception as e:
                    print(f"[HATA] İşlem kapatılamadı: {e}")
                    
                input("\nDevam etmek için Enter'a basın...")
            else:
                print("[!] Geçersiz seçim.")
        else:
            print("[!] Lütfen geçerli bir sayı girin.")