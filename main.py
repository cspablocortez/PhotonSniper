from pynput.mouse import Button, Controller
import os

print("Initializing Photon Sniper...")
mouseX = 800
mouseY = -600
mouse_dx = 1

mouse = Controller()

# mouse.position(mouseX, mouseY)


mouse.move(1, 0)

while True:
    os.system('clear') # Change this to 'cls' on Windows
    print('Pointer position: {0}'.format(mouse.position))
    
    