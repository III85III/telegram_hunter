<h1 align="center">⚡ TelegramHunter v3.0 ⚡</h1>
<h3 align="center">High-Speed Real Dictionary & Alphanumeric Telegram Username Scanner</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Telethon-MTProto-green?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/NLTK-40k%2B%20Words-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Security-Safe%20%26%20Zero--Leak-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Author-III85III-purple?style=for-the-badge" />
</p>

---

## 🌟 Overview / درباره پروژه

**TelegramHunter** is an advanced, high-performance Telegram username hunting and checking engine designed to scan **over 40,000+ real, meaningful English dictionary words** as well as 4-character, 5-character, and 6-character combinations.

Unlike basic random string generators that test meaningless gibberish, TelegramHunter leverages official linguistic corpora (NLTK) to hunt **real, valuable, and branded Telegram handles**.

پروژه **TelegramHunter** یک اسکنر سریع و هوشمند برای کشف یوزرنیم‌های آزاد و ارزشمند تلگرام است. این ابزار به جای تولید کاراکترهای رندوم و بی‌معنی، بیش از **۴۰,۰۰۰ کلمه واقعی و معنادار دیکشنری انگلیسی** (۴، ۵ و ۶ حرفی) را با سشن‌های شخصی شما بررسی و ثبت می‌کند.

---

## ✨ Key Features / ویژگی‌های کلیدی

- 📖 **Real Dictionary Hunting (+40k Words)**:
  - 4-Letter English words (~4,000 words like `lion`, `echo`, `tech`)
  - 5-Letter English words (~12,000 words like `cloud`, `alpha`, `cyber`)
  - 6-Letter English words (~25,000+ words like `shield`, `matrix`, `photon`)
  - Combined multi-length dictionary mode (+40,000 real words)
- 🔤 **Alphanumeric & Pattern Modes**:
  - Pure alphabet (a-z) combinations (4 and 5 characters)
  - Alphanumeric (a-z0-9) combinations
  - Custom file support (`wordlist.txt`)
- 👥 **Multi-Session Rotation**:
  - Drop multiple Telethon `.session` files into `sessions/` for parallel distributed checking.
  - Interactive phone number login directly inside the console if you don't have a `.session` file yet.
- 🛡️ **FloodWait Protection & Intelligent Throttling**:
  - Automatically captures Telegram FloodWait RPC exceptions, sleeps gracefully, and rotates workers.
- 💾 **Safe Auto-Resume & Results Logging**:
  - Checkpoint tracking saves your exact progress in `hunter_state.json` — resume anytime after closing with `Ctrl+C`.
  - Available usernames are saved instantly to `available_usernames.txt`.
- 🔒 **Zero-Leak Architecture**:
  - Strict `.gitignore` ensures that `.env`, `.session` files, and found usernames are NEVER committed to GitHub.

---

## 🚀 Quick Start / نحوه نصب و اجرا

### 1. Requirements
- Python 3.10 or higher
- Windows 10/11 or Linux / macOS

### 2. Automatic Installation (Windows)
Simply run the automatic installer:
```cmd
setup.bat
```
This will create a virtual environment, install all dependencies, and download the NLTK English words corpus.

### 3. Launching
Run:
```cmd
run.bat
```

### 4. Manual Installation (Linux / macOS / Manual)
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 -c "import nltk; nltk.download('words')"
python3 hunter.py
```

---

## 📁 Project Structure / ساختار فایل‌ها

```
TelegramHunter/
├── sessions/               # Place your Telethon .session files here (Git-ignored)
├── hunter.py               # Main unified scanner engine with Rich CLI
├── requirements.txt        # Dependencies (telethon, rich, nltk, python-dotenv)
├── .env.example            # Optional custom API_ID / API_HASH template
├── .gitignore              # Absolute security filter (no leaks)
├── setup.bat               # One-click automated setup
├── run.bat                 # One-click launcher
└── README.md               # Project documentation
```

---

## 🔒 Security Notice / نکات امنیتی

- **Never share or commit files from the `sessions/` directory.** They contain full access to your Telegram accounts.
- This repository has a strict `.gitignore` pre-configured to keep your sessions, tokens, and scanned output 100% private.
- Always use dedicated accounts and sensible rate limits (recommended delay: 1.5 - 3.0 seconds per worker) to prevent temporary Telegram rate limits.

---

## 👤 Author
Developed with ❤️ by **[III85III](https://github.com/III85III)**
