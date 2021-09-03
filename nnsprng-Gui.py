try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
import nnsprng_model as spring


def l1(event):
    l1.sec=lattice1.get(lattice1.curselection())
def l2(event):
    l2.sec=lattice2.get(lattice2.curselection())
def l3(event):
    l3.sec=lattice3.get(lattice3.curselection())
def l4(event):
    l4.sec=lattice4.get(lattice4.curselection())
def l5(event):
    l5.sec=lattice5.get(lattice5.curselection())
    
def send():
    latticel=[]
    conf=[]

    isim=E1.get()
    a=float(a1.get())
    R=float(R1.get())
    r=float(r1.get())
    p=float(p1.get())
    N=int(n1.get())

    if a==1 and r==1:
        pass
    else:
        lttc=l1.sec
        conf=[isim,lttc,a,R,r,p,N]
        latticel.append(conf)        

    ###############
    isim=E2.get()
    a=float(a2.get())   
    r=float(r2.get())
    
    if a==1 and r==1:
        pass
    else:
        lttc=l2.sec
        conf=[isim,lttc,a,R,r,p,N]
        latticel.append(conf)
    ##    
    isim=E3.get()
    a=float(a3.get())   
    r=float(r3.get())
    
    if a==1 and r==1:
        pass
    else:
        lttc=l3.sec
        conf=[isim,lttc,a,R,r,p,N]
        latticel.append(conf)
    ##
    isim=E4.get()
    a=float(a4.get())   
    r=float(r4.get())
    
    if a==1 and r==1:
        pass
    else:
        lttc=l4.sec
        conf=[isim,lttc,a,R,r,p,N]
        latticel.append(conf)
    ##
    isim=E5.get()
    a=float(a5.get())   
    r=float(r5.get())
    
    if a==1 and r==1:
        pass
    else:
        lttc=l5.sec
        conf=[isim,lttc,a,R,r,p,N]
        latticel.append(conf)

        

    print(latticel)


    spring.nanospring(len(latticel),latticel)
    
mainWindow = tkinter.Tk()

mainWindow.title("Nanoyay Modelleme v0.12")
mainWindow.geometry('900x400')



leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=0, column=0)
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=0, column=1, sticky='n')
label = tkinter.Label(rightFrame, text="Kristal Yapısı")
label.grid(row=0, column=0)

lattice1=tkinter.Listbox(rightFrame,selectmode='single',exportselection=0,height=2)

lattice1.insert(1,"sc")
lattice1.insert(2,"bcc")
lattice1.insert(3,"fcc")
lattice1.insert(4,"diamond")
lattice1.grid(row=0,column=1)
scrollbar1 = tkinter.Scrollbar(rightFrame, orient="vertical")
scrollbar1.config(command=lattice1.yview)
scrollbar1.grid(row=0, column=2)
lattice1.config(yscrollcommand = scrollbar1.set)
lattice1.bind("<<ListboxSelect>>",l1)  
##
lattice2=tkinter.Listbox(rightFrame,selectmode='single',exportselection=0,height=2)
lattice2.insert(1,"sc")
lattice2.insert(2,"bcc")
lattice2.insert(3,"fcc")
lattice2.insert(4,"diamond")
lattice2.grid(row=0,column=3)
scrollbar2 = tkinter.Scrollbar(rightFrame, orient="vertical")
scrollbar2.config(command=lattice2.yview)
scrollbar2.grid(row=0, column=4)
lattice2.config(yscrollcommand = scrollbar2.set)
lattice2.bind("<<ListboxSelect>>",l2)  
##
lattice3=tkinter.Listbox(rightFrame,selectmode='single',exportselection=0,height=2)
lattice3.insert(1,"sc")
lattice3.insert(2,"bcc")
lattice3.insert(3,"fcc")
lattice3.insert(4,"diamond")
lattice3.grid(row=0,column=5)
scrollbar3 = tkinter.Scrollbar(rightFrame, orient="vertical")
scrollbar3.config(command=lattice3.yview)
scrollbar3.grid(row=0, column=6)
lattice3.config(yscrollcommand = scrollbar3.set)
lattice3.bind("<<ListboxSelect>>",l3)
##
lattice4=tkinter.Listbox(rightFrame,selectmode='single',exportselection=0,height=2)
lattice4.insert(1,"sc")
lattice4.insert(2,"bcc")
lattice4.insert(3,"fcc")
lattice4.insert(4,"diamond")
lattice4.grid(row=0,column=7)
scrollbar4 = tkinter.Scrollbar(rightFrame, orient="vertical")
scrollbar4.config(command=lattice4.yview)
scrollbar4.grid(row=0, column=8)
lattice4.config(yscrollcommand = scrollbar4.set)
lattice4.bind("<<ListboxSelect>>",l4)
##
lattice5=tkinter.Listbox(rightFrame,selectmode='single',exportselection=0,height=2)
lattice5.insert(1,"sc")
lattice5.insert(2,"bcc")
lattice5.insert(3,"fcc")
lattice5.insert(4,"diamond")
lattice5.grid(row=0,column=9)
scrollbar5 = tkinter.Scrollbar(rightFrame, orient="vertical")
scrollbar5.config(command=lattice5.yview)
scrollbar5.grid(row=0, column=10)
lattice5.config(yscrollcommand = scrollbar5.set)
lattice5.bind("<<ListboxSelect>>",l5) 



