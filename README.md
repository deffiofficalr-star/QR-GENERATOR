# 📱 QR-GENERATOR

**Генератор QR-кодов для текста, ссылок и Wi-Fi**

---

## 📌 Что это?

QR-GENERATOR — это программа для создания QR-кодов из текста, ссылок и данных для Wi-Fi. Поддерживает настройку цвета, размера и сохранение в PNG.

---

## ✨ Возможности

- 📝 Генерация QR-кода из любого текста
- 🔗 Генерация QR-кода из ссылки
- 📶 Генерация QR-кода для Wi-Fi (SSID + пароль)
- 🎨 Настройка цвета и фона
- 📏 Выбор размера (8–20)
- 💾 Сохранение в PNG
- 📁 Автоматическое создание папки `qr_codes/`

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/deffiofficalr-star/QR-GENERATOR.git
cd QR-GENERATOR
pip install -r requirements.txt
python qr.py
```

---

📁 Структура

```
QR-GENERATOR/
├── qr.py
├── requirements.txt
├── README.md
└── qr_codes/          # создаётся автоматически
```

---

📋 Пример работы

```
📌 Выберите действие:
   1. Сгенерировать QR-код из текста
   2. Сгенерировать QR-код из ссылки
   3. Сгенерировать QR-код для Wi-Fi
   4. Выйти

> 1

📝 Введите текст или ссылку для QR-кода:
> https://github.com/deffiofficalr-star

🎨 Настройки QR-кода:
📁 Имя файла: github
🎨 Цвет: #7c3aed
⬜ Цвет фона: white
📏 Размер: 12

✅ QR-код сохранён: qr_codes/github.png
```

---

🛠 Технологии

· Python 3.8+
· qrcode
· Pillow

---

📬 Связь

Автор: @bytefps

---

📄 Лицензия

MIT

---

QR-GENERATOR © 2026

```
