from tkinter import *
from tkinter import ttk
import tkinter.font as font
from math import *


class Calculator:

    def __init__(self):

        self.master = Tk()
        #self.master.resizable(False, False)
        frame = ttk.Frame(self.master, padding=(5, 5, 5, 5))
        frame.bind_all("<Key>", self.key_listen)
        frame.pack(expand=YES,
                   fill=BOTH)

        self.customFont = font.Font(family="Monaco",
                                    size=10,
                                    weight="bold")

        self.display_num = StringVar()
        self.display_num.set("0")

        self.first_num = DoubleVar()
        self.second_num = DoubleVar()

        self.is_adding = False
        self.is_subtracting = False
        self.is_multiplying = False
        self.is_dividing = False

        self.has_decimal = False

        self.has_old_calculation = False

        self.w = Label(frame,
                       textvariable=self.display_num,
                       relief="sunken",
                       anchor="e",
                       bg="white",
                       justify="right",
                       width=1,
                       font=self.customFont)

        self.w.grid(ipady=10,
                    row=0,
                    column=0,
                    columnspan=4,
                    sticky=(N, S, E, W))

        # self.w.pack(expand=YES,
        #           fill=BOTH)

        self.seven_key = Button(frame,
                                text="7",
                                relief="solid",
                                bg="white",
                                command=lambda: self.entry(7),
                                font=self.customFont)

        self.seven_key.grid(ipadx=14,
                            ipady=10,
                            row=3,
                            column=0,
                            sticky=(N, S, E, W))

        self.eight_key = Button(frame,
                                text="8",
                                bg="white",
                                command=lambda: self.entry(8),
                                font=self.customFont)

        self.eight_key.grid(ipadx=10,
                            ipady=10,
                            row=3,
                            column=1,
                            sticky=(N, S, E, W))

        self.nine_key = Button(frame,
                               text="9",
                               bg="white",
                               command=lambda: self.entry(9),
                               font=self.customFont)

        self.nine_key.grid(ipadx=14,
                           ipady=10,
                           row=3,
                           column=2,
                           sticky=(N, S, E, W))

        self.four_key = Button(frame,
                               text="4",
                               bg="white",
                               command=lambda: self.entry(4),
                               font=self.customFont)

        self.four_key.grid(ipadx=14,
                           ipady=10,
                           row=4,
                           column=0, sticky=(N, S, E, W))

        self.five_key = Button(frame,
                               text="5",
                               bg="white",
                               command=lambda: self.entry(5),
                               font=self.customFont)

        self.five_key.grid(ipadx=10,
                           ipady=10,
                           row=4,
                           column=1,
                           sticky=(N, S, E, W))

        self.six_key = Button(frame,
                              text="6",
                              bg="white",
                              command=lambda: self.entry(6),
                              font=self.customFont)

        self.six_key.grid(ipadx=14,
                          ipady=10,
                          row=4,
                          column=2,
                          sticky=(N, S, E, W))

        self.one_key = Button(frame,
                              text="1",
                              bg="white",
                              command=lambda: self.entry(1),
                              font=self.customFont)

        self.one_key.grid(ipadx=14,
                          ipady=10,
                          row=5,
                          column=0, sticky=(N, S, E, W))

        self.two_key = Button(frame,
                              text="2",
                              bg="white",
                              command=lambda: self.entry(2),
                              font=self.customFont)

        self.two_key.grid(ipadx=10,
                          ipady=10,
                          row=5,
                          column=1, sticky=(N, S, E, W))

        self.three_key = Button(frame,
                                text="3",
                                bg="white",
                                command=lambda: self.entry(3),
                                font=self.customFont)

        self.three_key.grid(ipadx=14,
                            ipady=10,
                            row=5,
                            column=2,
                            sticky=(N, S, E, W))

        self.zero_key = Button(frame,
                               text="0",
                               bg="gray",
                               command=lambda: self.entry(0),
                               font=self.customFont)

        self.zero_key.grid(ipadx=30,
                           ipady=10,
                           row=6,
                           column=0,
                           columnspan=2,
                           sticky=(N, S, E, W))

        self.equals_key = Button(frame,
                                 text="=",
                                 bg="white",
                                 command=lambda: self.solve(),
                                 font=self.customFont)

        self.equals_key.grid(ipadx=14,
                             ipady=33,
                             row=5,
                             column=3,
                             rowspan=3,
                             sticky=(N, S, E, W))

        self.plus_key = Button(frame,
                               text="+",
                               bg="white",
                               command=lambda: self.add(),
                               font=self.customFont)

        self.plus_key.grid(ipadx=14,
                           ipady=10,
                           row=4,
                           column=3,
                           sticky=(N, S, E, W))

        self.minus_key = Button(frame,
                                text="-",
                                bg="white",
                                command=lambda: self.sub(),
                                font=self.customFont)

        self.minus_key.grid(ipadx=14,
                            ipady=10,
                            row=3,
                            column=3,
                            sticky=(N, S, E, W))

        self.clear_key = Button(frame,
                                text="C",
                                bg="white",
                                command=lambda: self.clear(),
                                font=self.customFont)

        self.clear_key.grid(ipadx=14,
                            ipady=10,
                            row=2,
                            column=0,
                            sticky=(N, S, E, W))

        self.mult_key = Button(frame,
                               text="*",
                               bg="white",
                               command=lambda: self.mult(),
                               font=self.customFont)

        self.mult_key.grid(ipadx=14,
                           ipady=10,
                           row=2,
                           column=3,
                           sticky=(N, S, E, W))

        self.div_key = Button(frame,
                              text="/",
                              bg="white",
                              command=lambda: self.div(),
                              font=self.customFont)
        self.div_key.grid(ipadx=14,
                          ipady=10,
                          row=2,
                          column=2,
                          sticky=(N, S, E, W))

        self.remove_num_key = Button(frame,
                                     text="<-",
                                     bg="white",
                                     command=lambda: self.remove_num(),
                                     font=self.customFont)

        self.remove_num_key.grid(ipadx=9,
                                 ipady=10,
                                 row=2,
                                 column=1,
                                 sticky=(N, S, E, W))

        self.decimal_place = Button(frame,
                                    text=".",
                                    bg="white",
                                    command=lambda: self.entry('.'),
                                    font=self.customFont)

        self.decimal_place.grid(ipadx=10,
                                ipady=10,
                                row=6,
                                column=2,
                                sticky=(N, S, E, W))

        self.square_root_button = Button(frame,
                                         text="SQ",
                                         bg="white",
                                         command=lambda: self.square_root(),
                                         font=self.customFont)

        self.square_root_button.grid(ipadx=10,
                                     ipady=10,
                                     row=1,
                                     column=1,
                                     sticky=(N, S, E, W))

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_rowconfigure(5, weight=1)
        frame.grid_rowconfigure(6, weight=1)

        self.master.mainloop()

    def key_listen(self, event):
        key = event.char
        if key == '0':
            self.entry(0)
            return
        if key == '1':
            self.entry(1)
            return
        if key == '2':
            self.entry(2)
            return
        if key == '3':
            self.entry(3)
            return
        if key == '4':
            self.entry(4)
            return
        if key == '5':
            self.entry(5)
            return
        if key == '6':
            self.entry(6)
            return
        if key == '7':
            self.entry(7)
            return
        if key == '8':
            self.entry(8)
            return
        if key == '9':
            self.entry(9)
            return
        if key == '\r':
            self.solve()
            return
        if key == '+':
            self.add()
            return
        if key == '-':
            self.sub()
            return
        if key == '*':
            self.mult()
            return
        if key == '/':
            self.div()
            return
        if key == '\b':
            self.remove_num()
            return
        if key == '.':
            self.entry('.')
        if key == '\x1B':
            exit()

    def entry(self, num):
        temp = self.display_num.get()
        if self.has_decimal == False or num != '.':
            if num == '.':
                self.has_decimal = True
            if temp == "0":
                self.display_num.set(str(num))
            elif self.has_old_calculation:
                self.clear()
                self.display_num.set(str(num))
                self.has_old_calculation = False
            else:
                temp += str(num)
                self.display_num.set(str(temp))
            print(num)

    def remove_num(self):
        temp = self.display_num.get()
        temp = temp[:-1]
        self.display_num.set(temp)

    def clear(self):
        self.display_num.set("0")
        self.has_old_calculation = False
        self.has_decimal = False
        self.is_adding = False
        self.is_subtracting = False
        self.is_multiplying = False
        self.is_dividing = False
        self.first_num = 0
        self.second_num = 0

    def add(self):
        self.first_num = self.display_num.get()
        self.display_num.set("0")
        self.has_decimal = False
        self.is_adding = True
        self.is_subtracting = False
        self.is_multiplying = False
        self.is_dividing = False

    def sub(self):
        self.first_num = self.display_num.get()
        self.display_num.set("0")
        self.has_decimal = False
        self.is_adding = False
        self.is_subtracting = True
        self.is_multiplying = False
        self.is_dividing = False

    def mult(self):
        self.first_num = self.display_num.get()
        self.display_num.set("0")
        self.has_decimal = False
        self.is_adding = False
        self.is_subtracting = False
        self.is_multiplying = True
        self.is_dividing = False

    def div(self):
        self.first_num = self.display_num.get()
        self.display_num.set("0")
        self.has_decimal = False
        self.is_adding = False
        self.is_subtracting = False
        self.is_multiplying = False
        self.is_dividing = True

    def square_root(self):
        self.first_num = self.display_num.get()
        self.first_num = sqrt(float(self.first_num))
        self.display_num.set(str(self.first_num))

    def solve(self):
        self.second_num = self.display_num.get()
        if self.is_adding:
            temp = float(self.first_num) + float(self.second_num)
            temp = round(temp, 4)
            self.display_num.set(str(temp))
            self.has_old_calculation = True
            return
        elif self.is_subtracting:
            temp = float(self.first_num) - float(self.second_num)
            temp = round(temp, 4)
            self.display_num.set(str(temp))
            self.has_old_calculation = True
            return
        elif self.is_multiplying:
            temp = float(self.first_num) * float(self.second_num)
            temp = round(temp, 4)
            self.display_num.set(str(temp))
            self.has_old_calculation = True
            return
        elif self.is_dividing:
            if float(self.second_num) == 0:
                self.display_num.set("Division by ZERO")
                self.has_old_calculation = True
                return
            temp = float(self.first_num) / float(self.second_num)
            temp = round(temp, 4)
            self.display_num.set(str(temp))
            self.has_old_calculation = True


Calculator()
