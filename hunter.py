#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
==============================================================================
TelegramHunter - Ultimate High-Speed Telegram Username Scanner & Hunter
Author: III85III
Repository: https://github.com/III85III/telegram_hunter
==============================================================================
"""

import os
import sys
import glob
import json
import time
import string
import itertools
import asyncio
from pathlib import Path
from datetime import datetime

# Third-party libraries
try:
    from telethon import TelegramClient, errors, functions
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, IntPrompt, Confirm
    from rich.live import Live
except ImportError:
    print("[!] Required packages missing. Please run 'setup.bat' or install requirements.txt first.")
    sys.exit(1)

# NLTK for real dictionary words
try:
    import nltk
    try:
        nltk.data.find('corpora/words')
    except (LookupError, AttributeError):
        print("[*] Downloading NLTK English words corpus (one-time setup)...")
        nltk.download('words', quiet=True)
    from nltk.corpus import words
except Exception as e:
    words = None

# Configuration
BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "sessions"
SESSIONS_DIR.mkdir(exist_ok=True)
STATE_FILE = BASE_DIR / "hunter_state.json"
RESULTS_FILE = BASE_DIR / "available_usernames.txt"

# Default Telegram API credentials (can be overridden via .env or environment)
API_ID = int(os.getenv("TELEGRAM_API_ID", "2040"))
API_HASH = os.getenv("TELEGRAM_API_HASH", "b18441a1ff607e10a989891a5462e627")

console = Console()

BANNER = """[bold cyan]
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
[/bold cyan]
[bold yellow]   ⚡ TelegramHunter v3.0 | Real Words & Multi-Session Scanner | By III85III ⚡[/bold yellow]
"""


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"last_index": 0, "session_mode": ""}


def save_state(index: int, mode_name: str = ""):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({"last_index": index, "session_mode": mode_name}, f)
    except Exception:
        pass


def save_found_username(username: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(f"@{username} | Available | {timestamp}\n")


class TelegramHunter:
    def __init__(self):
        self.clients = []
        self.channels = []
        self.wordlist = []
        self.total_checked = 0
        self.available_found = 0
        self.taken_count = 0
        self.errors_count = 0
        self.start_time = None

    async def setup_sessions(self) -> bool:
        session_files = list(SESSIONS_DIR.glob("*.session"))

        if not session_files:
            console.print(Panel(
                "[yellow]No .session files found in the 'sessions/' directory.[/yellow]\n\n"
                "[cyan]You can either:[/cyan]\n"
                " 1. Copy your existing Telethon [bold]*.session[/bold] files into [bold]sessions/[/bold]\n"
                " 2. Log in directly now with your phone number to create a new session.",
                title="[bold yellow]Session Setup[/bold yellow]", border_style="yellow"
            ))

            add_now = Confirm.ask("Do you want to log in a Telegram account right now?")
            if not add_now:
                console.print("[red][!] Please place at least one .session file in the sessions/ folder and restart.[/red]")
                return False

            session_name = Prompt.ask("Enter a session nickname", default="account1")
            session_path = str(SESSIONS_DIR / session_name)
            client = TelegramClient(session_path, API_ID, API_HASH)
            await client.start()
            console.print(f"[bold green]✓ Logged in and saved session as '{session_name}.session'[/bold green]")
            session_files = [SESSIONS_DIR / f"{session_name}.session"]

        console.print(f"[cyan][*] Connecting {len(session_files)} Telegram session(s)...[/cyan]")

        for s_file in session_files:
            s_base = s_file.stem
            s_path = str(SESSIONS_DIR / s_base)
            client = TelegramClient(s_path, API_ID, API_HASH)

            try:
                await client.connect()
                if not await client.is_user_authorized():
                    console.print(f"[yellow][!] Session '{s_base}' is unauthorized or expired. Skipping.[/yellow]")
                    continue

                me = await client.get_me()
                user_name = me.first_name if me else s_base
                console.print(f"[green]✓ Connected session: [bold]{s_base}[/bold] ({user_name})[/green]")
                self.clients.append(client)

                # Ensure/create a dedicated dummy channel for safe channel-based checking
                channel = None
                async for dialog in client.iter_dialogs(limit=25):
                    if dialog.title == "TelegramHunter Checker":
                        channel = dialog.entity
                        break

                if not channel:
                    try:
                        res = await client(functions.channels.CreateChannelRequest(
                            title="TelegramHunter Checker",
                            about="Automated username availability checker",
                            broadcast=True
                        ))
                        channel = res.chats[0]
                    except Exception:
                        channel = None

                self.channels.append(channel)

            except Exception as e:
                console.print(f"[red][!] Error initializing session '{s_base}': {e}[/red]")

        if not self.clients:
            console.print("[bold red][!] No valid or authorized sessions available. Exiting.[/bold red]")
            return False

        console.print(f"[bold green]✓ Successfully activated {len(self.clients)} worker session(s)![/bold green]\n")
        return True

    def generate_wordlist(self) -> tuple[list[str], str]:
        console.print(Panel("""[bold cyan]Select Scan Mode:[/bold cyan]
 [bold green]1.[/bold green] 📖 Real English Dictionary Words - [bold yellow]4 Letters[/bold yellow]  (~4,000 real words)
 [bold green]2.[/bold green] 📖 Real English Dictionary Words - [bold yellow]5 Letters[/bold yellow]  (~12,000 real words)
 [bold green]3.[/bold green] 📖 Real English Dictionary Words - [bold yellow]6 Letters[/bold yellow]  (~25,000+ real words)
 [bold green]4.[/bold green] 🌟 Real English Dictionary Words - [bold yellow]4 to 6 Letters All Combined[/bold yellow] (+40,000+ words)
 [bold green]5.[/bold green] 🔤 Alphabet Combinations - [bold yellow]4 Characters (a-z)[/bold yellow] (456,976 combos)
 [bold green]6.[/bold green] 🔤 Alphabet Combinations - [bold yellow]5 Characters (a-z)[/bold yellow] (Selective range)
 [bold green]7.[/bold green] 🔢 Alphanumeric Combinations (Letters + Numbers, 4 chars)
 [bold green]8.[/bold green] 📂 Load Custom Wordlist from text file (wordlist.txt)
