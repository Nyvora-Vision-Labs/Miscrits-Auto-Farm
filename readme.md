# Miscrits Auto Farm
**By Nyvora Vision Labs**

An automated Wooly XP farming bot for Miscrits. Captures Wooly and defeats all other crits. Requires **Light Zaptor maxed out** as your attacker with relics equipped.

All the scripts inside the **flow_clickable_patterns** folder helps automate things. Run main.py to get started. You might need to fix coordinates as per your device. Secondary Monitor is preferred as we are still testing this.

---

## Setup

Stand at the **bottom-right of the chest**, or play one manual battle first and run the script after killing the first miscrit.

![Where to stand](Where_to_stand.png)

> **Note:** If you do not have the level-up boost, change the retry delay in `check_loading_screen.py` from 24 seconds to 30 seconds.

---

## How It Works

1. **Click the chest** — starts a battle attempt
2. **Detect loading screen** — confirms battle started; if not, waits and retries
3. **Detect Wooly** — checks if the enemy is Wooly using image matching
   - If **Wooly**: stops (capture logic coming soon)
   - If **not Wooly**: attacks and continues, then repeats
4. **Attack & Continue** — defeats the miscrit and loops back to step 1

---

## File Reference

| File | Description |
|------|-------------|
| `click_chest.py` | Clicks the initial chest to start a battle |
| `check_loading_screen.py` | Detects the loading screen; no loading = battle didn't start, waits before retry |
| `detect_miscrits_logo.py` | Detects Wooly via image matching; triggers attack/continue if not Wooly |
| `click_attack.py` | Attacks the enemy miscrit |
| `click_continue.py` | Clicks Continue after battle ends and restarts the loop |
| `utils.py` | Shared utilities: human-like mouse movement, screenshotting, image matching |
| `test.py` | Helper to get coordinates while the game is running |
| `main.py` | Entry point — runs the full farming loop |

### Data / Images

| Path | Description |
|------|-------------|
| `images/miscrits/` | Reference images of miscrits (portrait only) |
| `images/miscrits-in-game/` | Full detail in-game images of miscrits |
| `images/` | Template images used for screen detection |

> `get_coordinates/` is legacy code and no longer used.

---

## TODO

| Feature | Notes |
|---------|-------|
| `click_capture.py` | Use weak attacks to capture Wooly — **(Hard)** |
| `detect_double.py` | Detect double battles — changes the entire flow **(Hard)** |
| `level_up_crit.py` | Every ~5 minutes, trigger a level-up event then resume farming (no plat train) |
| `collect_loot.py` | When a battle fails, collect gold or relic reward |

---

## 🤝 Contributing

Contributions are welcome! Ideas for improvement:

- Complete the TODO seciton.
- Improve image matching accuracy

Feel free to open an issue or submit a pull request.

---

## 🏢 Built By

**Nyvora Vision Labs**

---

## 📄 License

This project is unofficial and fan-made. Miscrits is a property of Broken Bulb Studios. All game assets belong to their respective owners.