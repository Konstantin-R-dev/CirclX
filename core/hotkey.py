import keyboard

menü_offen = False

def umschalten():
    global menü_offen
    if menü_offen == False:
        print("Radialmenü  geöffnet!")
        menü_offen = True
    else:
        print("Radiamenü geschlossen!")
        menü_offen = False

    keyboard.add_hotkey("ctrl+alt+m", umschalten)
    keyboard.wait()
