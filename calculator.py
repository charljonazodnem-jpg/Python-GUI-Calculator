
import tkinter as tk

window = tk.Tk()
window.title("Cal-Q")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="#F3F5F9")

expression = ""

display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="#F2F2F0",
    fg="#0D0D0D",
    insertbackground="#0D0D0D",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=20, ipady=20)


def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"


def sync_expression(event):
    global expression
    expression = display.get()


display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)


def button_click(value):
    global expression

    if value == ".":
        current_number = expression

        for operator in "+-*/":
            current_number = current_number.split(operator)[-1]

        if "." in current_number:
            return

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression

    expression = ""
    display.delete(0, tk.END)
    
def backspace():
    global expression
    
    expression = expression[:-1]
    
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        expression = str(result)

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "ERROR")
        expression = ""


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


button_frame = tk.Frame(
    window,
    bg="#F3F5F9"
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)

clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="#FF5978",
    fg="#F3F5F9",
    bd=0,
    command=clear
)

backspace_button = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 18, "bold"),
    bg="#5B6E74",
    fg="#F3F5F9",
    bd=0,
    command=backspace
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)

backspace_button.grid(
    row=0,
    column=2,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)

for row_index, row in enumerate(buttons, start=1):

    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = "#0D0D0D"
            text_color = "#F3F5F9"

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#5B6E74"
            text_color = "#F3F5F9"

        else:
            command = lambda v=value: button_click(v)
            color = "#819FA7"
            text_color = "#F3F5F9"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg=text_color,
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)


window.mainloop()
