import tkinter as tk

startx, starty = 0, 0
endx, endy = 0, 0


# functions
def get_press(event):
    global startx, starty
    startx = event.x
    starty = event.y


def get_release(event):
    global endx, endy
    endx = event.x
    endy = event.y
    canvas.create_line((startx, starty, endx, endy), fill='blue')


def clear_canvas():
    canvas.delete('all')


# window
window = tk.Tk()
window.geometry('600x400')
window.title('L paint')

# canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# events
canvas.bind('<Button>', get_press)
canvas.bind('<ButtonRelease>', get_release)

# widgets
label = tk.Label(window, text='draw a line')
label.pack(padx=10, pady=10)

button = tk.Button(window, text='clear canvas', command=clear_canvas)
button.pack(padx=10, pady=10)

# run
window.mainloop()
