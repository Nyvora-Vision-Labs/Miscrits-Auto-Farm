import time, random, threading
from click_chest import click_chest
from click_attack import click_attack
from click_continue import click_continue
from check_loading_screen import check_loading_screen
from detect_miscrits_logo import is_wooly
#TODO every five minute check to see if miscrit needs to be leveled up.

stop = False

def listen_for_quit():
    global stop
    while not stop:
        if input().strip().lower() == "q":
            print("🛑 Stopping...")
            stop = True

if __name__ == "__main__":
    print("Starting in 1 second — switch to your game window! (type 'q' to stop)")
    time.sleep(1)

    threading.Thread(target=listen_for_quit, daemon=True).start()

    while not stop:
        print("\n--- Step 1: Click Chest ---")
        click_chest()

        print("\n--- Step 2: Check Loading Screen ---")
        if check_loading_screen():
            print("✅ Loading screen appeared — chest click worked!")
            #First check for doubles (TODO)

            is_it_wooly = is_wooly()
            if is_it_wooly:
                print("✅ It's Wooly! Stopping.")
                stop = True
                break               #Write the capture code here! (TODO)
            else:
                print("❌ Not Wooly.")
                print("\n--- Step 3: Attack & Continue ---")
                time.sleep(random.uniform(4, 4.5))
                click_attack()
                time.sleep(random.uniform(7, 8))
                click_continue()

                # ✅ Wait 13s after a completed battle before re-clicking chest
                print("⏳ Waiting 13 seconds before next chest click...")
                for _ in range(130):
                    if stop:
                        break
                    time.sleep(0.1)
                

        else:
            # Chest click didn't register — wait then retry
            #Pickup Gold and Relics (TODO)
            delay = random.uniform(20, 25)
            print(f"❌ Loading screen did not appear — retrying in {delay:.1f}s...")
            for _ in range(int(delay * 10)):
                if stop:
                    break
                time.sleep(0.1)
            # Loop naturally back to Step 1 (click_chest) ✅