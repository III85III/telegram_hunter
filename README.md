<h1 align="center">⚡ TelegramHunter v3.0 ⚡</h1>
<h3 align="center">High-Speed Real Dictionary (+40k Words) & Alphanumeric Telegram Username Scanner</h3>

<p align="center">
  <a href="https://github.com/III85III/telegram_hunter/releases"><img src="https://img.shields.io/github/v/release/III85III/telegram_hunter?color=blue&style=for-the-badge&logo=github" alt="Release" /></a>
  <a href="https://github.com/III85III/telegram_hunter/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" /></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Telethon-MTProto-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telethon MTProto" />
  <img src="https://img.shields.io/badge/NLTK-40k%2B%20Words-orange?style=for-the-badge" alt="NLTK Dictionary" />
  <img src="https://img.shields.io/badge/Security-Safe%20%26%20Zero--Leak-red?style=for-the-badge" alt="Zero Leak Security" />
</p>

<p align="center">
  <b>The fastest and most reliable open-source Telegram username availability scanner & hunter.</b><br>
  Hunt authentic, high-value, 4-letter, 5-letter, and 6-letter Telegram handles using multi-session rotation and real English dictionaries.
</p>

---

## 📑 Table of Contents / فهرست مطالب
- [🌟 Overview / درباره پروژه](#-overview--درباره-پروژه)
- [✨ Key Features / ویژگی‌های کلیدی](#-key-features--ویژگیهای-کلیدی)
- [🖥️ Terminal Interface Preview / پیش‌نمایش محیط برنامه](#️-terminal-interface-preview--پیشنمایش-محیط-برنامه)
- [🚀 Quick Start / نحوه نصب و اجرا](#-quick-start--نحوه-نصب-و-اجرا)
- [📁 Project Structure / ساختار فایل‌ها](#-project-structure--ساختار-فایلها)
- [🛡️ Anti-Flood & Rate Limiting / مدیریت لیمیت](#️-anti-flood--rate-limiting--مدیریت-لیمیت)
- [🔒 Zero-Leak Security Guarantee / امنیت ۱۰۰٪](#-zero-leak-security-guarantee--امنیت-۱۰۰)
- [🔍 SEO Search Keywords / کلیدواژه‌ها](#-seo-search-keywords--کلیدواژهها)
- [📄 License](#-license)

---

## 🌟 Overview / درباره پروژه

**TelegramHunter** is a state-of-the-art Telegram username hunting suite built on the native MTProto protocol via Telethon. Unlike conventional brute-force scripts that scan random, meaningless character combinations (`x8z1q`), TelegramHunter queries an official linguistic database (**NLTK English Corpus with over 40,000+ authentic words**).

پروژه **TelegramHunter** پیشرفته‌ترین اسکنر و شکارچی آیدی‌های تلگرام بر بستر پروتکل رسمی MTProto است. این ابزار به جای تولید کلمات تصادفی و بی‌مصرف، بیش از **۴۰,۰۰۰ کلمه واقعی و معنادار دیکشنری انگلیسی** (شامل کلمات محبوب ۴، ۵ و ۶ حرفی) را با سشن‌های شخصی شما بررسی و یوزرنیم‌های آزاد را فوراً ذخیره می‌کند.

---

## ✨ Key Features / ویژگی‌های کلیدی

- 📖 **Real English Dictionary Database (+40,000 Authentic Words)**:
  - **4-Letter Words**: ~4,000 authentic English words (e.g., `lion`, `echo`, `tech`, `neon`, `flux`).
  - **5-Letter Words**: ~12,000 authentic English words (e.g., `cloud`, `alpha`, `cyber`, `pulse`, `elite`).
  - **6-Letter Words**: ~25,000+ authentic English words (e.g., `shield`, `matrix`, `photon`, `vector`).
  - **All-in-One Mode**: Scans 4-to-6 character dictionary words consecutively (+40,000 words).
- 🔤 **Alphanumeric & Pattern Generation**:
  - Pure alphabet (a-z) exhaustive combinations (4 and 5 characters).
  - Alphanumeric (letters + numbers) combinations.
  - Custom dictionary support: Load any custom wordlist via `wordlist.txt`.
- 👥 **Multi-Session Worker Rotation**:
  - Place multiple Telethon `.session` files into `sessions/` for distributed parallel scanning.
  - Interactive login option directly in the terminal if you don't have session files yet.
- 🛡️ **Intelligent FloodWait Handling**:
  - Automatically intercepts Telegram rate-limit exceptions (`FloodWaitError`), pauses gracefully, and switches workers without crashing.
- 💾 **State Persistence & Checkpoints**:
  - Automatic progress tracking saved in `hunter_state.json`. You can press `Ctrl+C` at any time and resume exactly where you left off.
  - Valid available usernames are appended immediately to `available_usernames.txt`.

---

## 🖥️ Terminal Interface Preview / پیش‌نمایش محیط برنامه

```text
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
   ⚡ TelegramHunter v3.0 | Real Words & Multi-Session Scanner | By III85III ⚡

[12,410/40,215] @pulse          -> TAKEN   | 2.15 req/s
[12,411/40,215] @cyber          -> TAKEN   | 2.15 req/s
🔥 [AVAILABLE FOUND] @neonflux        | Index: 12,412/40,215 | Saved to file!
```

---

## 🚀 Quick Start / نحوه نصب و اجرا

### 1. Requirements
- Python 3.10 or higher
- Operating System: Windows 10/11, Linux, or macOS

### 2. Automatic Setup (Windows)
Run the automated installer:
```cmd
setup.bat
```
*Creates the virtual environment, installs all dependencies, and downloads the 40k+ NLTK word corpus automatically.*

### 3. Launching
```cmd
run.bat
```

### 4. Manual Setup (Linux / macOS)
```bash
git clone https://github.com/III85III/telegram_hunter.git
cd telegram_hunter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -c "import nltk; nltk.download('words')"
python3 hunter.py
```

---

## 📁 Project Structure / ساختار فایل‌ها

```
TelegramHunter/
├── sessions/               # Place your Telethon *.session files here (100% Git-ignored)
├── hunter.py               # Main unified scanner engine with Rich CLI
├── requirements.txt        # Production dependencies (telethon, rich, nltk, python-dotenv)
├── .env.example            # Optional custom API_ID / API_HASH template
├── .gitignore              # Absolute security filter (prevent session & result leaks)
├── setup.bat               # Automated one-click setup script
├── run.bat                 # Automated one-click launcher
├── LICENSE                 # MIT License
└── README.md               # Documentation & Guide
```

---

## 🛡️ Anti-Flood & Rate Limiting / مدیریت لیمیت

To maximize scanning lifespan and avoid Telegram rate limits:
1. Recommended request delay: **1.5 to 3.0 seconds** per account.
2. Distribute workload across multiple accounts by placing multiple `.session` files in the `sessions/` folder.
3. If Telegram returns a `FloodWait` cooldown, TelegramHunter sleeps automatically for the requested duration.

---

## 🔒 Zero-Leak Security Guarantee / امنیت ۱۰۰٪

- **Zero-Logging of Sessions**: The `.gitignore` is hard-configured to ignore all `.session`, `.env`, and `available_usernames.txt` files.
- **Client-Side MTProto**: All API communications connect directly from your machine to Telegram official MTProto gateways. No external proxy, tracking, or telemetry is used.

---

## 🔍 SEO Search Keywords / کلیدواژه‌ها

`telegram username checker` · `telegram username hunter` · `telegram username scanner` · `telethon username availability` · `telegram 4 letter usernames` · `telegram 5 letter usernames` · `telegram dictionary checker` · `telegram osint tools` · `telegram account checker` · `telegram tools python` · `telegram handle checker` · `check telegram username available`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — see the LICENSE file for details.

Developed with ❤️ by **[III85III](https://github.com/III85III)**

