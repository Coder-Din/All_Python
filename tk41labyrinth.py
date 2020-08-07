from tkinter import *

window = Tk()
c = Canvas(window, height=304, width=480)
c.pack()

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                 WWWWWW    KW",
    "WWWWWWWWWWW  WWW  WWWWWW  W  W",
    "WWWWWWW      WWW  WWWWWW  W  W",
    "WWWWWWW  WWWWWWW          W  W",
    "W        WWW      WWWWWW  W  W",
    "W  WWWW  WWW  WWWWWWWW    W  W",
    "W  WWWW  WWW       WWW  WWW  W",
    "W     W    WWWWWW  WWW  W    W",
    "WWWW  WWW  WWWWWW    W  W  WWW",
    "WW            WWWWW  W  W    W",
    "WW  WWWWWWW   WWW       WWW  W",
    "WW    W                KWWW  W",
    "WWWW  W       WWWWWWWWWWW    W",
    "WW    WWWWWWWWWWWWWWWWWWW    W",
    "WW    W                     KW",
    "WWDW  W  WWWWWWWWWW  WWWW  WWW",
    "WW  WWW        KWWW     W  WWW",
    "WWEEWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
exit = []
walls = []
keys = []
x = 0
y = 0
for row in level:
    for i in row:
        if i == "W":
            c.create_rectangle(x, y, x + 16, y + 16, fill="black")
            walls.append((x, y, x + 16, y + 16))
        if i == "E":
            c.create_rectangle(x, y, x + 16, y + 16, fill="Orange")
            exit.append((x, y, x + 16, y + 16))
        if i == "K":
            c.create_rectangle(x, y, x + 16, y + 16, fill="Yellow")
            keys.append((x, y, x + 16, y + 16))
        if i == "D":
            door = c.create_rectangle(x, y, x + 16, y + 16, fill="Blue")
            door_coor = (x, y, x + 16, y + 16)
        x += 16
    y += 16
    x = 0
Player = c.create_rectangle(17, 17, 31, 31, fill="Green")


def Player_control(event):
    key = event.keysym
    x = y = 0
    if key == "Up":
        y = -4
    if key == "Down":
        y = 4
    elif key == "Left":
        x = -4
    elif key == "Right":
        x = 4
    c.move(Player, x, y)
    for wall in walls:
        if Player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
            c.move(Player, -x, -y)
    for e in exit:
        if Player in c.find_overlapping(e[0], e[1], e[2], e[3]):
            c.create_text(200, 200, text="You Won The Game", fill="red", font="Verdana 20")
    for k in keys:
        if Player in c.find_overlapping(k[0], k[1], k[2], k[3]):
            c.create_rectangle(k[0], k[1], k[2], k[3], fill="black")
    if Player in c.find_overlapping(door_coor[0], door_coor[1], door_coor[2], door_coor[3]):
        if len(keys) == 0:
            c.create_rectangle(door_coor[0], door_coor[1], door_coor[2], door_coor[3], fill="black")
            c.move(Player, x, y)
        else:
            c.move(Player, -x, -y)


c.bind_all('<Key>', Player_control)
window.mainloop()