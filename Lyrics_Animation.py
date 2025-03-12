import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(f"\033[97m{char}\033[0m")  # White text
            sys.stdout.flush()
            time.sleep(delay)
        print()
        time.sleep(1)

def animate_heart_delay(text, delay=0.02):  # Faster appearance
    with lock:
        for char in text:
            sys.stdout.write(f"\033[94m{char}\033[0m")  # Blue text for heart
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def animate_heart():
    heart = [
        "\n",
        "        ******         ******        ",
        "      **********     **********      ",
        "    *************   *************    ",
        "   ******************************   ",
        "   ******************************   ",
        "    ****************************    ",
        "      ************************      ",
        "        ********************        ",
        "          ****************          ",
        "            ************            ",
        "              ********              ",
        "                ****                ",
        "                 **                 "
    ]

    time.sleep(20)  # Ensuring the heart appears after the lyrics
    for line in heart:
        animate_heart_delay(line, 0.02)  # Blue heart color

def sing_song():
    lyrics = [
        ("Your morning eyes, I could stare like watching stars", 0.1),
        ("I could walk you by, and I'll tell without a thought", 0.1),
        ("You'd be mine, would you mind if I took your hand tonight?", 0.1),
        ("Know you're all that I want this life", 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 15.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    heart_thread = Thread(target=animate_heart)  # Adding heart animation at the end
    threads.append(heart_thread)
    heart_thread.start()

    for thread in threads:
        thread.join()

sing_song()