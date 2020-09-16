import tkinter as tk

root = tk.Tk()
# root.geometry('500x500')

# root2 = tk.Tk()
# c = Canvas(root, height=500, width=500)

# w, h = 500, 500
# x, y = w//2, h//2

canvas = tk.Canvas(root)
canvas.grid()
r1 = canvas.create_rectangle(0,0,50,50)

def keypress(event):
    x, y = 0, 0
    if event.char == "w": y = -45
    if event.char == "a": x = -45
    if event.char == "s": y = 45
    if event.char == "d": x = 45
    canvas.move(r1, x, y)

def room1Create():
    for i in range(15):
        for j in range(15):
            # color walls
            # change width to 5 and height to 2 for smaller squares
            if i == 1 and j == 4:
                tk.Label(root, width="7", height="3", bg="red", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 0 and j == 1:
                tk.Label(root, width="7", height="3", bg="pink", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 0 and j == 14:
                tk.Label(root, width="7", height="3", bg="green4", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 8 and j == 14:
                tk.Label(root, width="7", height="3", bg="yellow", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 13 and j == 14:
                tk.Label(root, width="7", height="3", bg="yellow", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 14 and j == 0:
                tk.Label(root, width="7", height="3", bg="yellow", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 7 and j == 7:
                tk.Label(root, width="7", height="3", bg="peachpuff", borderwidth="1", relief="solid").grid(row=i, column=j)
            # gray walls
            elif i == 3 and j == 4:
                for j in range(5):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 7 and j == 6:
                for j in range(7):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 3 and j == 7:
                for i in range(4):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 7 and j == 9:
                for i in range(2,8):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 10 and j == 8:
                for i in range(6,11):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 2 and j == 14:
                for j in range(12,15):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 7 and j == 14:
                for j in range(11,15):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 5 and j == 11:
                for j in range(10,12):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 6 and j == 7:
                for j in range(6,8):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 12 and j == 0:
                for j in range(0,2):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 12 and j == 3:
                for j in range(2,4):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 14 and j == 3:
                for i in range(13,15):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 8 and j == 11:
                tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 12 and j == 11:
                for i in range(10,13):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 12 and j == 14:
                for j in range(12,15):
                    tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 13 and j == 12:
                tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 8 and j == 6:
                tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 0 and j == 4:
                tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            elif i == 2 and j == 4:
                tk.Label(root, width="7", height="3", bg="gray", borderwidth="1", relief="solid").grid(row=i, column=j)
            # movable space
            else:
                tk.Label(root, width="7", height="3", bg="light gray", borderwidth="1", relief="solid").grid(row=i, column=j)

room1Create()

root.bind("<Key>", keypress)
root.mainloop()

# walls = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#          [0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 0],
#          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# def drawWallsArray():
#     for y in range(len(walls)):
#         for x in range(len(walls[y])):
#             if walls[y][x] == 1:
#                 stroke(64, 64, 64)
#                 fill(128, 128, 128)
#                 rect(side * x, side * y, side, side)
#             if walls[y][x] == 2: #it's a chip
#                 stroke(230, 230, 230)
#                 strokeWeight(2)
#                 fill(100,100,100)
#                 y1 = (y * side) + 10
#                 x1 = (x * side) + 3
#                 rect(x1, y1, 30, 16)
#                 strokeWeight(1)