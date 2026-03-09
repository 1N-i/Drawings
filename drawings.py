import pyautogui as pygui
from time import sleep

screenWidth, screenHeight = pygui.size() #Get the size of the monitor

print("Draws: \n1- Square \n2- Spiral square \n3- Circle \n4- Spiral circle")
i = input("Drawing to be made: ")

sleep(5)
pygui.moveTo(screenWidth / 2, screenHeight / 2)
if i == "1": #Square
    distance = 150
    pygui.move(distance, distance, 0.5)
    pygui.drag(0, -distance, 1) #Up
    pygui.drag(-distance, 0, 1) #Left
    pygui.drag(0, distance, 1) #Down
    pygui.drag(distance, 0, 1) #Right

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
    #X^2 + Y^2 - r^2 = 0
    #X^2 + Y^2 - 22500 = 0
    pass

elif i == "4": #Spiral circle
    pass

else:
    print("Invalid value")