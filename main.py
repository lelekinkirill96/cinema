import tkinter as tk
from fpdf import FPDF

minn = 30
import tkinter.messagebox
import webbrowser
class Printer:
    def __init__(self, namefilm, place):
        self.namefilm = namefilm
        self.place = place

    def generate(self):
        number = self.place[0]
        row = self.place[1]
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image('ticket.png', w=pdf.w / 3.0, h=pdf.h / 12.0)

        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=200, h=50, txt=f'Name of film: {self.namefilm}', border=0, align='L', ln=1)
        pdf.cell(w=200, h=50, txt=f'ROW           NUMBER', border=0, align='L', ln=1)
        pdf.cell(w=200, h=30, txt=f'{row}                   {number}', border=0, align='L', ln=1)
        pdf.set_xy(150, 150)
        pdf.rotate(90, 250, 100)
        pdf.set_font(family='Times', size=28, style='B')
        pdf.cell(w=100, h=25, txt='CONTROL')

        pdf.output(self.namefilm)
        webbrowser.open(self.namefilm)


class Question:
    def __init__(self, place):
        self.place = place
        self.this_place = place['text']

        self.roott = tk.Tk()
        self.roott.title('Билет')
        self.roott.geometry('250x200+100+100')

        self.roott.grid_columnconfigure(0, minsize=15)
        self.roott.grid_columnconfigure(1, minsize=15)
        self.roott.grid_columnconfigure(2, minsize=15)
        self.roott.grid_columnconfigure(3, minsize=15)
        self.roott.grid_columnconfigure(4, minsize=15)
        self.roott.grid_columnconfigure(5, minsize=15)
        self.roott.grid_columnconfigure(6, minsize=15)
        self.roott.grid_columnconfigure(7, minsize=15)
        self.roott.grid_columnconfigure(8, minsize=15)

        self.roott.grid_rowconfigure(0, minsize=15)
        self.roott.grid_rowconfigure(1, minsize=15)
        self.roott.grid_rowconfigure(2, minsize=15)
        self.roott.grid_rowconfigure(3, minsize=15)
        self.roott.grid_rowconfigure(4, minsize=15)
        self.roott.grid_rowconfigure(5, minsize=15)

        self.myprint1 = tk.Button(self.roott, text='распечатать', font=('Arial', 12), bg='light green',
                                  command=self.printerist)
        self.myprint2 = tk.Button(self.roott, text='не распечатывать', font=('Arial', 12), bg='light green',
                                  command=self.close_window)
        self.myprint1.grid(row=4, column=1, columnspan=2, sticky='wens', padx=10, pady=10)
        self.myprint2.grid(row=5, column=1, columnspan=6, sticky='wens', padx=10, pady=10)

        self.roott.mainloop()

    def printerist(self):
        ticket = Printer('Superman', self.this_place)
        ticket.generate()
        print("Печать")

    def close_window(self):
        self.roott.destroy()
        self.place['bg'] = 'white'

