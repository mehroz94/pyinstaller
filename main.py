import tkinter as tk
import sectionproperties.pre.library.primitive_sections as sections
import pint
import ezdxf
from jinja2 import Template
import ttkthemes

import xhtml2pdf

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def hello():
    t = Template("Hello {{ something }}!")
    t.render(something="World")
    test = sections.rectangular_section(d=500, b=300)
    print(test)
    ureg = pint.UnitRegistry()
    unit = 3 * ureg.meter + 4 * ureg.cm
    label1 = tk.Label(root, text=f'Hello World! {unit}', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)


button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()