from rich.progress import track
import time


for rnd in range(3):
    for n in track(range(400), description="Breath IN [4 Sec]"):
        time.sleep(0.01)
        n = n+1

    for n in track(range(700), description="HOLD [7 Sec]"):
        time.sleep(0.01)
        n = n+1

    for n in track(range(800), description="Breath Out [8 Sec]"):
        time.sleep(0.01)
        n = n+1
        