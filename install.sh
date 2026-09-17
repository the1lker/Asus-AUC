#!/bin/bash

# Projenin mevcut bulunduğu dizini otomatik olarak al
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$HOME/.local/bin"
TARGET_BIN="$BIN_DIR/Asus-AUC"

echo "[*] Asus-AUC global kurulumu başlatılıyor..."

# 1. ~/.local/bin dizini yoksa oluştur
mkdir -p "$BIN_DIR"

# 2. Wrapper (sarmalayıcı) betiği oluştur
echo "[*] Komut dosyası oluşturuluyor..."
cat << EOF > "$TARGET_BIN"
#!/bin/bash
cd "$PROJECT_DIR"
python3 main.py
EOF

# 3. Çalıştırma izni ver
chmod +x "$TARGET_BIN"

# 4. Aktif kabuğu (Shell) tespit et ve PATH ekle
CURRENT_SHELL="$(basename "$SHELL")"
echo "[*] Tespit edilen kabuk: $CURRENT_SHELL"

case "$CURRENT_SHELL" in
    fish)
        # Fish için kalıcı path ekleme
        if ! fish -c "contains \$HOME/.local/bin \$fish_user_paths" >/dev/null 2>&1; then
            fish -c "set -U fish_user_paths \$fish_user_paths \$HOME/.local/bin"
            echo "[+] ~/.local/bin, Fish path listesine eklendi."
        else
            echo "[=] ~/.local/bin zaten Fish path listesinde mevcut."
        fi
        ;;
    zsh)
        if ! grep -q "\.local/bin" "$HOME/.zshrc" 2>/dev/null; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
            echo "[+] ~/.local/bin, .zshrc dosyasına eklendi."
        else
            echo "[=] ~/.local/bin zaten .zshrc içinde tanımlı."
        fi
        ;;
    bash)
        if ! grep -q "\.local/bin" "$HOME/.bashrc" 2>/dev/null; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
            echo "[+] ~/.local/bin, .bashrc dosyasına eklendi."
        else
            echo "[=] ~/.local/bin zaten .bashrc içinde tanımlı."
        fi
        ;;
    *)
        echo "[!] Bilinmeyen kabuk. Lütfen ~/.local/bin dizinini manuel olarak PATH değişkenine ekleyin."
        ;;
esac

echo "---------------------------------------------------"
echo "[✔] Kurulum tamamlandı!"
echo "[✔] Artık terminalde herhangi bir yerde 'Asus-AUC' yazarak çalıştırabilirsiniz."
echo "    (Not: Değişikliklerin geçerli olması için yeni bir terminal açmanız gerekebilir.)"