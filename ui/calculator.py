from tkinter import *
from tkmacosx import Button
from model.complex import Complex

class Calculator:

    # initializes the screen
    def __init__(self):
        root = Tk()
        set_frame(root)
        root.mainloop()

# sets up all necessary details associated with the current frame
def set_frame(root: Tk):
    set_frame_info(root)
    set_buttons(root)


# sets all base info of the frame
def set_frame_info(root: Tk):
    root.geometry("1200x500")
    root.title("Calculator")
    set_icon(root)
    root.resizable(False, False)


# sets the icon of the frame
def set_icon(root: Tk):
    icon = PhotoImage(file="ui/icon.png")
    root.iconphoto(True, icon)

# sets all the buttons on the frame
def set_buttons(root: Tk):
    place_num_buttons(root)
    place_ops_buttons(root)
    # i_button = create_button(root, text="i", command=root.destroy, bg="#eaaef5", size=size)
    # pi_button = create_button(root, text="π", command=root.destroy, bg="#eaaef5", size=size)
    # e_button = create_button(root, text="e", command=root.destroy, bg="#eaaef5", size=size)

# places numbers in a 3x4 grid. Helper for set_buttons
def place_num_buttons(root: Tk):
    ini_x = 0
    ini_y = 100
    size = 100
    one_button = create_button(root, text="1", command=root.destroy, bg="#daf5f3", size=size)
    two_button = create_button(root, text="2", command=root.destroy, bg="#daf5f3", size=size)
    three_button = create_button(root, text="3", command=root.destroy, bg="#daf5f3", size=size)
    four_button = create_button(root, text="4", command=root.destroy, bg="#daf5f3", size=size)
    five_button = create_button(root, text="5", command=root.destroy, bg="#daf5f3", size=size)
    six_button = create_button(root, text="6", command=root.destroy, bg="#daf5f3", size=size)
    seven_button = create_button(root, text="7", command=root.destroy, bg="#daf5f3", size=size)
    eight_button = create_button(root, text="8", command=root.destroy, bg="#daf5f3", size=size)
    nine_button = create_button(root, text="9", command=root.destroy, bg="#daf5f3", size=size)
    zero_button = create_button(root, text="0", command=root.destroy, bg="#daf5f3", size=size)
    decimal_button = create_button(root, text=".", command=root.destroy, bg="#daf5f3", size=size)
    equal_button = create_button(root, text="=", command=root.destroy, bg="#daf5f3", size=size)
    one_button.place(x=ini_x, y=ini_y)
    two_button.place(x=ini_x + size, y=ini_y)
    three_button.place(x=ini_x + 2*size, y=ini_y)
    four_button.place(x=ini_x, y=ini_y + size)
    five_button.place(x=ini_x + size, y=ini_y + size)
    six_button.place(x=ini_x + 2*size, y=ini_y + size)
    seven_button.place(x=ini_x, y=ini_y + 2*size)
    eight_button.place(x=ini_x + size, y=ini_y + 2*size)
    nine_button.place(x=ini_x + 2*size, y=ini_y + 2*size)
    zero_button.place(x=ini_x, y=ini_y + 3*size)
    decimal_button.place(x=ini_x + size, y=ini_y + 3*size)
    equal_button.place(x=ini_x + 2*size, y=ini_y + 3*size)

def place_ops_buttons(root: Tk):
    ini_x = 310
    ini_y = 100
    size = 100
    bg = "#eaaef5"

    place_bacic_ops(root, 310, 100, size, bg)

    place_trig_ops(root, 720, 100, size, bg)
    exp_button = create_button(root, text="eˣ", command=root.destroy, bg=bg, size=size)
    ln_button = create_button(root, text="ln()", command=root.destroy, bg=bg, size=size)
    lg_button = create_button(root, text="log(arg, base)", command=root.destroy, bg=bg, size=size)

    gamma_button = create_button(root, text="Γ()", command=root.destroy, bg=bg, size=size)
    erf_button = create_button(root, text="erf()", command=root.destroy, bg=bg, size=size)
    erfi_button = create_button(root, text="erfi()", command=root.destroy, bg=bg, size=size)


