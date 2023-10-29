from tkinter import *
from tkinter import font
from cell import Cell
import settings

root = Tk()
root.configure(background='deep sky blue')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Tic Tac Toe')
# root.resizable(False, False)

top_frame = Frame(root, background='deep sky blue', width=settings.WIDTH, height=settings.HEIGHT*0.2)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='deep sky blue',
    fg='white',
    text='Tic Tac Toe',
    font=('underline', 48)
)
game_title.place(x=settings.WIDTH * 0.25, y=0)

left_frame = Frame(root, background='deep sky blue', width=settings.WIDTH*0.2, height=settings.HEIGHT*0.8)
left_frame.place(x=0, y=settings.HEIGHT*0.2)

center_frame = Frame(root, background='deep sky blue', width=settings.WIDTH*0.8, height=settings.HEIGHT*0.8)
center_frame.place(x=settings.WIDTH*0.2, y=settings.HEIGHT*0.2)

for x in range(3):
    for y in range(3):
        c = Cell(x, y)
        c.create_button_object(center_frame)
        c.cell_button_object.grid(
            column=x,
            row=y)

Cell.create_player_info_label(left_frame)
Cell.cell_player_info_label.place(x=0, y=settings.HEIGHT*0.16)

root.mainloop()
