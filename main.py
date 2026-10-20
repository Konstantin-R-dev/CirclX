#============================
# CIRCLX - MAIN ENTRY POINT
#============================

#Starting hotkey.py File
import keyboard
from core.hotkey import toggle_menu

keyboard.add_hotkey("ctrl+alt+m", toggle_menu)
keyboard.wait()
