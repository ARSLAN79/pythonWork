
#!/usr/bin/env python

from Tkinter import *
import Pmw, sys

filename = "index.htm"
root = Tk()            
top = Frame(root); top.pack(side='top', expand=True, fill='both')
text = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='file %s' % filename,
       text_width=40, 
       text_height=4,
       text_wrap='none', 
       )
text.grid(column=0, row=0, sticky='news')
top.rowconfigure(0, weight=1)
top.columnconfigure(0, weight=1)

text.insert('end', open(filename,'r').read())
Button(top, text='Quit', command=root.destroy).grid(column=0, row=1, pady=15)
root.mainloop()