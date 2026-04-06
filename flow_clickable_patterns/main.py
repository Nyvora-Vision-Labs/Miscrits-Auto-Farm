import time, random, threading
from click_chest import click_chest
from click_attack import click_attack
from click_continue import click_continue
from check_loading_screen import check_loading_screen

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
        time.sleep(0.8)

        print("\n--- Step 2: Check Loading Screen ---")
        if check_loading_screen():
            print("✅ Loading screen appeared — chest click worked!")
            #TAKE SCREENSHOT
            #{cHECK FOR WOOLY}
            #(check for double)
            #Attack
            print("\n--- Step 3: Click Attack ---")
            time.sleep(3.5)
            click_attack()
            click_continue()
            break
        else:
            delay = random.uniform(20, 25)
            print(f"❌ Loading screen did not appear — retrying in {delay:.1f}s...")
            for _ in range(int(delay * 10)):
                if stop:
                    break
                time.sleep(0.1)