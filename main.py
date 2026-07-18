import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) 
column_count = len(button_values[0])

white = "#F1E4F3"
gray = "#D6D2D2"
light_pink = "#F4BBD3"
pink = "#F686BD"
dark_pink = "#FE5D9F"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", anchor="e", font=("Arial", 45), bg=white, fg=dark_pink, width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                 bg=white, fg=dark_pink, width=column_count-1, height=1,
                                 command=lambda value=value: button_clicked(value))
        if value in right_symbols:
            button.config(bg=pink, fg=white)
        elif value in top_symbols:
            button.config(bg=light_pink, fg=dark_pink)
        else:
            button.config(bg=gray, fg=pink)
        button.grid(row=row + 1, column=column, sticky="nsew")

frame.pack()

A = 0
operator = None
B = None

def clear_all():
    global A, B, operator
    A = 0
    B = None
    operator = None

def remove_zero_decimal(num):
    if isinstance(num, float) and num.is_integer():
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator


    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
        else:
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)


window.update()
width = window.winfo_width()
height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width // 2) - (width // 2))
window_y = int((screen_height // 2) - (height // 2))

window.geometry(f"{width}x{height}+{window_x}+{window_y}")

window.mainloop()
