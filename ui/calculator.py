from tkinter import *
from tkmacosx import Button
from model.complex import Complex

class Calculator:

    # initializes the screen
    def __init__(self):
        root = Tk()
        text = set_text_box(root)
        press_down_buttons = {}
        set_frame(root, text, press_down_buttons)
        root.mainloop()

# entry constant
inputs = []

# sets up all necessary details associated with the current frame
def set_frame(root: Tk, text: Entry, press_down_buttons: dict):
    set_frame_info(root)
    set_buttons(root, text, press_down_buttons)

def set_text_box(root: Tk):
    # text = Text(root, width=17, height=1, font=("Comic Sans", 70), bg="#ffffff", fg="#000000")
    text = Entry(root, width= 17, font=("Comic Sans", 70), bg="#ffffff", fg="#000000")
    text.place(x=0, y=0)
    return text

# sets all base info of the frame
def set_frame_info(root: Tk):
    root.geometry("1150x500")
    root.title("Calculator")
    set_icon(root)
    root.resizable(False, False)


# sets the icon of the frame
def set_icon(root: Tk):
    icon = PhotoImage(file="ui/icon.png")
    root.iconphoto(True, icon)

# sets all the buttons on the frame
def set_buttons(root: Tk, text: Entry, press_down_buttons: dict):
    place_num_buttons(root, text, press_down_buttons)
    place_ops_buttons(root, text, press_down_buttons)
    place_constants(root, text)
    place_convert(root, text)

# places numbers in a 3x4 grid. Helper for set_buttons
def place_num_buttons(root: Tk, text: Entry, press_down_buttons: dict):
    ini_x = 0
    ini_y = 100
    size = 100
    one_button = create_button(root, text="1", command=lambda: text.insert(END, "1"), bg="#daf5f3", size=size)
    two_button = create_button(root, text="2", command=lambda: text.insert(END, "2"), bg="#daf5f3", size=size)
    three_button = create_button(root, text="3", command=lambda: text.insert(END, "3"), bg="#daf5f3", size=size)
    four_button = create_button(root, text="4", command=lambda: text.insert(END, "4"), bg="#daf5f3", size=size)
    five_button = create_button(root, text="5", command=lambda: text.insert(END, "5"), bg="#daf5f3", size=size)
    six_button = create_button(root, text="6", command=lambda: text.insert(END, "6"), bg="#daf5f3", size=size)
    seven_button = create_button(root, text="7", command=lambda: text.insert(END, "7"), bg="#daf5f3", size=size)
    eight_button = create_button(root, text="8", command=lambda: text.insert(END, "8"), bg="#daf5f3", size=size)
    nine_button = create_button(root, text="9", command=lambda: text.insert(END, "9"), bg="#daf5f3", size=size)
    zero_button = create_button(root, text="0", command=lambda: text.insert(END, "0"), bg="#daf5f3", size=size)
    decimal_button = create_button(root, text=".", command=lambda: text.insert(END, "."), bg="#daf5f3", size=size)
    equal_button = create_button(root, text="=", command=lambda: equal_lambda(text, press_down_buttons), bg="#daf5f3", size=size)
    press_down_buttons['='] = equal_button
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

def place_ops_buttons(root: Tk, text: Entry, press_down_buttons: dict):
    size = 100
    place_basic_ops(root, 310, 100, size, "#eaaef5", text, press_down_buttons)
    place_other_ops(root, 410, 300, size, "#f56969", text)
    place_trig_ops(root, 720, 100, size, "#eaaef5", text)
    place_special_ops(root, 1030, 100, size, "#eaaef5", text)

def place_constants(root: Tk, text: Entry):
    size = 100
    ini_x = 310
    ini_y = 400
    bg = "#a2dcf2"
    i_button = create_button(root, text="i", command=lambda: text.insert(END, "i"), bg=bg, size=size)
    pi_button = create_button(root, text="π", command=lambda: input_constants(text, "π"), bg=bg, size=size)
    e_button = create_button(root, text="e", command=lambda: input_constants(text, "e"), bg=bg, size=size)
    phi_button = create_button(root, text="Φ", command=lambda: input_constants(text, "Φ"), bg=bg, size=size)
    i_button.place(x=ini_x, y=ini_y)
    pi_button.place(x=ini_x + size, y=ini_y)
    e_button.place(x=ini_x + 2*size, y=ini_y)
    phi_button.place(x=ini_x + 3*size, y=ini_y)

