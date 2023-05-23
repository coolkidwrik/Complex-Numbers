from tkinter import *
from tkmacosx import Button

class Calculator:

    # initializes the screen
    def __init__(self):
        root = Tk()
        set_frame(root)
        root.mainloop()

# sets up all necessary details associated with the current frame
def set_frame(root: Tk, img1: PhotoImage, img2: PhotoImage):
    set_frame_info(root)
    set_buttons(root)


# sets all base info of the frame
def set_frame_info(root: Tk):
    root.geometry("700x500")
    root.title("Calculator")
    set_icon(root)
    root.resizable(False, False)


# sets the icon of the frame
def set_icon(root: Tk):
    icon = PhotoImage(file="../images/taiga_logo.png") # image to be changes
    root.iconphoto(True, icon)

# sets all the buttons on the frame
def set_buttons(root: Tk):
    button1 = create_button(root, text="Browse Lists", command=root.destroy)    # buttons to be changed
    button2 = create_button(root, text="Create New Lists", command=root.destroy)
    button3 = create_button(root, text="Quit", command=root.destroy)
    button1.place(x=80, y=250)
    button2.place(x=80, y=300)
    button3.place(x=80, y=350)


def create_button(root: Tk, **kwargs):      # implementation to be changed
    # for handling errors
    valid_indexes = {'text', 'command'}
    items = kwargs.items()
    assert items.__sizeof__() <= valid_indexes.__sizeof__(), "too many arguments"
    for key, value in items:
        assert key in valid_indexes, "not a valid index"

    # working function
    bg = "#e7abf5"  # background color of the button
    button = Button(root,
                    text=kwargs['text'],
                    bg=bg,
                    width=270,
                    height=40,
                    highlightbackground=bg,
                    fg="#fa39b3",
                    font=("Comic Sans", 30, "italic"),
                    command=kwargs['command'])
    return button