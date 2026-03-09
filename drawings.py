import pyautogui as pygui
from time import sleep

screenWidth, screenHeight = pygui.size() #Get the size of the monitor
x = screenWidth / 2
y = screenHeight / 2

print("Draws: \n1- Square \n2- Spiral square \n3- Circle \n4- Spiral circle")
i = input("Drawing to be made: ")

sleep(5)
pygui.moveTo(x, y)
if i == "1": #Square
    pygui.moveTo(x + 150, y + 150, 0.5)
    pygui.dragTo(x + 150, y - 150, 1) #Up
    pygui.dragTo(x - 150, y - 150, 1) #Left
    pygui.dragTo(x - 150, y + 150, 1) #Down
    pygui.dragTo(x + 150, y + 150, 1) #Right

elif i == "2": #Spiral square
    distance = 10
    for i in range(12):
        pygui.drag(distance, 0) #Right
        distance += 10
        pygui.drag(0, -distance) #Up
        pygui.drag(-distance, 0) #Left
        distance += 10
        pygui.drag(0, distance) #Down

elif i == "3": #Circle
    pass

elif i == "4": #Spiral circle
    pass

else:
    print("Invalid value")