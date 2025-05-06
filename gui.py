import tkinter as tk
from tkinter import messagebox
from database import criar_tabela, inserir_nota, listar_notas

def cadastrar():
    numero = entry_numero.get()
    fornecedor = entry_fornecedor.get()
    data = entry_data.get()
    valor = entry_valor.get()

    if numero and fornecedor and data and valor:
        inserir_nota(numero, fornecedor, data, float(valor))
        messagebox.showinfo("Sucesso", "Nota cadastrada com sucesso!")
        atualizar_lista()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def atualizar_lista():
    lista.delete(0, tk.END)
    for nota in listar_notas():
        lista.insert(tk.END, f"Nº {nota[1]} | {nota[2]} | {nota[3]} | R$ {nota[4]:.2f}")

def iniciar_interface():
    global entry_numero, entry_fornecedor, entry_data, entry_valor, lista

    criar_tabela()

    janela = tk.Tk()
    janela.title("Gerenciador de Notas Fiscais")

    tk.Label(janela, text="Número da Nota").grid(row=0, column=0)
    entry_numero = tk.Entry(janela)
    entry_numero.grid(row=0, column=1)

    tk.Label(janela, text="Fornecedor").grid(row=1, column=0)
    entry_fornecedor = tk.Entry(janela)
    entry_fornecedor.grid(row=1, column=1)

    tk.Label(janela, text="Data").grid(row=2, column=0)
    entry_data = tk.Entry(janela)
    entry_data.grid(row=2, column=1)

    tk.Label(janela, text="Valor").grid(row=3, column=0)
    entry_valor = tk.Entry(janela)
    entry_valor.grid(row=3, column=1)

    tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=4, columnspan=2)

    lista = tk.Listbox(janela, width=50)
    lista.grid(row=5, columnspan=2)

    atualizar_lista()
    janela.mainloop()
