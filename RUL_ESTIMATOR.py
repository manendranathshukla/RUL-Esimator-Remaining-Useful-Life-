import tkinter as tk
import pandas as pd
import numpy as np
from pandas import DataFrame
import utils
import featuretools as ft

from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
root.title("RUL SIMULATOR")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))



canvas1 = tk.Canvas(root, width = 300, height = 110, bg = 'lightsteelblue2', relief = 'raised')
canvas1.place(x=1220,y=800,anchor=tk.SW)
widget = tk.Label(canvas1, text=' Developed BY: ', fg='white', bg='black')
widget.pack()
canvas1.create_window(50, 25, window=widget)

kcsir = tk.Label(canvas1, text='DR.G.R.Kanagachidambarasen', fg='black')
kcsir.pack()
canvas1.create_window(180, 55, window=kcsir)


sis = tk.Label(canvas1, text=' Shreya Kumari ', fg='black')
sis.pack()
canvas1.create_window(145, 75, window=sis)


sis = tk.Label(canvas1, text=' Manendra Nath Shukla ', fg='black')
sis.pack()
canvas1.create_window(140, 90, window=sis)






def getCSV():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    grph(df)




def onestep():
    pass


def stop():
    pass



def laststep():
    pass



def rul():
    window=tk.Toplevel(root)
    data = utils.load_data('train_FD004.txt')
    cutoff_times = utils.make_cutoff_times(data)

    s=cutoff_times.head(20)
    tk.Label(window,text=s).pack()




browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
browseButton_CSV.pack(side=tk.LEFT)



OneStep = tk.Button(text=" One step ",command=onestep,bg='blue', fg='white', font=('helvetica', 12, 'bold'))
OneStep.place(x=750,y=700, anchor=tk.NW)


Stop = tk.Button(text="     Reset    ", command=stop, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
Stop.place(x=650,y=700, anchor=tk.NW)


LastStep = tk.Button(text=" Last Step ", command=laststep, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
LastStep.place(x=850,y=700, anchor=tk.NW)


Status=tk.Label(text="STATUS: ", bg='white', fg='black',font=('helvetica', 12, 'bold'))
Status.place(x=30,y=600,anchor=tk.NW)

Title=tk.Label(text="            RUL    SIMULATOR          ", bg='red', fg='white',font=('helvetica', 15, 'bold'))
Title.place(x=950,y=50,anchor=tk.NE)




RUL=tk.Button(text="   RUL:   ", bg='white', fg='black',font=('helvetica', 14, 'bold'),command=rul)
RUL.place(x=100,y=500,anchor=tk.NE)



def grph(df):
    figure3 = plt.Figure(figsize=(8, 6), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df['RUL'], df['sensor_1'], color='g')
    scatter3 = FigureCanvasTkAgg(figure3, root)
    scatter3.get_tk_widget().place(x=800, y=390, anchor=tk.CENTER)
    ax3.legend()
    ax3.set_xlabel('No Of Cycles')
    ax3.set_title('Sensor Value Vs RUL')



figure3 = plt.Figure(figsize=(8, 6), dpi=100)
ax3 = figure3.add_subplot(111)
#ax3.scatter(df['RUL'], df['sensor_1'], color='g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().place(x=800, y=390, anchor=tk.CENTER)
ax3.legend()
ax3.set_xlabel('No Of Cycles')
ax3.set_title('Sensor Value Vs RUL')


root.mainloop()