""", title="[bold white]Mode Selection[/bold white]", border_style="cyan"))

        choice = Prompt.ask("Enter your choice (1-8)", choices=["1", "2", "3", "4", "5", "6", "7", "8"], default="4")

        word_list = []
        mode_label = ""

        if choice in ["1", "2", "3", "4"]:
            if not words:
                console.print("[red][!] NLTK words corpus is unavailable. Falling back to alphanumeric mode.[/red]")
                choice = "5"
            else:
                raw_words = words.words()
                if choice == "1":
                    word_list = [w.lower() for w in raw_words if len(w) == 4 and w.isalpha()]
                    mode_label = "Real_Dictionary_4Char"
                elif choice == "2":
                    word_list = [w.lower() for w in raw_words if len(w) == 5 and w.isalpha()]
                    mode_label = "Real_Dictionary_5Char"
                elif choice == "3":
                    word_list = [w.lower() for w in raw_words if len(w) == 6 and w.isalpha()]
                    mode_label = "Real_Dictionary_6Char"
                elif choice == "4":
                    word_list = [w.lower() for w in raw_words if 4 <= len(w) <= 6 and w.isalpha()]
                    mode_label = "Real_Dictionary_4to6Char"

                # Deduplicate while preserving order
                word_list = list(dict.fromkeys(word_list))

        if choice == "5":
            chars = string.ascii_lowercase
            word_list = ["".join(p) for p in itertools.product(chars, repeat=4)]
            mode_label = "Alphabet_4Char"

        elif choice == "6":
            chars = string.ascii_lowercase
            console.print("[yellow][*] Generating 5-character combinations batch...[/yellow]")
            # Generate a targeted slice of 5-letter combos
            word_list = ["".join(p) for p in itertools.islice(itertools.product(chars, repeat=5), 50000)]
            mode_label = "Alphabet_5Char_50k"

        elif choice == "7":
            chars = string.ascii_lowercase + string.digits
            word_list = ["".join(p) for p in itertools.islice(itertools.product(chars, repeat=4), 50000)]
            mode_label = "Alphanumeric_4Char_50k"

        elif choice == "8":
            filename = Prompt.ask("Enter wordlist file path", default="wordlist.txt")
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                    word_list = [line.strip().lower() for line in f if line.strip() and 4 <= len(line.strip()) <= 32]
                word_list = list(dict.fromkeys(word_list))
                mode_label = f"CustomFile_{Path(filename).stem}"
            else:
                console.print(f"[red][!] File '{filename}' not found. Using 5-letter dictionary instead.[/red]")
                word_list = [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()] if words else ["apple"]
                mode_label = "Real_Dictionary_5Char"

        return word_list, mode_label

    async def check_username(self, client: TelegramClient, channel, username: str) -> str:
        """
        Returns:
            'AVAILABLE' -> Username is completely free to take!
            'TAKEN'     -> Username is already occupied or in use.
            'FLOOD'     -> Flood wait error encountered.
            'ERROR'     -> Other RPC / network error.
        """
        try:
            # First try direct account username check
            try:
                res = await client(functions.account.CheckUsernameRequest(username=username))
                if res:
                    return "AVAILABLE"
                else:
                    return "TAKEN"
            except errors.UsernameOccupiedError:
                return "TAKEN"
            except errors.UsernameInvalidError:
                return "TAKEN"

        except errors.FloodWaitError as e:
            return f"FLOOD_{e.seconds}"

        except Exception:
            # Fallback to channel check if available
            if channel:
                try:
                    await client(functions.channels.CheckUsernameRequest(channel=channel, username=username))
                    return "TAKEN"
                except errors.UsernameNotOccupiedError:
                    return "AVAILABLE"
                except errors.UsernameOccupiedError:
                    return "TAKEN"
                except errors.UsernameInvalidError:
                    return "TAKEN"
                except errors.FloodWaitError as e:
                    return f"FLOOD_{e.seconds}"
                except Exception:
                    pass

        return "TAKEN"

    async def start(self):
        console.clear()
        console.print(BANNER)

        # 1. Setup Sessions
        success = await self.setup_sessions()
        if not success:
            return

        # 2. Generate Wordlist
        self.wordlist, mode_label = self.generate_wordlist()
        total_words = len(self.wordlist)
        console.print(f"\n[bold green]✓ Loaded {total_words:,} targets for scanning![/bold green]")

        # 3. Check State for Resume
        state = load_state()
        start_index = 0
        if state.get("session_mode") == mode_label and state.get("last_index", 0) > 0:
            saved_idx = state["last_index"]
            if saved_idx < total_words:
                if Confirm.ask(f"Found previous saved progress at word {saved_idx:,}/{total_words:,}. Resume?"):
                    start_index = saved_idx

        # 4. Scanner Loop
        delay = float(Prompt.ask("Delay between requests per session in seconds (recommended 1.5 - 3.0)", default="2.0"))

        console.print(Panel(f"""
 [bold cyan]Scan Mode:[/bold cyan] {mode_label}
 [bold cyan]Total Targets:[/bold cyan] {total_words:,}
 [bold cyan]Start Index:[/bold cyan] {start_index:,}
 [bold cyan]Active Workers:[/bold cyan] {len(self.clients)}
 [bold cyan]Output File:[/bold cyan] {RESULTS_FILE}
