# -*-coding: utf-8-*-
from Tkinter import *
import math
import cmath


class Calculator:

    def get_input(self):
        self.expression = self.e.get()
        self.newtext = self.expression

    # Result
    def equals(self):
        self.get_input()
        print(self.expression)
        try:
            self.value = eval(self.expression)  # Equal statement
        except ZeroDivisionError:
            self.e.delete(0, END)
            self.e.insert(0, 'Can\'t division by ZERO!')
        except (SyntaxError, NameError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!!!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def clear_all(self):
        self.e.delete(0, END)

    def clear_last(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, arg):
        self.e.insert(END, arg)

    def trigonometric_form(self):
        self.get_input()
        try:
            complx = complex(self.expression)
            complex_modul = math.sqrt(pow(complx.imag, 2) + pow(complx.real, 2))
            polar_coord__sin = (complx.real/complex_modul)
            polar_coord__cos = (complx.imag/complex_modul)
            self.value = str(complex_modul)[:4] + '* (' + str(polar_coord__sin)[:4] + '  + ' + str(polar_coord__cos)[:4] + 'j )'
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def modul(self):
        self.get_input()
        try:
            complex_modul = complex(self.expression)
            self.value = math.sqrt(pow(complex_modul.imag, 2) + pow(complex_modul.real, 2))
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def main_argument(self):
        self.get_input()
        try:
            self.value = cmath.phase(complex(self.expression))
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def compare(self):
        self.get_input()
        try:
            if abs(complex(self.expression)) > abs(complex(self.memory)):
                self.value = str(self.expression) + " is bigger than " + str(self.memory)
            elif abs(complex(self.expression)) < abs(complex(self.memory)):
                self.value = str(self.expression) + " is smaller than " + str(self.memory)
            elif (complex(self.expression)) == (complex(self.memory)):
                self.value = str(self.expression) + " is the same as " + str(self.memory)
            else:
                raise Exception
        except SyntaxError or NameErrror or ValueError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        except Exception:
            self.e.delete(0, END)
            self.e.insert(0, "Can\'t compare values")
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def show_memory(self):
        self.e.delete(0, END)
        self.e.insert(0, self.memory)

    def save_memory(self):
        self.get_input()
        print(self.memory)
        try:
            eval(self.expression)   # Check is number and catch exception if doesn't
            self.memory = self.expression
        except SyntaxError or NameErrror or ValueError:
            self.memory = 0
            self.e.delete(0, END)
            self.e.insert(0, 'Can\'t save')
        else:
            self.show_memory()

    # Constructor
    def __init__(self, master):
        master.title('Complex Calculator - Patryk Nizio')
        master.geometry()
        self.e = Entry(master, width=40)
        self.e.grid(row=0, column=0, columnspan=10)
        self.e.focus_set()
        self.div = 'init'
        self.newdiv = self.div.decode('utf-8')
        self.memory = 0

        Button(master, text='Tryg. form', width=12, command=lambda: self.trigonometric_form()).grid(row=1, column=6)
        Button(master, text='Modul', width=12, command=lambda: self.modul()).grid(row=2, column=6)
        Button(master, text='Argument', width=12, command=lambda: self.main_argument()).grid(row=3, column=6)
        Button(master, text='Compare with M', width=12, command=lambda: self.compare()).grid(row=4, column=6)
        Button(master, text='AC', width=6, command=lambda: self.clear_all()).grid(row=1, column=5)
        Button(master, text='C', width=6, command=lambda: self.clear_last()).grid(row=2, column=5)
        Button(master, text='Save M', width=6, command=lambda: self.save_memory()).grid(row=3, column=5)
        Button(master, text='Show M', width=6, command=lambda: self.show_memory()).grid(row=4, column=5)
        Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=2, column=4)
        Button(master, text="*", width=3, command=lambda: self.action('*')).grid(row=3, column=3)
        Button(master, text="/", width=3, command=lambda: self.action('/')).grid(row=3, column=4)
        Button(master, text="=", width=9, bg="blue", fg="white", command=lambda: self.equals()).grid(row=4, column=3, columnspan=2)
        Button(master, text="j", width=3, bg="yellow", command=lambda: self.action('j')).grid(row=4, column=2)
        Button(master, text="(", width=3, command=lambda: self.action('(')).grid(row=1, column=3)
        Button(master, text=")", width=3, command=lambda: self.action(')')).grid(row=1, column=4)
        Button(master, text="7", width=3, command=lambda: self.action(7)).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1)


# Main
root = Tk()
obj = Calculator(root)  # object
root.mainloop()