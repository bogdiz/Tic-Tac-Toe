from tkinter import *
import sys
import ctypes


class Cell:
    interchange = False
    all = []
    used_count = 0
    cell_player_info_label = interchange
    plyrInfo = interchange

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cell_button_object = None
        self.is_used = None
        self.is_x = None
        self.is_0 = None
        Cell.all.append(self)

    def create_button_object(self, frame):
        btn = Button(
            frame,
            bg='white',
            fg='black',
            width=18,
            height=8
        )
        # img = PhotoImage(file='C:/Users/Bogdi/Desktop/download.png')
        # btn.config(image=img)
        # btn.pack()
        self.cell_button_object = btn
        btn.bind('<Button-1>', self.left_click_actions)

    def left_click_actions(self, event):
        self.is_used = True
        # print(self.surrounded_cells())
        Cell.used_count += 1

        if not Cell.interchange:
            self.cell_button_object.configure(text='X')
            self.is_x = True
            Cell.interchange = True
        else:
            self.cell_button_object.configure(text='0')
            self.is_0 = True
            Cell.interchange = False
        if self.is_used:
            self.cell_button_object.unbind('<Button-1>')

        if Cell.interchange is False:
            Cell.plyrInfo = 'X'
        else:
            Cell.plyrInfo = '0'
        if Cell.cell_player_info_label:
            Cell.cell_player_info_label.configure(
                text=f"Player {Cell.plyrInfo} :"
            )
        self.win_condition()

        if Cell.used_count == 9:
            ctypes.windll.user32.MessageBoxW(
                0,
                "         It's a tie!",
                'GAME OVER',
                0
            )
            sys.exit()

    def get_cell_by_axis(self, x, y):
        for c in Cell.all:
            if c.x == x and c.y == y:
                return c

    def surrounded_cells(self):
        line1 = [
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 2, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 2, self.y),
        ]
        line2 = [
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 2),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 2),
        ]
        line3 = [
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 2, self.y + 2),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 2, self.y - 2)
        ]
        line4 = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 2, self.y - 2),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x + 2, self.y + 2),
        ]
        line1 = [x for x in line1 if x is not None]
        line1 = [i for i in line1 if i.x == self.x or i.y == self.y or i.x == i.y or i.x + i.y == 2]

        line2 = [x for x in line2 if x is not None]
        line2 = [i for i in line2 if i.x == self.x or i.y == self.y or i.x == i.y or i.x + i.y == 2]

        line3 = [x for x in line3 if x is not None]
        line3 = [i for i in line3 if i.x == self.x or i.y == self.y or i.x == i.y or i.x + i.y == 2]

        line4 = [x for x in line4 if x is not None]
        line4 = [i for i in line4 if i.x == self.x or i.y == self.y or i.x == i.y or i.x + i.y == 2]

        cells = line1 + line2 + line3 + line4
        return cells

    def win_condition(self):
        cntX = 0
        cnt0 = 0
        cnt = 0
        for i in self.surrounded_cells():
            cnt += 1
            if cnt % 2 == 1:
                cntX = cnt0 = 0
            if cntX == 1 and self.is_x is True and i.is_x is True:
                # print("AI CASTIGAT")
                ctypes.windll.user32.MessageBoxW(
                    0,
                    'Player X has won!',
                    'GAME OVER',
                    0
                )
                sys.exit()
            else:
                cntX = 0
            if self.is_x is True and i.is_x is True:
                cntX = 1
            ################################
            if cnt0 == 1 and self.is_0 is True and i.is_0 is True:
                # print("AI CASTIGAT")
                ctypes.windll.user32.MessageBoxW(
                    0,
                    'Player 0 has won!',
                    'GAME OVER',
                    0,
                )
                sys.exit()
            else:
                cnt0 = 0
            if self.is_0 is True and i.is_0 is True:
                cnt0 = 1

    @staticmethod
    def create_player_info_label(frame):
        if Cell.interchange is False:
            Cell.plyrInfo = 'X'
        else:
            Cell.plyrInfo = '0'

        lbl = Label(
            frame,
            text=f"Player {Cell.plyrInfo} :",
            width=10,
            height=5,
            bg='deep sky blue',
            fg='white',
            font=('', 18)
        )
        Cell.cell_player_info_label = lbl

    def __repr__(self):
        return f'Cell({self.x},{self.y})'
