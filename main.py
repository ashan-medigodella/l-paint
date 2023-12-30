import tkinter as tk

# Global variables to store starting and ending coordinates
startx, starty = 0, 0
endx, endy = 0, 0


# Event handler for mouse button press
def get_press(event):
    global startx, starty
    startx = event.x
    starty = event.y


# Event handler for mouse button release
def get_release(event):
    global endx, endy
    endx = event.x
    endy = event.y

    # Draw a line on the canvas
    canvas.create_line(startx, starty, endx, endy, fill='blue')


# Function to clear the canvas
def clear_canvas():
    canvas.delete('all')


# Create the main window
window = tk.Tk()
window.geometry('600x400')
window.title('L paint')

# Create a canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# Bind mouse button press and release events to functions
canvas.bind('<Button>', get_press)
canvas.bind('<ButtonRelease>', get_release)

# Create widgets
label = tk.Label(window, text='draw a line')
label.pack(padx=10, pady=10)

button = tk.Button(window, text='clear canvas', command=clear_canvas)
button.pack(padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