""", title="[bold green]Starting Hunter[/bold green]", border_style="green"))

        console.print("[bold yellow]Press Ctrl+C at any time to pause and save progress.[/bold yellow]\n")

        self.start_time = time.time()
        num_workers = len(self.clients)

        try:
            for i in range(start_index, total_words):
                worker_idx = i % num_workers
                client = self.clients[worker_idx]
                channel = self.channels[worker_idx]
                word = self.wordlist[i]

                result = await self.check_username(client, channel, word)
                self.total_checked += 1

                elapsed = max(1, time.time() - self.start_time)
                speed = self.total_checked / elapsed

                if result == "AVAILABLE":
                    self.available_found += 1
                    save_found_username(word)
                    console.print(f"[bold green]🔥 [AVAILABLE FOUND] @{word:<15} | Index: {i:,}/{total_words:,} | Saved to file![/bold green]")
                elif result == "TAKEN":
                    self.taken_count += 1
                    status_line = f"[dim cyan][{i:,}/{total_words:,}][/dim cyan] [dim white]@{word:<14}[/dim white] -> [dim red]TAKEN[/dim red] | [dim yellow]{speed:.2f} req/s[/dim yellow]"
                    console.print(status_line)
                elif result.startswith("FLOOD_"):
                    wait_sec = int(result.split("_")[1])
                    console.print(f"[bold yellow]⚠️ FloodWait: Worker {worker_idx+1} sleeping for {wait_sec}s...[/bold yellow]")
                    await asyncio.sleep(min(wait_sec, 60))
                else:
                    self.errors_count += 1

                # Save checkpoint every 10 usernames
                if i % 10 == 0:
                    save_state(i, mode_label)

                await asyncio.sleep(delay)

            console.print(f"\n[bold green]🎉 Finished scanning all {total_words:,} words![/bold green]")

        except (KeyboardInterrupt, asyncio.CancelledError):
            save_state(i, mode_label)
            console.print(f"\n[bold yellow]⏸️ Scan safely paused at index {i:,}. Progress saved![/bold yellow]")

        finally:
            for c in self.clients:
                try:
                    await c.disconnect()
                except Exception:
                    pass

        # Final Summary
        console.print(Panel(f"""
 [bold green]Available Usernames Found:[/bold green] {self.available_found} (Saved in [bold]{RESULTS_FILE.name}[/bold])
 [bold cyan]Total Usernames Checked:[/bold cyan] {self.total_checked}
 [bold red]Taken Usernames:[/bold red] {self.taken_count}
 [bold yellow]Elapsed Time:[/bold yellow] {int(time.time() - self.start_time)} seconds
""", title="[bold white]Hunter Summary[/bold white]", border_style="cyan"))


if __name__ == "__main__":
    try:
        asyncio.run(TelegramHunter().start())
    except KeyboardInterrupt:
        print("\nExited.")
