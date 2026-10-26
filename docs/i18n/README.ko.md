<!-- language-selector:start -->
<p align="center">
<a href="../../README.md" title="English"><img src="flags/gb.svg" width="30" height="20" alt="English"></a>
<a href="README.fa.md" title="فارسی"><img src="flags/ir.svg" width="30" height="20" alt="فارسی"></a>
<a href="README.es.md" title="Español"><img src="flags/es.svg" width="30" height="20" alt="Español"></a>
<a href="README.fr.md" title="Français"><img src="flags/fr.svg" width="30" height="20" alt="Français"></a>
<a href="README.de.md" title="Deutsch"><img src="flags/de.svg" width="30" height="20" alt="Deutsch"></a>
<a href="README.pt-BR.md" title="Português"><img src="flags/br.svg" width="30" height="20" alt="Português"></a>
<a href="README.it.md" title="Italiano"><img src="flags/it.svg" width="30" height="20" alt="Italiano"></a>
<a href="README.ru.md" title="Русский"><img src="flags/ru.svg" width="30" height="20" alt="Русский"></a>
<a href="README.zh-CN.md" title="简体中文"><img src="flags/cn.svg" width="30" height="20" alt="简体中文"></a>
<a href="README.ja.md" title="日本語"><img src="flags/jp.svg" width="30" height="20" alt="日本語"></a>
<a href="README.ko.md" title="한국어"><img src="flags/kr.svg" width="30" height="20" alt="한국어"></a>
<a href="README.ar.md" title="العربية"><img src="flags/sa.svg" width="30" height="20" alt="العربية"></a>
<a href="README.hi.md" title="हिन्दी"><img src="flags/in.svg" width="30" height="20" alt="हिन्दी"></a>
<a href="README.bn.md" title="বাংলা"><img src="flags/bd.svg" width="30" height="20" alt="বাংলা"></a>
<a href="README.ur.md" title="اردو"><img src="flags/pk.svg" width="30" height="20" alt="اردو"></a>
<a href="README.tr.md" title="Türkçe"><img src="flags/tr.svg" width="30" height="20" alt="Türkçe"></a>
<a href="README.id.md" title="Bahasa Indonesia"><img src="flags/id.svg" width="30" height="20" alt="Bahasa Indonesia"></a>
<a href="README.vi.md" title="Tiếng Việt"><img src="flags/vn.svg" width="30" height="20" alt="Tiếng Việt"></a>
<a href="README.th.md" title="ไทย"><img src="flags/th.svg" width="30" height="20" alt="ไทย"></a>
<a href="README.pl.md" title="Polski"><img src="flags/pl.svg" width="30" height="20" alt="Polski"></a>
</p>
<!-- language-selector:end -->

# TelegramHunter

**한국어**

TelegramHunter는 Telethon과 NLTK로 Telegram 사용자 이름을 확인하고 결과와 진행 상황을 저장합니다. Python 3.10+가 필요하며 setup.bat 다음 run.bat를 실행합니다. 본인 계정을 사용하고 Telegram 제한을 지키며 세션 파일을 공개하지 마세요.

> 이 페이지는 소개와 설치 안내를 번역한 것이며 앱의 표시 언어는 변경하지 않습니다.

## 필수 환경

Python 3.10+ · Telegram · Internet

## 소스 코드 받기

```bash
git clone https://github.com/III85III/telegram_hunter.git
cd telegram_hunter
```

## 설치 · 실행

**Windows**

```bat
setup.bat
run.bat
```

**Linux / macOS**

```bash
python3 -m venv venv
. venv/bin/activate
python -m pip install -r requirements.txt
python -c "import nltk; nltk.download('words')"
python hunter.py
```

## 원본 문서 및 기술 정보

[README](../../README.md) · [GitHub](https://github.com/III85III/telegram_hunter)

[LICENSE](../../LICENSE)
