import pyautogui
import time

print("Move the mouse to the desired position and press Ctrl+C to exit.")

try:
    while True:
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Print the coordinates
        print(f"Mouse position: ({x}, {y})", end="\r")
        # Wait for a short period to avoid flooding the console
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram terminated.")
