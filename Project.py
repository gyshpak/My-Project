from tkinter import *
root = Tk()
HEIGHT = 800
WIDTH = 800
x1 = 0
y1 = 0
x2 = 0
y2 = 0
coordinat_list =[]
glob_color = 'black'
# nom_click = 0

# def new_position(event):
#     global x1, y1, x2, y2
#     print(x1, x2)
#     if x1 == 0:
#         x1 = event.x
#         y1 = event.y
#     else:
#         x2 = event.x
#         y2 = event.y
#     print(x1, x2)

# canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg="#87cefa", bd=5)
frame.place(relx=0.5, rely=0.01, relwidth=0.9, relheight=0.05, anchor='n')

button = Button(frame, 
                   text="Oval", 
                   bg="gray", fg="white", 
                   font=('Courier', 12), 
                #    command=lambda: get_weather(entry_field.get()))
                   command=lambda: my_oval())
button.place(relx=0.1, rely=0, relwidth=0.1, relheight=1)

button = Button(frame, 
                   text="red", 
                   bg="red", fg="white", 
                   font=('Courier', 12), 
                #    command=lambda: get_weather(entry_field.get()))
                   command=lambda: take_color('red'))
button.place(relx=0.2, rely=0, relwidth=0.1, relheight=1)
button = Button(frame, 
                   text="green", 
                   bg="green", fg="white", 
                   font=('Courier', 12), 
                #    command=lambda: get_weather(entry_field.get()))
                   command=lambda: take_color('green'))
button.place(relx=0.3, rely=0, relwidth=0.1, relheight=1)
button = Button(frame, 
                   text="blue", 
                   bg="blue", fg="white", 
                   font=('Courier', 12), 
                #    command=lambda: get_weather(entry_field.get()))
                   command=lambda: take_color('blue'))
button.place(relx=0.4, rely=0, relwidth=0.1, relheight=1)

def take_color(color):
    global glob_color
    glob_color = color

def new_coord1(event):
    # global x1, y1, x2, y2, nom_click
    global x1, y1, x2, y2
    x1 = event.x
    x2 = x1
    y1 = event.y
    y2 = y1
    # nom_click = 1
def new_coord2(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    # nom_click = 0
    # canvas.create_oval(x1,y1,x2,y2,fill = 'RED', width=0)
    create_oval2(x1, y1, x2, y2)
    x1, y1, x2, y2 = 0, 0, 0, 0


def cre_ov(event):
    global x1, y1, x2, y2
    # canvas.create_oval(x1,y1,x2,y2,fill = 'white', width=0)
    canvas.create_oval(x1,y1,x2,y2,outline = 'white', width=1)
    x2 = event.x
    y2 = event.y
    # canvas.create_oval(x1,y1,x2,y2,fill = 'green', width=0)
    canvas.create_oval(x1,y1,x2,y2, width=1)

def create_oval2(x1, y1, x2, y2):
    # list1 = x1, 
    coordinat_list.append([x1, y1, x2, y2, glob_color])
    for i in coordinat_list:

        # canvas.create_oval(i, fill = 'blue', width=0)
        # canvas.create_oval(i, outline = glob_color, width=2)
        canvas.create_oval(i[0], i[1], i[2], i[3], outline = i[4], width=2)

# print(x1, x2)

# canvas.bind('<Button-1>',new_position)
def my_oval():
    canvas.bind('<Button-1>', new_coord1)
    canvas.bind('<B1-Motion>',cre_ov)
    canvas.bind('<ButtonRelease-1>', new_coord2)

# canvas.bind('<B-1>', new_coord2)

# if x1 != 0 and x2 !=0:
    # canvas.create_oval(x1,y1,x2,y2,fill = 'RED', width=0)

# canvas.create_oval(x1,y1,x2,y2,fill = 'red', width=0)

# print(x1, x2)


root.mainloop()