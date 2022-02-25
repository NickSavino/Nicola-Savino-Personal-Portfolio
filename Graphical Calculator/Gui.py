import tkinter as tk

root = tk.Tk()
root.title("Graphical Calculator V0.1")
root.geometry("400x600")



def new_frame(height, width, anchor, side):
    frame = tk.Frame(root, height=height, width=width)
    frame.pack(anchor=anchor, side=side)
    return frame

def calculator_buttons(integer, frame, row, column):
    button = tk.Button(frame, text=f"{integer}", height='3', width='5')
    button.grid(row=row, column=column)

def arithmetic_buttons():
    button = tk.Button(frame,)