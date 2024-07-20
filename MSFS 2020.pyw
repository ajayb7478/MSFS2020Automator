import tkinter as tk
import subprocess
import os
from screeninfo import get_monitors
import platform
import pyautogui
import time
import sys
import webbrowser
from pathlib import Path
import pygetwindow as gw
import win32gui
import win32con
import psutil

# Check if running as a bundled executable
if getattr(sys, 'frozen', False):
    # If so, determine path to bundled resource files
    bundle_dir = sys._MEIPASS
else:
    # Else, use current directory
    bundle_dir = Path(__file__).parent

# Path to the folder containing your .exe and .bat files
folder_path = 'F:\\MSFS 2020\\Mods\\Apps and stuff'  # Change this to your folder path

# Full paths to the executable and batch files
file1 = os.path.join(folder_path, 'FsPanelServer.exe')
file2 = os.path.join(folder_path, 'MSFS_MCA_v1-9-1.exe')
file3 = os.path.join(folder_path, 'MSFSPopoutPanelManager.exe')
file4 = os.path.join("F:\\MSFS 2020\\Community\\fsltl-traffic-injector", 'fsltl-trafficinjector.exe')
folder_to_open = 'F:\\MSFS 2020'  # Change this to your folder path
steam_url = 'steam://rungameid/1250410'


# Function to open file1
def open_file1():
    subprocess.Popen([file1])

# Function to open file2 in a new terminal window
def open_file2():
    subprocess.Popen(['start', 'cmd.exe', '/k', file2], shell=True)


def open_file3():
    subprocess.Popen([file3])

# Function to open file4 in a new terminal window
def open_file4():
    subprocess.Popen(['start', 'cmd.exe', '/k', file4], shell=True)
    

# Function to open a folder in the file explorer
def open_folder():
    if os.name == 'nt':  # Windows
        os.startfile(folder_to_open)
    elif os.name == 'posix':  # macOS and Linux
        subprocess.Popen(['open', folder_to_open])  # For macOS
        # subprocess.Popen(['xdg-open', folder_to_open])  # For Linux
        
# Function to move the mouse to a specific position and perform a left-click
def move_and_click(x, y):
    pyautogui.moveTo(x, y)  # Move the mouse to the specified coordinates
    pyautogui.click()       # Perform a left-click

# Coordinates to move the mouse to
x_coordinate = 100
y_coordinate = 200

# Call the function to move the mouse and click
move_and_click(x_coordinate, y_coordinate)

def is_steam_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'steam.exe':
            return True
    return False
        
def open_steam_game():
    if is_steam_running():
        webbrowser.open(steam_url)
    else:
        webbrowser.open(steam_url)
        steam_window = None
        while steam_window is None:
            time.sleep(1)  # Check every second
            windows = gw.getWindowsWithTitle('Sign in to steam')
            if windows:
                steam_window = windows[0]

        # Bring the Steam window to the foreground
        win32gui.SetForegroundWindow(steam_window._hWnd)
        steam_window.activate()

        # Get the coordinates for the account selection button
        # You might need to run the script to get the coordinates first
        account_selection_x = 860  # Replace with actual x-coordinate
        account_selection_y = 527  # Replace with actual y-coordinate
        
        # Move the mouse to the account selection button and click
        time.sleep(0.5)  # Small delay to ensure the window is focused
        pyautogui.moveTo(account_selection_x, account_selection_y)
        pyautogui.click()
        time.sleep(0.5)
        close_app("Steam", 1570, 160)
    

def close_app(name_of_app, x, y):
    app_window = None
    while app_window is None:
        time.sleep(0.1)  # Check every second
        windows = gw.getWindowsWithTitle(name_of_app)
        if windows:
            app_window = windows[0]

    # Bring the Steam window to the foreground
    win32gui.SetForegroundWindow(app_window._hWnd)
    app_window.activate()
    
    
    # Move the mouse to the account selection button and click
    
    time.sleep(4)  # Small delay to ensure the window is focused
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    

# Create the main window
root = tk.Tk()
root.title("MSFS Launchers")

# Set window size
window_width = 300
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Get screen information
monitors = get_monitors()
if len(monitors) > 1:
    # Get the second monitor's screen
    second_monitor = monitors[1]
    monitor_width = second_monitor.width
    monitor_height = second_monitor.height
    monitor_x = second_monitor.x
    monitor_y = second_monitor.y
    # Position the window at the bottom right of the second monitor
    position_right = monitor_x + monitor_width - window_width
    position_bottom = monitor_y + monitor_height - window_height
else:
    # Default to the primary monitor if only one monitor is detected
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = screen_width - window_width
    position_bottom = screen_height - window_height

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_bottom}")

# Create buttons and assign functions
btn_file1 = tk.Button(root, text="FsPanel", command=open_file1)
btn_file2 = tk.Button(root, text="Msfs Companion", command=open_file2)
btn_file3 = tk.Button(root, text="Msfs Pop out manager", command=open_file3)
btn_file4 = tk.Button(root, text="FSLTL Traffic", command=open_file4)
btn_open_folder = tk.Button(root, text="Open Folder", command=open_folder)
btn_steam_game = tk.Button(root, text="Microsoft Flight Simulator", command=open_steam_game)

# Pack buttons
btn_file1.pack(pady=5)
btn_file2.pack(pady=5)
btn_file3.pack(pady=5)
btn_file4.pack(pady=5)
btn_open_folder.pack(pady=5)
btn_steam_game.pack(pady=10)

# Run the Tkinter event loop
open_file4()
time.sleep(0.5)  # Wait for the application to open
pyautogui.press('enter')
time.sleep(0.5)
open_steam_game()
#time.sleep(0.5)
#close_app("Special Offers", 1186, 896)
root.mainloop()

