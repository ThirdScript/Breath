from rich.progress import track
import time

def BreathCycle(b_in: int, b_hold: int, b_out: int, b_hold_out: int, b_round: int):
    for rnd_number in range(1, b_round+1):
        print(F"\n\tRound: {rnd_number}")
        print("\t"+("#-"*30))

        for n in track(range(b_in* 100), description=F"Breath IN [{b_in} Sec]"):
            time.sleep(0.01)
            n = n+1

        for n in track(range(b_hold * 100 - 100), description=F"HOLD [{b_hold} Sec]"):
            time.sleep(0.01)
            n = n+1

        for n in track(range(b_out * 100 - 100), description=F"Breath Out [{b_out} Sec]"):
            time.sleep(0.01)
            n = n+1

        for n in track(range((b_hold_out+1) * 100 - 100), description=F"Hold [{b_out} Sec]"):
            time.sleep(0.01)
            n = n+1
            

basic_breath = (4, 7, 8, 1, 2)

BreathCycle(*basic_breath)