def place_convert(root: Tk, text: Entry):
    size = 89
    ini_x = 741
    ini_y = 3
    bg = "#98f794"
    rect_button = create_button(root, text="a + bi", command=lambda: convert_lambda(NONE, text), bg=bg, size=size)
    cis_button = create_button(root, text="r * cis(θ)", command=lambda: convert_lambda(Complex.rect_to_cis, text),
                               bg=bg, size=size)
    euler_button = create_button(root, text="r * eⁱᶿ", command=lambda: convert_lambda(Complex.rect_to_euler, text),
                                 bg=bg, size=size)
    rect_button.place(x=ini_x, y=ini_y)
    cis_button.place(x=ini_x + size, y=ini_y)
    euler_button.place(x=ini_x + 2 * size, y=ini_y)

def place_basic_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str, text: Entry, press_down_buttons: dict):
    plus_button = create_button(root, text="+",
                                command= lambda: double_input_function_lambda('+', text, press_down_buttons),
                                bg=bg, size=size)
    minus_button = create_button(root, text="-",
                                 command=lambda: double_input_function_lambda('-', text, press_down_buttons),
                                 bg=bg, size=size)
    mult_button = create_button(root, text="x",
                                command=lambda: double_input_function_lambda('x', text, press_down_buttons),
                                bg=bg, size=size)
    div_button = create_button(root, text="÷",
                               command=lambda: double_input_function_lambda('÷', text, press_down_buttons),
                               bg=bg, size=size)
    pow_button = create_button(root, text="^",
                               command=lambda: double_input_function_lambda('^', text, press_down_buttons),
                               bg=bg, size=size)
    root_button = create_button(root, text="√",
                                command=lambda: double_input_function_lambda('√', text, press_down_buttons),
                                bg=bg, size=size)
    exp_button = create_button(root, text="eˣ", command=lambda: function_lambda(Complex.exp, text),
                               bg=bg, size=size)
    ln_button = create_button(root, text="ln(x)", command=lambda: function_lambda(Complex.natural_log, text),
                              bg=bg, size=size)
    lg_button = create_button(root, text="log(x, b)",
                              command=lambda: double_input_function_lambda('log', text, press_down_buttons),
                              bg=bg, size=size)
    press_down_buttons['+'] = plus_button
    press_down_buttons['-'] = minus_button
    press_down_buttons['x'] = mult_button
    press_down_buttons['÷'] = div_button
    press_down_buttons['^'] = pow_button
    press_down_buttons['√'] = root_button
    press_down_buttons['log'] = lg_button
    plus_button.place(x=ini_x, y=ini_y)
    minus_button.place(x=ini_x + size, y=ini_y)
    mult_button.place(x=ini_x + 2 * size, y=ini_y)
    div_button.place(x=ini_x + 3 * size, y=ini_y)
    pow_button.place(x=ini_x, y=ini_y + size)
    root_button.place(x=ini_x + size, y=ini_y + size)
    exp_button.place(x=ini_x + 2*size, y=ini_y + size)
    ln_button.place(x=ini_x + 3*size, y=ini_y + size)
    lg_button.place(x=ini_x, y=ini_y + 2*size)

def place_other_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str, text: Entry):
    clear_button = create_button(root, text="AC", command=lambda: text.delete(0, END), bg=bg, size=size)
    change_sign_button = create_button(root, text="+/-", command=lambda: plus_minus_lambda(text), bg=bg, size=size)
    percentage_button = create_button(root, text="%", command=lambda: percentage_lambda(text), bg=bg, size=size)
    clear_button.place(x=ini_x, y=ini_y)
    change_sign_button.place(x=ini_x + size, y=ini_y)
    percentage_button.place(x=ini_x + 2*size, y=ini_y)


def place_trig_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str, text: Entry):
    sin_button = create_button(root, text="sin(x)", command=lambda: function_lambda(Complex.sin, text),
                               bg=bg, size=size)
    cos_button = create_button(root, text="cos(x)", command=lambda: function_lambda(Complex.cos, text),
                               bg=bg, size=size)
    tan_button = create_button(root, text="tan(x)", command=lambda: function_lambda(Complex.tan, text),
                               bg=bg, size=size)
    csc_button = create_button(root, text="csc(x)", command=lambda: function_lambda(Complex.csc, text),
                               bg=bg, size=size)
    sec_button = create_button(root, text="sec(x)", command=lambda: function_lambda(Complex.sec, text),
                               bg=bg, size=size)
    cot_button = create_button(root, text="cot(x)", command=lambda: function_lambda(Complex.cot, text),
                               bg=bg, size=size)
    sin_h_button = create_button(root, text="sinh(x)", command=lambda: function_lambda(Complex.sinh, text),
                                 bg=bg, size=size)
    cos_h_button = create_button(root, text="cosh(x)", command=lambda: function_lambda(Complex.cosh, text),
                                 bg=bg, size=size)
    tan_h_button = create_button(root, text="tanh(x)", command=lambda: function_lambda(Complex.tanh, text),
                                 bg=bg, size=size)
    arc_sin_button = create_button(root, text="arcsin(x)", command=lambda: function_lambda(Complex.arcsin, text),
                                   bg=bg, size=size)
    arc_cos_button = create_button(root, text="arccos(x)", command=lambda: function_lambda(Complex.arccos, text),
                                   bg=bg, size=size)
    arc_tan_button = create_button(root, text="arctan(x)", command=lambda: function_lambda(Complex.arctan, text),
                                   bg=bg, size=size)

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

