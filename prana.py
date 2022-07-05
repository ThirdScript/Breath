from rich.progress import track
import time
import os


big_banner = """
 __   __   ___      ___      
|__) |__) |__   /\   |  |__| 
|__) |  \ |___ /~~\  |  |  | 
                                                        
"""

# BreathCycle Function Gets Breathing Times and
# creates progress bars for them
def BreathCycle(b_in: int, b_hold: int, b_out: int, b_hold_out: int, b_round: int):
    # Rounds Of Breathing Cycle
    for rnd_number in range(1, b_round+1):

        # Clearing Screen and Showing Round Number
        os.system('cls' if os.name == 'nt' else 'clear')
        print(F"\n\tRound: {rnd_number}")
        print("\t"+("#-"*30))

        # IN Breath
        for n in track(range(b_in* 100), description=F"Breath IN [{b_in} Sec]"):
            time.sleep(0.01)
            n = n+1

        # Hold Breath
        for n in track(range(b_hold * 100), description=F"HOLD [{b_hold} Sec]"):
            time.sleep(0.01)
            n = n+1

        # Out Breath
        for n in track(range(b_out * 100), description=F"Breath Out [{b_out} Sec]"):
            time.sleep(0.01)
            n = n+1

        # Out Hold Breath
        for n in track(range(b_hold_out * 100), description=F"Hold [{b_out} Sec]"):
            time.sleep(0.01)
            n = n+1
            

# Breathing Patterns
b_patterns = {"relax": (4, 7, 8, 0, 3),
              "calm": (4, 2, 4, 2, 3),
              "box": (5, 5, 5, 5, 3)}



# ShowMenu Function Shows The Menu :D
def ShowMenu():
    print(big_banner)
    print("""
    1. Relax        (4 - 7 - 8)
    2. Calm         (4 - 2 - 4)
    3. Box Breath   (5 - 5 - 5)

    4. * Custom *
    """)
    # User Choice IS A Global Variable
    global choice
    choice = int(input("Choose : "))

ShowMenu()
if choice == 1:
    BreathCycle(*b_patterns["relax"])
elif choice == 2:
    BreathCycle(*b_patterns["calm"])
elif choice == 3:
    BreathCycle(*b_patterns["box"])
else:
    print("Bad input")