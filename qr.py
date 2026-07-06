import qrcode
from PIL import Image
import os

class QRGenerator:
    def __init__(self):
        self.output_folder = "qr_codes"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def generate(self, data, filename="qrcode.png", fill_color="black", back_color="white", size=10, border=2):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        filepath = os.path.join(self.output_folder, filename)
        if not filename.endswith('.png'):
            filepath += '.png'
        
        img.save(filepath)
        print(f"✅ QR-код сохранён: {filepath}")
        return filepath
    
    def generate_from_text(self):
        print("\n📝 Введите текст или ссылку для QR-кода:")
        data = input("> ").strip()
        if not data:
            print("❌ Текст не может быть пустым!")
            return
        
        print("\n🎨 Настройки QR-кода (Enter для пропуска):")
        filename = input("📁 Имя файла (без расширения): ").strip() or "qrcode"
        fill = input("🎨 Цвет (например, black, blue, #7c3aed): ").strip() or "black"
        back = input("⬜ Цвет фона (например, white, #ffffff): ").strip() or "white"
        size = input("📏 Размер (8-20, по умолчанию 10): ").strip()
        size = int(size) if size.isdigit() else 10
        size = max(8, min(20, size))
        
        self.generate(data, filename, fill, back, size)
        print(f"📁 Файл сохранён в папке: {self.output_folder}/")
    
    def generate_from_url(self):
        print("\n🔗 Введите ссылку для QR-кода:")
        url = input("> ").strip()
        if not url:
            print("❌ Ссылка не может быть пустой!")
            return
        
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        filename = "url_qrcode"
        self.generate(url, filename, "black", "white", 10)
        print(f"🔗 QR-код для {url} создан!")
    
    def generate_wifi(self):
        print("\n📶 Введите данные для Wi-Fi:")
        ssid = input("📶 Имя сети (SSID): ").strip()
        if not ssid:
            print("❌ SSID обязателен!")
            return
        
        password = input("🔑 Пароль: ").strip()
        encryption = input("🔒 Тип шифрования (WPA/WEP, по умолчанию WPA): ").strip() or "WPA"
        
        wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
        filename = f"wifi_{ssid}"
        self.generate(wifi_data, filename, "black", "white", 12)
        print("📶 QR-код для Wi-Fi создан!")

def main():
    print("""
╔═══════════════════════════════════════════╗
║                                           ║
║   ██████╗ ██████╗                         ║
║   ██╔══██╗██╔══██╗                        ║
║   ██████╔╝██████╔╝                        ║
║   ██╔══██╗██╔══██╗                        ║
║   ██████╔╝██║  ██║                        ║
║   ╚═════╝ ╚═╝  ╚═╝                        ║
║                                           ║
║         QR GENERATOR v1.0                 ║
║                                           ║
╚═══════════════════════════════════════════╝
    """)
    
    generator = QRGenerator()
    
    while True:
        print("\n📌 Выберите действие:")
        print("   1. Сгенерировать QR-код из текста")
        print("   2. Сгенерировать QR-код из ссылки")
        print("   3. Сгенерировать QR-код для Wi-Fi")
        print("   4. Выйти")
        
        choice = input("> ").strip()
        
        if choice == "1":
            generator.generate_from_text()
        elif choice == "2":
            generator.generate_from_url()
        elif choice == "3":
            generator.generate_wifi()
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()
