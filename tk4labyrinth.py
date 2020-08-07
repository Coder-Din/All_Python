from tkinter import *
from tkinter import messagebox
root = Tk()

canvas = Canvas(root, height = 430, width = 540)
canvas.pack()
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W            WWWWWWWWWWWWWWWWWWWWW",
    "W            WWWWWWWWWWWWWWW     W",
    "W             WWWWWWWWWWWWW   W  W",
    "W                WWWWWWWWWW   W  W",
    "W       WWWWWW    WWWWWWWWW   W  W",
    "W      WWWWWWWW   WWWWWWW    WWDDW",
    "W   W KWWWWWWW   WWWWWWWW    WW  W",
    "W   W    WWW    WWWWWWW    WWW   W",
    "W   WW                   WWWW   WW",
    "W   WWWWW   WWWWWWWW    WW     WWW",
    "W   WW  W    WWWWW    WW   WWWWWWW",
    "W   WW  WW           WWWW   WWWWWW",
    "WW   WW  WWWW    KWWWWWW   WWWWWWW",
    "WWW   WW    WWWWWWWWWWWWW    WWWWW",
    "WWWW   WWW        WWWWW    WWWWWWW",
    "WWWWW   WWW      WWWW    WWWWWWWWW",
    "WWWWWW   WWW    WWWW    WWWWWWWWWW",
    "WWWWWWW   WWWWWWWWW    WWWWW   WWW",
    "WWWWWWWW   WWWWWWW    WWWWW  W  WW",
    "WWWWWWWWW   WWWWWWW   WWWWW  W  WW",
    "WWWWWWWWW   WWWWWWWW   WWW  WW  WW",
    "WWWWWWWWW   WWWWWWWWW      WWW  WW",
    "WWWWWWWWW   WWWWWWWWWWWWWWWWWW  WW",
    "WWWWWW        WWWWWWWWWWWWWWW  WWW",
    "W               KWWWWWWWWWWWW  WWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEWWW",
]
exits = []
walls = []
doors = []
keys = []
keysclone = []
canvasdoors = []
canvaskeys = []
keycount = 3
x = 0
y = 0
def restart():
    global x, y, player, canvasdoors, canvaskeys
    for elem in level:
        for elem1 in elem:
            if elem1 == 'W':
                canvas.create_rectangle(x, y, x + 16, y + 16, fill = 'black')
                walls.append((x, y, x + 16, y + 16))
            if elem1 == 'E':
                canvas.create_rectangle(x, y, x + 16, y + 16, fill = 'yellow')
                exits.append((x, y, x + 16, y + 16))
            if elem1 == 'D':
                canvasdoors.append(canvas.create_rectangle(x, y, x + 16, y + 16, fill = 'brown'))
                doors.append((x, y, x + 16, y + 16))
            if elem1 == 'K':
                canvaskeys.append(canvas.create_rectangle(x, y, x + 16, y + 16, fill = 'green'))
                keys.append((x, y, x + 16, y + 16))
                keysclone.append((x, y, x + 16, y + 16))
            x += 16
        y += 16
        x = 0
    player = canvas.create_rectangle(17, 17, 31, 31, fill = 'red')
    def player_move(event):
        global player, keycount, doors
        key = event.keysym
        dx = dy = 0
        if key == 'Up':
            dy = -4
        if key == 'Down':
            dy = 4
        if key == 'Left':
            dx = -4
        if key == 'Right':
            dx = 4
        for wall in walls:
            if player in canvas.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                canvas.delete(player)
                player = canvas.create_rectangle(17, 17, 31, 31, fill='red')
                print(canvasdoors)
        for exit in exits:
            if player in canvas.find_overlapping(exit[0], exit[1], exit[2], exit[3]):
                messagebox.showinfo('Nice', 'You won!')
                canvas.delete(player)
                player = canvas.create_rectangle(17, 17, 31, 31, fill='red')
        for door in doors:
            if player in canvas.find_overlapping(door[0], door[1], door[2], door[3]):
                messagebox.showinfo('Sorry', 'Door locked')

        for id, key in enumerate(keys):
            if player in canvas.find_overlapping(key[0], key[1], key[2], key[3]):
                keycount -= 1
                print(keycount)
                canvas.create_rectangle(key[0], key[1], key[2], key[3], fill="black")

                del keys[id]
                if keycount == 0:
                    for id, canvasdoor in enumerate(canvasdoors):
                        canvas.delete(canvasdoor)
                        del doors[id]

        canvas.move(player, dx, dy)
    canvas.bind_all('<Key>', player_move)
restart()
root.mainloop()
