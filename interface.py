from tkinter import *
from tkinter import ttk
root = Tk()

root.title("ProdPrediction")

root.geometry("700x600")
root.minsize(400,300)

root.configure(bg="#a9e4ef")
Title = Label(root,text="Product Predictor",font=("Times New Roman",20,"bold"))
Title.grid(row = 0, column=3)
Date_l = Label(root,text="Date",font=("Arial",17),bg="#a9e4ef")
Date_l.grid(row = 1, column = 0, sticky = W, pady = 4)
Date = Entry(root,justify = CENTER,font=('Arial', 12))
Date.grid(row = 1, column = 1, sticky = W, pady = 4)
City_l = Label(root,text="City",font=("Arial",17),bg="#a9e4ef")
City_l.grid(row = 2, column = 0, sticky = W, pady = 4)
City = Entry(root,justify = CENTER,font=('Arial', 12))
City.grid(row = 2, column = 1, sticky = W, pady = 4)
State_l = Label(root,text="State",font=("Arial",17),bg="#a9e4ef")
State_l.grid(row = 3, column = 0, sticky = W, pady = 4)
State = Entry(root,justify = CENTER,font=('Arial', 12))
State.grid(row = 3, column = 1, sticky = W, pady = 4)
Type_l = Label(root,text="Type",font=("Arial",17),bg="#a9e4ef")
Type_l.grid(row = 4, column = 0, sticky = W, pady = 4)
Type = Entry(root,justify = CENTER,font=('Arial', 12))
Type.grid(row = 4, column = 1, sticky = W, pady = 4)
Cluster_l = Label(root,text="Cluster",font=("Arial",17),bg="#a9e4ef")
Cluster_l.grid(row = 5, column = 0, sticky = W, pady = 4)
Cluster = Entry(root,justify = CENTER,font=('Arial', 12))
Cluster.grid(row = 5, column = 1, sticky = W, pady = 4)

value_inside = StringVar(root)
value_inside.set("Internaional")
TH_l = Label(root,text="Type_of_Holliday",font=("Arial",17),bg="#a9e4ef")
TH_l.grid(row = 6, column = 0, sticky = W, pady = 4)
Hollidays_list= ['International', 'Local']
Type_of_Holliday = OptionMenu(root, value_inside, *Hollidays_list)
Type_of_Holliday.grid(row = 6, column = 1, sticky = W, pady = 4)
if (Type_of_Holliday =='Local') :
    LOCHOL_l = Label(root,text="Local_holliday_name",font=("Arial",17),bg="#a9e4ef")
    LOCHOL_l.grid(row = 7, column = 0, sticky = W, pady = 4)
    Local_holliday_name = Entry(root,justify = CENTER,font=('Arial', 12))
    Local_holliday_name.grid(row = 7, column = 1, sticky = W, pady = 4)


Button_P = Button(text="Predict" ,font=22,bg='lightgreen',
    command=lambda:lb1.config(text='plus2net',bg='lightblue'))
Button_P.grid(row = 7, column = 3, sticky = W, pady = 4)
OilP_l = Label(root,text="Oil Price",font=("Arial",17),bg="#a9e4ef")
OilP_l.grid(row = 8, column = 0, sticky = W, pady = 4)

root.mainloop()