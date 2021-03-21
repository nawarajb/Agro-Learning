from Tkinter import *
import tkMessageBox
import pandas as pd

from linear_para import calc,diff
from time import asctime
from product import crop_data_extraction


def check():
    n1 = int(mon.get())
    x1 = int(yea.get())
    if (n1>=9):
        x = x1-56
        n = n1+4-12
        
    else:
        n = n1+4
        x = x1-57
        
    try:
        int(n) and int(x)
    except ValueError:
        tkMessageBox.showinfo('Productivity','You entered a invalid month or year')
    else:
        n = int(n)
        x = int(x)
        if(n<13 and x<2020):
            df = pd.read_csv('Weather_data_KTM.csv', parse_dates=['Date AD'], index_col='Date AD')

            df = df[['Avg Temp', 'Rainfall' ]]

            df['year'] = df.index.year
            df['month'] = df.index.month


            df_counts = df.groupby(['month', 'year']).mean()
            temp = []
            rain = []
            a = 2*n-2
            b = 2*n-1
            tot1 = list(df_counts.iloc[a])
            tot2 = list(df_counts.iloc[b])
            temp = [tot1[0],tot2[0]]
            rain = [tot1[1],tot2[1]]
            year = [2012,2013]
            m1,c1 = calc(year,temp)
            m2,c2 = calc(year,rain)
            y1 = m1*x+c1
            y2 = m2*x+c2
            dat = crop_data_extraction()
            
            val = str('The crop which increases your Productivity is ')
            li_crop = list(set(diff(dat,y1,y2)))
            for i in range(len(li_crop)-1):
                val += li_crop[i]+' or '
            val += li_crop[i+1]
            tkMessageBox.showinfo('Productivity',val)
        else:
            strng = "Month or year not in range"
            tkMessageBox.showinfo('Productivity',strng)

a = Tk()
a.title("Productivity Evaluation")
a.geometry("450x300+200+200")

labelText = StringVar()
labelText.set("Enter which month?\neg. : 1 for Baishakh")
label1 = Label(a,textvariable = labelText, height = 5).pack()

month = IntVar()
mon = Entry(a, textvariable = month)
mon.pack()

labelText = StringVar()
labelText.set("Enter which Year?\nEnter in BS")
label2 = Label(a,textvariable = labelText).pack()

year = IntVar()
yea = Entry(a, textvariable = year)
yea.pack()

butn = Button(a,text = "Submit",width = 18, command = check).pack(side = 'bottom',padx =15,pady=15)

a.mainloop()