def place_special_ops(root: Tk, ini_x: int, ini_y: int, size: int, bg: str, text: Entry):
    gamma_button = create_button(root, text="Γ(x)", command=lambda: function_lambda(Complex.gamma, text),
                                 bg=bg, size=size)
    erf_button = create_button(root, text="erf(x)", command=lambda: function_lambda(Complex.erf, text),
                               bg=bg, size=size)
    erfi_button = create_button(root, text="erfi(x)", command=lambda: function_lambda(Complex.erf_i, text),
                                bg=bg, size=size)
    gamma_button.place(x=ini_x, y=ini_y)
    erf_button.place(x=ini_x, y=ini_y + size)
    erfi_button.place(x=ini_x, y=ini_y + 2*size)

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

# functions for lambdas

def function_lambda(func, text: Entry):
    try:
        ans = func(Complex(text.get())).__repr__()
        text.delete(0, END)
        text.insert(0, ans)
    except ValueError:
        text.delete(0, END)
        text.insert(0, "Undefined")
    except AssertionError:
        text.delete(0, END)
        text.insert(0, "Undefined")
    except OverflowError:
        text.delete(0, END)
        text.insert(0, "Error: Number too large")

def convert_lambda(func, text: Entry):
    s = text.get()
    if s == "":
        return
    else:
        ans = func(Complex(s))
        text.delete(0, END)
        text.insert(0, ans)

def plus_minus_lambda(text: Entry):
    s = text.get()
    if s == "":
        return
    else:
        inp = Complex(text.get())
        ans = Complex.mult(Complex(-1, 0), inp).__repr__()
        text.delete(0, END)
        text.insert(0, ans)

def percentage_lambda(text: Entry):
    inp = text.get()
    if inp != "":
        c = Complex(inp)
        ans = Complex.div(c, Complex(100, 0))
        text.delete(0, END)
        text.insert(0, ans)

def equal_lambda(text: Entry, press_down_buttons: dict):
    ans = ""
    if len(inputs) == 0:
        ans = constant_handler(text.get())
    else: # len(inputs) == 2
        for key in press_down_buttons.keys():
            press_down_buttons[key]['state'] = NORMAL
        op = inputs[1]
        a = Complex(constant_handler(inputs[0]))
        b = Complex(constant_handler(text.get()))
        if op == "+":
            ans = Complex.add(a, b).__repr__()
        elif op == "-":
            ans = Complex.sub(a, b).__repr__()
        elif op == "x":
            ans = Complex.mult(a, b).__repr__()
        elif op == "÷":
            ans = Complex.div(a, b).__repr__()
        elif op == "^":
            ans = Complex.power(a, b).__repr__()
        elif op == "√":
            ans = Complex.root(a, b).__repr__()
        elif op == "log":
            ans = Complex.log(a, b).__repr__()
    inputs.clear()
    text.delete(0, END)
    text.insert(0, ans)

def double_input_function_lambda(s: str, text: Entry, press_down_buttons: dict):
    if text.get() == "":
        return
    else:
        button = press_down_buttons[s]
        button['state'] = DISABLED
        # press_down_buttons['=']['state'] = DISABLED
        inputs.append(text.get())
        inputs.append(s)
        text.delete(0, END)



def constant_handler(inp: str):
    if inp == "π":
        ans = "3.141592653589793"
    elif inp == "-π":
        ans = "-3.141592653589793"
    elif inp == "e":
        ans = "2.718281828459045"
    elif inp == "-e":
        ans = "-2.718281828459045"
    elif inp == "Φ":
        ans = "1.618033988749895"
    elif inp == "-Φ":
        ans = "-1.618033988749895"
    else:
        ans = inp
    return ans

def input_constants(text: Entry, s: str):
    text.delete(0, END)
    text.insert(0, s)


