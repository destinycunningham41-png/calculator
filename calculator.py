import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("340x520")
root.configure(bg="black")
root.resizable(False, False)

expression = ""

def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("0")

def calculate():
    global expression
    try:
        expression = str(eval(expression))
        display_var.set(expression)
    except:
        expression = ""
        display_var.set("Error")

display_var = tk.StringVar(value="0")

display = tk.Label(
    root,
    textvariable=display_var,
    bg="black",
    fg="white",
    anchor="e",
    font=("Helvetica", 40),
    padx=20
)
display.pack(fill="both", pady=(40, 15))

button_frame = tk.Frame(root, bg="black")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for r, row in enumerate(buttons):
    c = 0

    for text in row:

        if text in ["/", "*", "-", "+", "="]:
            bg = "#ff9f0a"
            fg = "white"
        elif text in ["AC", "+/-", "%"]:
            bg = "#a5a5a5"
            fg = "black"
        else:
            bg = "#333333"
            fg = "white"

        cmd = (
            clear if text == "AC"
            else calculate if text == "="
            else lambda t=text: press(t)
        )

        if text == "0":
            btn = tk.Button(
                button_frame,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                font=("Helvetica", 20),
                borderwidth=0
            )
            btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
            c += 2
        else:
            btn = tk.Button(
                button_frame,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                font=("Helvetica", 20),
                borderwidth=0
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            c += 1

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

root.mainloop()