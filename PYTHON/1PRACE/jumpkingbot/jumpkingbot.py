import pyautogui
import time
import random


# Set the size of the game window
window_width, window_height = 1920, 1080

# Set the position of the jump button
jump_button_x, jump_button_y = window_width // 2, window_height - 50

# Set the duration of the jump
jump_duration = 0.2

# Set the time between jumps
jump_interval = 0.5

# Set the maximum number of jumps
max_jumps = 100

# Set the counter for the number of jumps
jump_count = 0

# Set the flag to indicate if the player is jumping
jumping = False

# Set the flag to indicate if the game is running
running = True

# Set the flag to indicate if the game is paused
paused = False

# Set the key to pause the game
pause_key = 'p'

while running:
    # Check if the game is paused
    if not paused:
        # Check if the player is jumping
        if jumping:
            # Decrement the jump counter
            jump_count -= 1
            
            # Check if the jump has finished
            if jump_count == 0:
                # Set the flag to indicate that the player is not jumping
                jumping = False
        else:
            # Check if the maximum number of jumps has been reached
            if jump_count == max_jumps:
                # Set the flag to indicate that the game is running
                running = False
                break
                
            # Press the jump button
            pyautogui.click(jump_button_x, jump_button_y)
            
            # Set the flag to indicate that the player is jumping
            jumping = True
            
            # Set the jump counter
            jump_count = jump_duration * 60
    
    # Check for a pause key press
    if pyautogui.keyDown(pause_key):
        # Toggle the pause flag
        paused = not paused
        
    # Wait for the next frame
    time.sleep(1.0 / 60)
