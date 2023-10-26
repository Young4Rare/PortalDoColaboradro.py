import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    telefone = telefone_entry.get()
    numero_colaborador = numero_colaborador_entry.get()

    # Aqui você pode adicionar a lógica para salvar os dados em algum lugar (por exemplo, em um arquivo ou banco de dados).
    # Neste exemplo, apenas exibiremos os dados na tela.
    mensagem = f"Nome: {nome}\nCPF: {cpf}\nTelefone: {telefone}\nNúmero de Colaborador: {numero_colaborador}"
    messagebox.showinfo("Cadastro Realizado", mensagem)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Portal do colaborador")

# Rótulos e campos de entrada
nome_label = tk.Label(janela, text="Nome Completo:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

cpf_label = tk.Label(janela, text="CPF:")
cpf_label.pack()
cpf_entry = tk.Entry(janela)
cpf_entry.pack()

telefone_label = tk.Label(janela, text="Telefone:")
telefone_label.pack()
telefone_entry = tk.Entry(janela)
telefone_entry.pack()

numero_colaborador_label = tk.Label(janela, text="Número de Colaborador:")
numero_colaborador_label.pack()
numero_colaborador_entry = tk.Entry(janela)
numero_colaborador_entry.pack()

# Botão para cadastrar
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack()

# Iniciar a interface gráfica
janela.mainloop()
