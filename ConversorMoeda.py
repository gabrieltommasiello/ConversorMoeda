import tkinter as tk
from moeda import apiDolar

def dolar():
    cotacao = float(apiDolar())
    reais = float(valor.get())
    conta = round(reais / cotacao,2)
    mensagem = f'Com R${reais:.2f} reais, compra-se ${conta} dólares'
    resposta.config(text=mensagem)
    # return mensagem


janela = tk.Tk()
janela.geometry('350x300')
janela.title('Aula 04 - Tkinter')
janela.configure(bg='#267365')

titulo = tk.Label(janela, text='Conversor de Reais para Dólar', font=('Times New Roman', 16), fg='#F29F05', bg='#267365')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digite valor em Reais para Converter', font=('Times New Roman', 12), fg='#F29F05', bg='#267365')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#D6D58E', fg='#005C53')
valor.pack(pady=10)

botao = tk.Button(janela, text='CONVERTER', command=dolar, bg='#F2CB05', fg='#267365')
botao.pack(pady=10)

resposta = tk.Label(janela, text='', font=('Times New Roman', 12), fg='#F29F05', bg='#267365')
resposta.pack(pady=10)

####################


janela.mainloop()