import keyboard
import pyautogui
import time

from PIL import ImageGrab


def take_screenshot():
    #im = ImageGrab.grab(bbox=[640, 70, 1280, 1080])  # left , top , right, bottom
    im = ImageGrab.grab()
    return im

def print_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse Position - X: {x}, Y: {y}")
    except KeyboardInterrupt:
        print("\nMouse position printing terminated by user.")



coord = [(709, 815), (876, 815), (1037, 815), (1208, 815)]
pyautogui.PAUSE = 0

def click(x,y):
    pyautogui.click(x, y)
    #time.sleep(0.1)

def start_game():
    screenshot = take_screenshot()
    color = screenshot.getpixel((coord[0][0], 750))
    if color == (54, 159, 198):
        print("COORD 1:", color)
        click(coord[0][0], 750)
    color = screenshot.getpixel((coord[1][0], 750))
    if color == (54, 159, 198):
        print("COORD 2:", color)
        click(coord[1][0], 750)
    color = screenshot.getpixel((coord[2][0], 750))
    if color == (54, 159, 198):
        print("COORD 3:", color)
        click(coord[2][0], 750)
    color = screenshot.getpixel((coord[3][0], 750))
    if color == (54, 159, 198):
        print("COORD 4:", color)
        click(coord[3][0], 750)
    print("Game Started!!!")

def run_autoclicker():
    print("Autoclicker Ready!!!")
    autoclick = True
    while autoclick:
        if keyboard.is_pressed('num lock'):
            print("Autoclicker Off!!!")
            autoclick = False
            exit()
        screenshot = take_screenshot()
        color = screenshot.getpixel((coord[0][0], coord[0][1]))
        if color[0] < 20:
            print("COORD 1:", color)
            click(coord[0][0], coord[0][1])
        color = screenshot.getpixel((coord[1][0], coord[1][1]))
        if color[0] < 20:
            print("COORD 2:", color)
            click(coord[1][0], coord[1][1])
        color = screenshot.getpixel((coord[2][0], coord[2][1]))
        if color[0] < 20:
            print("COORD 3:", color)
            click(coord[2][0], coord[2][1])
        color = screenshot.getpixel((coord[3][0], coord[3][1]))
        if color[0] < 20:
            print("COORD 4:", color)
            click(coord[3][0], coord[3][1])



def find_max_value_and_index(arr):
    if not arr:
        print("Array is empty.")
        return None, None

    max_value = max(arr)
    max_index = arr.index(max_value)

    return max_index, max_value

def run_autoclicker_v2():
    print("Autoclicker Ready!!!")
    autoclick = True
    while autoclick:
        if keyboard.is_pressed('num lock'):
            print("Autoclicker Off!!!")
            autoclick = False
            exit()
        screenshot = take_screenshot()
        for y in range(screenshot.height - 1, 99, -1):
            ready = False
            current_tile = [0, 0, 0, 0]
            color = screenshot.getpixel((coord[0][0], y))
            if color[0] < 20:
                print("COORD 1:", color)
                current_tile[0] = y
                ready = True
            color = screenshot.getpixel((coord[1][0], y))
            if color[0] < 20:
                print("COORD 2:", color)
                current_tile[1] = y
                ready = True
            color = screenshot.getpixel((coord[2][0], y))
            if color[0] < 20:
                print("COORD 3:", color)
                current_tile[2] = y
                ready = True
            color = screenshot.getpixel((coord[3][0], y))
            if color[0] < 20:
                print("COORD 4:", color)
                current_tile[3] = y
                ready = True
            x, y = find_max_value_and_index(current_tile)
            if ready:
                click(coord[x][0], y)
                #time.sleep(0.01)
                break
start_game()
run_autoclicker_v2()

#print_mouse_position()