#♠canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
#canvas.grid(row=1, column=0)


##button1 = tkinter.Button(rightFrame, text="button1")
##button2 = tkinter.Button(rightFrame, text="button2")
##button3 = tkinter.Button(rightFrame, text="button3")
var = tkinter.StringVar()
var.set(0)
L1 = tkinter.Label(rightFrame, text="Element kısaltması")
E1 = tkinter.Entry(rightFrame, bd =5)
E1.insert(0,'Cu')
E2 = tkinter.Entry(rightFrame, bd =5)
E2.insert(0,'Cu')
E3 = tkinter.Entry(rightFrame, bd =5)
E3.insert(0,'Cu')
E4 = tkinter.Entry(rightFrame, bd =5)
E4.insert(0,'Cu')
E5 = tkinter.Entry(rightFrame, bd =5)
E5.insert(0,'Cu')

L2 = tkinter.Label(rightFrame, text="a lattice uzunluğu")
a1 = tkinter.Entry(rightFrame, bd =5)
a1.insert(0,1.0)
a2 = tkinter.Entry(rightFrame, bd =5)
a2.insert(0,1.0)
a3 = tkinter.Entry(rightFrame, bd =5)
a3.insert(0,1.0)
a4 = tkinter.Entry(rightFrame, bd =5)
a4.insert(0,1.0)
a5 = tkinter.Entry(rightFrame, bd =5)
a5.insert(0,1.0)

L3 = tkinter.Label(rightFrame, text="R Yayın Yarıçap   ")
R1 = tkinter.Entry(rightFrame, bd =5)
R1.insert(0,1.0)
xR=float(R1.get())
R2 = tkinter.Entry(rightFrame, bd =5)
#R2.delete(0)
#R2.insert(0,xR)

L4 = tkinter.Label(rightFrame, text="r Yayın Yarıçapı  ")
r1 = tkinter.Entry(rightFrame, bd =5)
r1.insert(0,1.0)
r2 = tkinter.Entry(rightFrame, bd =5)
r2.insert(0,1.0)
r3 = tkinter.Entry(rightFrame, bd =5)
r3.insert(0,1.0)
r4 = tkinter.Entry(rightFrame, bd =5)
r4.insert(0,1.0)
r5 = tkinter.Entry(rightFrame, bd =5)
r5.insert(0,1.0)

L5 = tkinter.Label(rightFrame, text="P Yayın Aralığı   ")
p1 = tkinter.Entry(rightFrame, bd =5)
p1.insert(0,1.0)
#p2 = tkinter.Entry(rightFrame, bd =5)
#p2.insert(0,1.0)

L6 = tkinter.Label(rightFrame, text="N Dönme Sayısı    ")
n1 = tkinter.Entry(rightFrame, bd =5)
n1.insert(0,1)
#n2 = tkinter.Entry(rightFrame, bd =5)
#n2.insert(0,1)

isim=E1.get()
##
##a=a1.get()
##R=R1.get()
##r=r1.get()
##p=p1.get()
##N=n1.get()

button1 = tkinter.Button(rightFrame, text="Oluştur",command=send)
L1.grid(row=1, column=0)
E1.grid(row=1, column=1)
E2.grid(row=1, column=3)
E3.grid(row=1, column=5)
E4.grid(row=1, column=7)
E5.grid(row=1, column=9)

L2.grid(row=2, column=0)
a1.grid(row=2, column=1)
a2.grid(row=2, column=3)
a3.grid(row=2, column=5)
a4.grid(row=2, column=7)
a5.grid(row=2, column=9)

L3.grid(row=3, column=0)
R1.grid(row=3, column=1)

L4.grid(row=4, column=0)
r1.grid(row=4, column=1)
r2.grid(row=4, column=3)
r3.grid(row=4, column=5)
r4.grid(row=4, column=7)
r5.grid(row=4, column=9)


L5.grid(row=5, column=0)
p1.grid(row=5, column=1)

L6.grid(row=6, column=0)
n1.grid(row=6, column=1)

button1.grid(row=9,column=4)



# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)
mainWindow.grid_columnconfigure(3, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=2)

mainWindow.mainloop()
