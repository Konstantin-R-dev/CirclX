import math
import tkinter as tk
import keyboard
import pyautogui

menue_open = False
window = None


def open_menue():
  global menue_open, window
  if menue_open:
    return

  x, y = pyautogui.position()
  menue_open = True

  window = tk.Tk()
  window.overrideredirect(True)
  size = 220
  window.geometry(f"{size}x{size}+{x - size//2}+{y - size//2}")
  window.configure(bg="#222222")
  window.attributes("-topmost", True)

  canvas = tk.Canvas(
      window, width=size, height=size, bg="#222222", highlightthickness=0
  )
  canvas.pack(fill="both", expand=True)

  cx, cy = size // 2, size // 2
  radius = 70
  bubble_radius = 20

  close_circle = canvas.create_oval(
      cx - 18,
      cy - 18,
      cx + 18,
      cy + 18,
      fill="#ff4d4d",
      outline="white",
      width=2,
  )
  close_text = canvas.create_text(
      cx, cy, text="X", fill="white", font=("Arial", 10, "bold")
  )

  canvas.tag_bind(close_circle, "<Button-1>", lambda e: close_menue())
  canvas.tag_bind(close_text, "<Button-1>", lambda e: close_menue())

  actions = ["Copy", "Paste", "CMD", "Explorer", "Screen"]
  num_items = len(actions)

  for i, name in enumerate(actions):
    angle = (2 * math.pi / num_items) * i
    bx = cx + radius * math.cos(angle)
    by = cy + radius * math.sin(angle)

    canvas.create_oval(
        bx - bubble_radius,
        by - bubble_radius,
        bx + bubble_radius,
        by + bubble_radius,
        fill="#00adb5",
        outline="white",
        width=2,
    )
    canvas.create_text(bx, by, text=name, fill="white", font=("Arial", 8))

  window.mainloop()


def close_menue():
  global menu_open, window
  if window:
    window.destroy()
    window = None
  menue_open = False


def toggle_menue():
  if not menu_open:
    open_menue()
  else:
    close_menue()
