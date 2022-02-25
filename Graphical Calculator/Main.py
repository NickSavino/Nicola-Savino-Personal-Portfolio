from logging import root
import Gui

if __name__ == '__main__':
    
    digits = Gui.new_frame('200', '300', 'sw', 'bottom')
    row = 0
    column = 3
    
    for i in range(9, -1, -1):
        print(i)
        print(f"{row} {column}")
        Gui.calculator_buttons(i, digits, row, column)
        column -= 1
        if column < 1:
            row += 1
            column = 3
    Gui.calculator_buttons('.', digits, row=3, column=2)

    Gui.root.mainloop()