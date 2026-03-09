import pyautogui as pygui
from time import sleep

screenWidth, screenHeight = pygui.size() #Get the size of the monitor

print("Draws: \n1- Square \n2- Spiral square \n3- Circle \n4- Spiral circle")
i = input("Drawing to be made: ")

sleep(5)
center_x, center_y = screenWidth / 2, screenHeight / 2

if i == "1": #Square
    distance = 150
    pygui.moveTo(center_x + (distance/2), center_y + (distance/2), 0.5)
    pygui.drag(0, -distance, 1) #Up
    pygui.drag(-distance, 0, 1) #Left
    pygui.drag(0, distance, 1) #Down
    pygui.drag(distance, 0, 1) #Right

elif i == "2": #Spiral square
    distance = 10
    pygui.moveTo(center_x + (distance/2), center_y + (distance/2), 0.5)
    for i in range(15):
        pygui.drag(0, distance) #Down
        pygui.drag(distance, 0) #Right
        distance += 10
        pygui.drag(0, -distance) #Up
        pygui.drag(-distance, 0) #Left
        distance += 10

elif i == "3": #Circle
    import math #x^2 + y^2 - r^2 = 0
    radius = 150
    pygui.moveTo(center_x + radius, center_y)
    for i in range(0, 361, 5):
        angulo_rad = math.radians(i)
        x = center_x + radius * math.cos(angulo_rad)
        y = center_y + radius * math.sin(angulo_rad)
        pygui.dragTo(x, y)

elif i == "4": #Spiral circle
    import math
    radius = 5
    pygui.moveTo(center_x + radius, center_y)
    for i in range(8):
        for j in range(0, 361, 20):
            angulo_rad = math.radians(j)
            x = center_x + radius * math.cos(angulo_rad)
            y = center_y + radius * math.sin(angulo_rad)
            pygui.dragTo(x, y)
            radius += 0.75

else:
    print("Invalid value")