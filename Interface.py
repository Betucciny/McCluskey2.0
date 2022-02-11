from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, messagebox
from Funciones import tam, execute


window = Tk()
window.title("Reducciones booleanas")


nbits= 0
valores= []
selected = ''
total = 0
generalnums = []

def getbits():
    global table, nbits,total,generalnums
    generalnums.clear()
    table.destroy()
    nbits = int(spinbox_var.get())
    total = tam(nbits, generalnums)
    lista = ['1']
    for i in range(nbits):
        lista.append(str(i+2))
    lista.append(str(nbits+2))
    table = ttk.Treeview(window, columns=lista, show= 'headings')
    scroll = ttk.Scrollbar(window, orient='vertical', command=table.yview)
    table.config(yscrollcommand=scroll.set)
    table.heading(1, text='Numero')
    table.column(1, minwidth=0 ,width= 100,anchor='c')
    for i in range(nbits):
        char = 65
        table.heading(i+2, text= chr(char+i))
        table.column(i+2, minwidth=0 , width= 20,anchor='c')
    table.heading(nbits+2, text= 'Estado')
    table.column(nbits+2, minwidth=0 , width= 100,anchor='c')
    table.grid_remove()
    table.tag_configure('oddrow',background="white")
    table.tag_configure('evenrow', background="lightblue")
    table.grid(row=2, column=4, columnspan=3, rowspan=5,sticky=N+S+E+W)
    scroll.grid(row=2,column=7,rowspan=5,sticky=N+S)
    count=0
    for i in generalnums:
        entry = [count]
        for j in i:
            entry.append(j)
        entry.append(2)
        if count % 2:
            table.insert('', 'end', values=entry,tags= 'oddrow')
        else:
            table.insert('', 'end', values=entry, tags= 'evenrow')
        count+=1


def getcont():
    global total,table
    content = str(text_table.get("1.0",END))
    if content == '':
        return
    cont = content.replace('\n',' ').replace(',',' ').split()
    for i in cont:
        if i.isnumeric():
            i = int(i)
            if i == 0 or i == 1 or i == 2:
                continue
        messagebox.showinfo("Error","Valores invalidos")
        return
    for i, line in zip(cont,table.get_children()):
        contenido = list(table.item(line, 'values'))
        contenido.pop()
        contenido.append(i)
        final = tuple(contenido)
        table.item(line,text='',values=final)


def select():
    global nbits, valores,selected
    text_num.config(state=NORMAL)
    text_var.config(state=NORMAL)
    text_num.delete(0,'end')
    text_var.delete(0,'end')
    selected= table.focus()
    valores = table.item(selected, 'values')
    out = ""
    for i in range(nbits):
        out=out + valores[i+1]
    text_num.insert(0, valores[0])
    text_var.insert(0, out)
    text_num.config(state=DISABLED)
    text_var.config(state=DISABLED)

def modif():
     global valores,table,selected
     selected = table.focus()
     valores = table.item(selected, 'values')
     valores = list(valores)
     valores.pop()
     valores.append(spinbox_state.get())
     valores = tuple(valores)
     table.item(selected, text='', values=valores)

def clear():
    text_table.delete('1.0', END)


def start():
    global nbits, generalnums,table
    nums=[]
    for line in table.get_children():
        contenido = list(table.item(line, 'values'))
        nums.append(contenido[nbits+1])
    final = execute(nbits,nums,generalnums)


    text_ans.config(state=NORMAL)
    text_ans.delete(0,'end')
    if final == '':
        text_ans.insert(0, 'No hay reduccion')
    else:
        text_ans.insert(0,final)
    text_ans.config(state=DISABLED)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                foreground='black',
                rowheight=25,
                font=("Helvetica", 10))
style.configure("Treeview.Heading", font=("Helvetica", 14))


