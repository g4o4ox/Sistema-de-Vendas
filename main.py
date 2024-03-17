
from tkinter import *
from tkinter import messagebox
import data
#interfaces

def main():
    main=Tk()
    main.title('Sistema de Vendas')
    main.resizable(True,False)
    main.geometry('990x650')
    #elementos da tela
    label=Label(main,text='Pagina de venda',font='poppins 21',fg='blue').place(y='0',x='0')
    search=Entry(main,width='60').place(y='43',x='505')
    #lista de produtos:
    def add_product():
        
        def insert_product():
            Preco=pric.get()
            nome=nam.get()
            data.cursor.execute('''
                        INSERT INTO produtos (nome,valor) VALUES(?,?)       
                                ''',(nome,Preco))
            
            data.conn.commit()
            messagebox.showinfo(title='Status',message='Produto adicionado com sucesso')
            add.destroy()
        
        add=Tk()
        add.resizable(False,False)
        add.geometry('140x280')
        lab=Label(add,text='Adicionar Produto').pack()
        nam=Entry(add)
        nam.pack()
        pric=Entry(add)
        pric.pack()
        bttn=Button(add,text='Adicionar',command=lambda:insert_product()).pack()
    
    
        
    
    listbox=Listbox(main,width=40,height=15,).place(y='60',x='10')
    listbox=Listbox(main,width=60,height=25).place(y='70',x='505')
        
    #botões
    button1=Button(main,text='Adicionar',bg='green',command=lambda:add_product()).place(x='0',y='620')
    button2=Button(main,text='Remover',bg='red').place(x='87',y='620')
    button3=Button(main,text='Sair',bg='darkred',command=lambda:quit()).place(x='168',y='620')
    
    main.mainloop()

def login():
    login=Tk()
    login.title('Login')
    login.resizable(False,False)
    login.geometry('470x350')
    
    #elementos da tela
    label=Label(login,text='Sistema de Vendas',font='poppins 32').pack()
    label=Label(login,text='Username').place(y='150',x='70')
    label=Label(login,text='Password').place(y='190',x='70')
    user_entry=Entry(login)
    user_entry.place(y='150',x='150')
    pswd_entry=Entry(login,show='*')
    pswd_entry.place(y='190',x='150')
    
    #conexão com o banco de dados
    def RegisterDatabase():
        
        User=user_entry.get()
        Password=pswd_entry.get()
        
        data.cursor.execute('''
INSERT INTO users(user,pwd) VALUES(?, ?) 
                            ''',(User,Password))
        
        if not User and not Password:
            messagebox.showerror('Erro de login','Campos vazios não são aceitos')
            return
        
        data.conn.commit()
        
        messagebox.showinfo(title='Login',message='Cadastro Concluido!!!')
        
    def LoginDatabase():
        
        User=user_entry.get()
        Password=pswd_entry.get()
        
        data.cursor.execute('''
SELECT * FROM users 
WHERE (user= ? AND pwd= ?)
                            ''',(User,Password))
        
        VeryfiLogin=data.cursor.fetchone()
        try:
            if(User in VeryfiLogin and Password in VeryfiLogin):
                messagebox.showinfo(title='Login',message='Login bem sucedido')
                login.destroy()
                main()
               
        except:
                messagebox.showerror('Login Error','Login não encontrado tente se cadastrar.')

    #
    button=Button(login,text='Login',bg='green',command=LoginDatabase).place(y='230',x='150')
    #button=Button(login,text='Register',bg='#a7d6d5',command=RegisterDatabase).place(y='230',x='230')
    login.mainloop()

main()