def place_bacic_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str):
    plus_button = create_button(root, text="+", command=root.destroy, bg=bg, size=size)
    minus_button = create_button(root, text="-", command=root.destroy, bg=bg, size=size)
    mult_button = create_button(root, text="x", command=root.destroy, bg=bg, size=size)
    div_button = create_button(root, text="÷", command=root.destroy, bg=bg, size=size)
    pow_button = create_button(root, text="^", command=root.destroy, bg=bg, size=size)
    root_button = create_button(root, text="√", command=root.destroy, bg=bg, size=size)
    plus_button.place(x=ini_x, y=ini_y)
    minus_button.place(x=ini_x + size, y=ini_y)
    mult_button.place(x=ini_x + 2 * size, y=ini_y)
    div_button.place(x=ini_x + 3 * size, y=ini_y)
    pow_button.place(x=ini_x, y=ini_y + size)
    root_button.place(x=ini_x + size, y=ini_y + size)

def place_trig_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str):
    sin_button = create_button(root, text="sin()", command=root.destroy, bg=bg, size=size)
    cos_button = create_button(root, text="cos()", command=root.destroy, bg=bg, size=size)
    tan_button = create_button(root, text="tan()", command=root.destroy, bg=bg, size=size)
    csc_button = create_button(root, text="csc()", command=root.destroy, bg=bg, size=size)
    sec_button = create_button(root, text="sec()", command=root.destroy, bg=bg, size=size)
    cot_button = create_button(root, text="cot()", command=root.destroy, bg=bg, size=size)
    sin_h_button = create_button(root, text="sinh()", command=root.destroy, bg=bg, size=size)
    cos_h_button = create_button(root, text="cosh()", command=root.destroy, bg=bg, size=size)
    tan_h_button = create_button(root, text="tanh()", command=root.destroy, bg=bg, size=size)
    arc_sin_button = create_button(root, text="arcsin()", command=root.destroy, bg=bg, size=size)
    arc_cos_button = create_button(root, text="arccos()", command=root.destroy, bg=bg, size=size)
    arc_tan_button = create_button(root, text="arctan()", command=root.destroy, bg=bg, size=size)

    sin_button.place(x=ini_x, y=ini_y)
    cos_button.place(x=ini_x + size, y=ini_y)
    tan_button.place(x=ini_x + 2 * size, y=ini_y)
    csc_button.place(x=ini_x, y=ini_y + size)
    sec_button.place(x=ini_x + size, y=ini_y + size)
    cot_button.place(x=ini_x + 2 * size, y=ini_y + size)
    sin_h_button.place(x=ini_x, y=ini_y + 2*size)
    cos_h_button.place(x=ini_x + size, y=ini_y + 2*size)
    tan_h_button.place(x=ini_x + 2*size, y=ini_y + 2*size)
    arc_sin_button.place(x=ini_x, y=ini_y + 3*size)
    arc_cos_button.place(x=ini_x + size, y=ini_y + 3*size)
    arc_tan_button.place(x=ini_x + 2*size, y=ini_y + 3*size)

def create_button(root: Tk, **kwargs):
    # for handling errors
    valid_indexes = {'text', 'command', 'bg', 'size'}
    items = kwargs.items()
    assert items.__sizeof__() <= valid_indexes.__sizeof__(), "too many arguments"
    for key, value in items:
        assert key in valid_indexes, "not a valid index"

    # working function
    bg = kwargs['bg']  # background color of the button
    size = kwargs['size'] # size of the button
    fg = "#000000"
    button = Button(root,
                    text=kwargs['text'],
                    bg=bg,
                    width=size,
                    height=size,
                    highlightbackground=bg,
                    fg=fg,
                    font=("Comic Sans", 20),
                    command=kwargs['command'])
    return button