label_title = Label(window, text = "Reducciones Booleanas", font=("Helvetica", 20))
label_space1 = Label(window, text= "       ")
label_space2 = Label(window, text= "       ")
label_space3 = Label(window, text= "       ")
label_space4 = Label(window, text= "       ")
label_space5 = Label(window, text= "       ")
label_space6 = Label(window, text= "       ")
label_space7 = Label(window, text= "       ")
label_space8 = Label(window, text= "       ")
label_var = Label(window, text = "Introduzca el numero de variables: ", font=("Helvetica", 14))
spinbox_var = Spinbox(window, from_= 2, to= 20, font=("Helvetica", 12),width=5,state='readonly')
button_var = Button(window, text= "Crear tabla", font=("Helvetica", 12), padx=50, command=getbits)
label_table = Label(window, text = "Entrada de tabla entera: ", font=("Helvetica",12))
text_table = ScrolledText(window, width=40, font=("Helvetica",11))
button_insert = Button(window, text= "Insertar datos", font= ("Helvetica", 12), command=getcont)
button_clear = Button(window, text= "Limpiar", font= ("Helvetica", 12), command=clear)
frame = Frame(window, background='white',width=300)
table = ttk.Treeview(window,columns='',show='headings')
label_num = Label(window, text= "Numero:", font=("Helvetica", 14))
label_tvar = Label(window, text= "Variable:", font=("Helvetica", 14))
label_est = Label(window, text= "Estado:", font=("Helvetica", 14))
text_num = Entry(window, state=DISABLED, width= 10, font= ("Helvetica", 16))
text_var = Entry(window, state=DISABLED, width= 10, font= ("Helvetica", 16))
spinbox_state = Spinbox(window, from_=0, to= 2, font=("Helvetica", 12),width=5,state='readonly')
button_sel = Button(window, text="Seleccionar", font= ("Helvetica", 11), padx= 15, command=select)
button_put = Button(window, text="Ingresar", font= ("Helvetica", 11), padx= 15,command=modif)
button_start = Button(window, text= "Generar reduccion booleana", font=("Helvetica", 12), padx=50, command=start)
name = Label(window, text= 'Roberto Ángel Herrera Rodríguez        Contacto: herrerarr08@gmail.com')
end = Label(window, text= 'Cualquier duda o comentario favor de mandar correo')

text_ans= Entry(window, state=DISABLED, width= 60, font= ("Helvetica", 20))
scroll_ans= Scrollbar(window, orient='horizontal', command=text_ans.xview)
text_ans.config(xscrollcommand=scroll_ans.set)


label_title.grid(row=0, column=1, columnspan=7)
label_space1.grid(row=0, column=0)
label_space2.grid(row=1, column=0)
label_space3.grid(row=1, column=3)
label_space4.grid(row=0, column=8)
label_space5.grid(row=7, column=0)
label_space6.grid(row=11, column=0)
label_space7.grid(row=13, column=0)
label_space8.grid(row=16, column=0)
label_var.grid(row=2, column=1)
spinbox_var.grid(row=2, column=2)
button_var.grid(row=3, column=1, columnspan=2)
label_table.grid(row=5, column=1, columnspan=2,sticky=W)
text_table.grid(row=6, column=1, columnspan=2, rowspan=6,sticky=N+S+E+W)
button_clear.grid(row=12, column=1,sticky=W)
button_insert.grid(row=12, column=2,sticky=E)
frame.grid(row=2, column=4, columnspan=4, rowspan=5,sticky=N+W+S+E)
label_num.grid(row=8, column=4, sticky=W)
label_tvar.grid(row=8, column=5, sticky=W)
label_est.grid(row=8, column=6, columnspan=2, sticky=W)
text_num.grid(row=9, column=4)
text_var.grid(row=9, column=5,sticky=E+W)
spinbox_state.grid(row=9, column=6, columnspan=2)
button_sel.grid(row=10,column=4, sticky=W)
button_put.grid(row=10, column=6,sticky=E)
button_start.grid(row=12, column=4, columnspan=4)
scroll_ans.grid(row=15, column=1, columnspan=7, sticky=E+W)
text_ans.grid(row=14, column=1, columnspan=7, sticky=E+W)
name.grid(row=17,column=0,columnspan=9,sticky=N)
end.grid(row=18,column=0,columnspan=9,sticky=N)
window.columnconfigure(5, weight=1)
window.rowconfigure(6,weight=1)

window.mainloop()