import csv
import pandas as pd
import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

filename = ''

def crearMatriz(n,m):
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz

def calcMayor(data):
    mayor = 0
    for tupla in data:
        if (int(tupla[0].strip()) > mayor):
            mayor = int(tupla[0].strip())
        if (int(tupla[1].strip()) > mayor):
            mayor = int(tupla[2].strip())
    return mayor

root = tk.Tk()
root.title('Generador de matriz')
root.resizable(False, False)
root.geometry('300x150')

def select_file():
    
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
    )
    global filename
    filename = fd.askopenfilename(
        title='Abrir archivo',
        initialdir='/',
        filetypes=filetypes)

open_button = ttk.Button(
    root,
    text='Abrir archivo',
    command=select_file
)

open_button.pack(expand=True)
root.mainloop()
root.quit()
    
with open(filename, newline = '') as data:                                                                                          
    df = csv.reader(data, delimiter='\t')
    data = list(df)
    data.pop(0)
n = calcMayor(data)
matrix = crearMatriz(n,n)
for tupla in data:
    f = int(tupla[0].strip())
    c = int(tupla[1].strip())
    value = tupla[2].strip()
    matrix[c-1][f-1] = value
df = pd.DataFrame(matrix).T
df.index += 1
df.columns += 1
name = os.path.basename(filename)
name += '.xlsx'
df.to_excel(excel_writer=name)