# Asus-AUC (ASUS Control Center)

Arch Linux üzerinde çalışan, ASUS dizüstü bilgisayarlar için geliştirilmiş modüler ve terminal tabanlı bir sistem kontrol ve yönetim aracıdır. Python ile yazılmış olup, temiz ve modüler bir mimariyi benimser.

# Proje Vibe Codelama ile yapildi

## Özellikler

- **Donanım İzleme (`hardware.py`):** CPU, RAM, GPU ve sistem donanım durumlarını raporlar.
- **Pil Yönetimi (`battery.py`):** Batarya şarj eşiği (threshold) yapılandırmasını kolayca yönetir.
- **Süreç Yöneticisi (`ram_manager.py`):** Kara liste (blacklist) filtreleme özelliğine sahip, PID bazlı güvenli RAM ve süreç yönetimi sağlar.

---

## Kurulum ve Global Komut Yapma

`Asus-AUC` aracını herhangi bir klasörden doğrudan çalıştırabilmek için bir sarmalayıcı (wrapper) betik oluşturup sistem yolunuza (`$PATH`) eklemeniz gerekir. 

Öncelikle projenizin tam yolunu bildiğinizden emin olun (Örnek yolumuz: `~/Projeler/Asus-AUC`).

### 1. Fish Shell İçin
Fish kabuğu kullanıyorsanız şu adımları izleyin:

```fish
# 1. ~/.local/bin dizininin olduğundan emin olun
mkdir -p ~/.local/bin

# 2. Global komut betiğini oluşturun
echo '#!/bin/bash' > ~/.local/bin/Asus-AUC
echo 'cd "$HOME/Projeler/Asus-AUC"' >> ~/.local/bin/Asus-AUC
echo 'python3 main.py' >> ~/.local/bin/Asus-AUC

# 3. Çalıştırma izni verin
chmod +x ~/.local/bin/Asus-AUC

# 4. Yol (PATH) tanımlamasını yapın (kalıcı olarak ekler)
fish_add_path ~/.local/bin
```

### 2. Bash/Zsh Shell İçin
Bash yada Zsh kullanıyorsanız bu komutlarla global komut haline getirin

```bash/zsh
# 1. ~/.local/bin dizininin olduğundan emin olun
mkdir -p ~/.local/bin

# 2. Global komut betiğini oluşturun
cat << 'EOF' > ~/.local/bin/Asus-AUC
#!/bin/bash
cd "$HOME/Projeler/Asus-AUC"
python3 main.py
EOF

# 3. Çalıştırma izni verin
chmod +x ~/.local/bin/Asus-AUC

# 4. Yol (PATH) tanımlamasını yapın (Eğer daha önce eklenmediyse)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # (Bash için)
# veya Zsh kullanıyorsanız:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc  # (Zsh için)
source ~/.zshrc
```

Not: global komut haline manuel olarak getirmek istemiyorsaniz otomasyon bash betiğini kullanın

```installer kullanimi
chmod +x install.sh
./install.sh
```
