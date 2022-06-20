from tkinter import ttk
from tkinter import *

janela_principal = Tk()
janela_principal.title("JUROS DE CARTÃO")
janela_principal.geometry("360x370")
janela_principal.resizable(False, False)

lista_parcelas = ["1x em dinheiro", "1x no cartão", "2x no cartão", "3x no cartão",
                  "4x no cartão", "5x no cartão", "6x no cartão"]


def verifica_parcela():
    valor_digitado = int(textbox_valor.get())
    quantidade_parcelas = cb_parcelas.get()
    if quantidade_parcelas == "1x em dinheiro":
        total = valor_digitado - (valor_digitado * 10/100)
        lbl_resultado['text'] = (f"Esta compra À VISTA EM DINHEIRO \n passa a totalizar R${total:.2f}."
                                 f"\n 10% de desconto aplicado.")
    elif quantidade_parcelas == "1x no cartão":
        total = valor_digitado - (valor_digitado * 5/100)
        lbl_resultado['text'] = (f"Esta compra À VISTA NO CARTÃO \n passa a totalizar R${total:.2f}"
                                 f"\n 5% de deconto aplicado.")
    elif quantidade_parcelas == "2x no cartão":
        total = valor_digitado
        parcela = total / 2
        lbl_resultado['text'] = (f"Esta compra será parcelada \n 2x de R${parcela:.2f}"
                                 f"\n Sem juros")
    elif quantidade_parcelas == "3x no cartão":
        total = valor_digitado
        parcela = total / 3
        lbl_resultado['text'] = (f"Esta compra será parcelada \n 3x de R${parcela:.2f}"
                                 f"\n Sem juros.")
    elif quantidade_parcelas == "4x no cartão":
        total = valor_digitado
        parcela = total / 4
        lbl_resultado['text'] = (f"Esta compra será parcelada \n 4x de R${parcela:.2f}"
                                 f"\n Sem juros.")
    elif quantidade_parcelas == "5x no cartão":
        total = valor_digitado + (valor_digitado * 20/100)
        parcela = total / 5
        lbl_resultado['text'] = (f"Esta compra será parcelada \n 5x de R${parcela:.2f}"
                                 f"\n Com juros simples de 20%.")
    elif quantidade_parcelas == "6x no cartão":
        total = valor_digitado + (valor_digitado * 20 / 100)
        parcela = total / 6
        lbl_resultado['text'] = (f"Esta compra será parcelada \n 6x de R${parcela:.2f}"
                                 f"\n Com juros simples de 20%.")



def limpa_resultado():
    lbl_resultado['text'] = ""


lbl_inicial = Label(janela_principal, text="VERIFICADOR DE PARCELAS", font="Arial 18 bold", bd=10)
lbl_inicial.grid(row=0, columnspan=4)

lbl_valor = Label(janela_principal, text="Valor da compra:", font="Arial 10 bold", bd=10)
lbl_valor.grid(row=1, column=0)
textbox_valor = Entry(janela_principal, font="Arial 10")
textbox_valor.grid(row=1, column=1)

lbl_parcelas = Label(janela_principal, text="Quantidade de parcelas:", font="Arial 10 bold", bd=20)
lbl_parcelas.grid(row=2, column=0)
cb_parcelas = ttk.Combobox(janela_principal, value=lista_parcelas)
cb_parcelas.grid(row=2, column=1)

btn_calcular = Button(janela_principal, text="Verificar", command=verifica_parcela)
btn_calcular.grid(row=3, column=0)
btn_limpar = Button(janela_principal, text="Limpar", command=limpa_resultado)
btn_limpar.grid(row=3, column=1)

lbl_vazia = Label(janela_principal)
lbl_vazia.grid(row=4, column=0)

lbl_resultado = Label(janela_principal, text="", bg="dark blue", fg="white", width=30, height=5,
                      font="Arial 12 bold")
lbl_resultado.grid(row=5, columnspan=4)

lbl_vazia_2 = Label(janela_principal)
lbl_vazia_2.grid(row=6, column=0)

lbl_assinatura = Label(janela_principal, text="Desenvolvido por Marco Moraes", font="Arial 10 italic")
lbl_assinatura.grid(row=7, columnspan=4)

janela_principal.mainloop()