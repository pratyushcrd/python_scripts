# Python 3 circular spiral script

import pyautogui, time, math

# change the parameters below to generate awesome arts :)
radius = 200 # radius for spiral
quadrant = 1 # 1, 2, 3, 4; 4 by default;
min_radius = 10 # last size of radius; radius decreases in spiral;
decreasing_factor = 0.995 # radius decreasing factor; higher means more circular spiral;
angle_increment = 3 # less means more detailed thus slow;
pyautogui.PAUSE = 0.01 # determines speed of task

def location(quadrant, radius, posX, posY):
    radian = math.radians(angle)
    if quadrant == 1:
        locX = math.sin(radian) * radius +  posX
        locY = math.cos(radian) * radius + posY
    elif quadrant == 2:
        locX = math.sin(radian) * -radius +  posX
        locY = math.cos(radian) * radius + posY
    elif quadrant == 2:
        locX = math.sin(radian) * -radius +  posX
        locY = math.cos(radian) * -radius + posY
    else:
        locX = math.sin(radian) * radius +  posX
        locY = math.cos(radian) * -radius + posY
    return (locX, locY)

time.sleep(1.5)
posX, posY = pyautogui.position()
pyautogui.click()
angle = 0


pyautogui.moveTo(location(quadrant, radius, posX, posY))
pyautogui.mouseDown(button='left')

while radius > min_radius:
    pyautogui.moveTo(location(quadrant, radius, posX, posY))
    angle += angle_increment
    radius *= decreasing_factor
    if angle > 359:
        angle = 0

pyautogui.mouseUp(button='left')