class My_gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('cinema')
        self.root.geometry('400x300+100+100')

        self.title = tk.Label(
            self.root,
            text='Экран',
            font=('Arial 16 bold'),
            bg='brown',
            fg='#FF0')

        self.title.grid(row=0, column=2, columnspan=3, sticky='wens', padx=10, pady=10)

        self.mybutton = tk.Button(self.root, bg='white', text='1a', command=lambda: self.makesmth(self.mybutton))
        self.mybutton1 = tk.Button(self.root, bg='white', text='2a', command=lambda: self.makesmth(self.mybutton1))
        self.mybutton2 = tk.Button(self.root, bg='white', text='3a', command=lambda: self.makesmth(self.mybutton2))
        self.mybutton3 = tk.Button(self.root, bg='white', text='4a', command=lambda: self.makesmth(self.mybutton3))
        self.mybutton4 = tk.Button(self.root, bg='white', text='5a', command=lambda: self.makesmth(self.mybutton4))
        self.mybutton5 = tk.Button(self.root, bg='white', text='1b', command=lambda: self.makesmth(self.mybutton5))
        self.mybutton6 = tk.Button(self.root, bg='white', text='2b', command=lambda: self.makesmth(self.mybutton6))
        self.mybutton7 = tk.Button(self.root, bg='white', text='3b', command=lambda: self.makesmth(self.mybutton7))
        self.mybutton8 = tk.Button(self.root, bg='white', text='4b', command=lambda: self.makesmth(self.mybutton8))
        self.mybutton9 = tk.Button(self.root, bg='white', text='5b', command=lambda: self.makesmth(self.mybutton9))
        self.mybutton10 = tk.Button(self.root, bg='white', text='1c', command=lambda: self.makesmth(self.mybutton10))
        self.mybutton11 = tk.Button(self.root, bg='white', text='2c', command=lambda: self.makesmth(self.mybutton11))
        self.mybutton12 = tk.Button(self.root, bg='white', text='3c', command=lambda: self.makesmth(self.mybutton12))
        self.mybutton13 = tk.Button(self.root, bg='white', text='4c', command=lambda: self.makesmth(self.mybutton13))
        self.mybutton14 = tk.Button(self.root, bg='white', text='5c', command=lambda: self.makesmth(self.mybutton14))

        self.mybutton.grid(row=1, column=1, sticky='wens', padx=10, pady=10)
        self.mybutton1.grid(row=1, column=2, sticky='wens', padx=10, pady=10)
        self.mybutton2.grid(row=1, column=3, sticky='wens', padx=10, pady=10)
        self.mybutton3.grid(row=1, column=4, sticky='wens', padx=10, pady=10)
        self.mybutton4.grid(row=1, column=5, sticky='wens', padx=10, pady=10)
        self.mybutton5.grid(row=2, column=1, sticky='wens', padx=10, pady=10)
        self.mybutton6.grid(row=2, column=2, sticky='wens', padx=10, pady=10)
        self.mybutton7.grid(row=2, column=3, sticky='wens', padx=10, pady=10)
        self.mybutton8.grid(row=2, column=4, sticky='wens', padx=10, pady=10)
        self.mybutton9.grid(row=2, column=5, sticky='wens', padx=10, pady=10)
        self.mybutton10.grid(row=3, column=1, sticky='wens', padx=10, pady=10)
        self.mybutton11.grid(row=3, column=2, sticky='wens', padx=10, pady=10)
        self.mybutton12.grid(row=3, column=3, sticky='wens', padx=10, pady=10)
        self.mybutton13.grid(row=3, column=4, sticky='wens', padx=10, pady=10)
        self.mybutton14.grid(row=3, column=5, sticky='wens', padx=10, pady=10)


        self.root.grid_columnconfigure(0, minsize=50)
        self.root.grid_columnconfigure(1, minsize=50)
        self.root.grid_columnconfigure(2, minsize=50)
        self.root.grid_columnconfigure(3, minsize=50)
        self.root.grid_columnconfigure(4, minsize=50)
        self.root.grid_columnconfigure(5, minsize=50)
        self.root.grid_columnconfigure(6, minsize=50)
        self.root.grid_columnconfigure(7, minsize=50)
        self.root.grid_columnconfigure(8, minsize=50)
        self.root.grid_columnconfigure(9, minsize=50)
        self.root.grid_columnconfigure(10, minsize=50)
        self.root.grid_columnconfigure(11, minsize=50)
        self.root.grid_columnconfigure(12, minsize=50)
        self.root.grid_columnconfigure(13, minsize=50)
        self.root.grid_columnconfigure(14, minsize=50)

        self.root.grid_rowconfigure(0, minsize=30)
        self.root.grid_rowconfigure(1, minsize=30)
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(3, minsize=30)
        self.root.grid_rowconfigure(4, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30)
        self.root.grid_rowconfigure(6, minsize=30)
        self.root.grid_rowconfigure(7, minsize=30)
        self.root.grid_rowconfigure(8, minsize=30)
        self.root.grid_rowconfigure(9, minsize=30)
        self.root.grid_rowconfigure(10, minsize=30)
        self.root.grid_rowconfigure(11, minsize=30)
        self.root.grid_rowconfigure(12, minsize=30)
        self.root.grid_rowconfigure(13, minsize=30)
        self.root.grid_rowconfigure(14, minsize=30)

        self.root.mainloop()

    def makesmth(self, t):
        if t['bg'] == 'white':
            t['bg'] = 'red'
            b = Question(t)

        elif t['bg'] == 'red':
            t['bg'] = 'white'

gui = My_gui()


