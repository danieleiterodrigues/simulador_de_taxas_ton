# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# def calcular_valores_parcelas(valor_recebido, bandeira):
#     taxas = {
#         'Visa/Master': {
#             1: 0.0079,
#             2: 0.0399,
#             3: 0.0499,
#             4: 0.0599,
#             5: 0.0699,
#             6: 0.0699,
#             7: 0.0699,
#             8: 0.0699,
#             9: 0.0699,
#             10: 0.0699,
#             11: 0.0699,
#             12: 0.0699,
#         },
#         'Elo/Hipercard/Amex': {
#             1: 0.0434,
#             2: 0.0702,
#             3: 0.0758,
#             4: 0.0838,
#             5: 0.0938,
#             6: 0.1038,
#             7: 0.1098,
#             8: 0.1138,
#             9: 0.1238,
#             10: 0.1288,
#             11: 0.1374,
#             12: 0.1378,
#         }
#     }

#     if bandeira not in taxas:
#         return "Bandeira inválida."

#     valores_parcelas = {}
#     for parcelas, taxa in taxas[bandeira].items():
#         valor_original = valor_recebido / (1 - taxa)
#         valores_parcelas[parcelas] = round(valor_original, 2)

#     return valores_parcelas

# def exibir_resultados():
#     try:
#         valor_recebido = float(entry_valor_recebido.get())
#         bandeira = combo_bandeira.get()

#         if valor_recebido <= 0:
#             raise ValueError("O valor recebido deve ser positivo.")

#         resultados = calcular_valores_parcelas(valor_recebido, bandeira)

#         resultado_texto = ""
#         for parcelas, valor in resultados.items():
#             resultado_texto += f"{parcelas}x: R${valor:.2f}\n"

#         texto_resultado.config(state=tk.NORMAL)
#         texto_resultado.delete(1.0, tk.END)
#         texto_resultado.insert(tk.END, resultado_texto)
#         texto_resultado.config(state=tk.DISABLED)
#     except ValueError as e:
#         messagebox.showerror("Erro", str(e))

# # Configuração da janela principal
# root = tk.Tk()
# root.title("Simulador de Parcelamento")

# # Alterar o ícone da janela
# icon_path = './ton.png'
# try:
#     icon = tk.PhotoImage(file=icon_path)
#     root.iconphoto(True, icon)
# except tk.TclError:
#     print(f"Erro: Não foi possível carregar o ícone de {icon_path}")

# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# label_valor_recebido = tk.Label(frame, text="Valor (R$):")
# label_valor_recebido.grid(row=0, column=0, padx=5, pady=5)

# entry_valor_recebido = tk.Entry(frame)
# entry_valor_recebido.grid(row=0, column=1, padx=5, pady=5)

# label_bandeira = tk.Label(frame, text="Bandeira do Cartão:")
# label_bandeira.grid(row=1, column=0, padx=5, pady=5)

# combo_bandeira = tk.StringVar(frame)
# combo_bandeira.set("Escolha a bandeira")
# bandeiras = ["Visa/Master", "Elo/Hipercard/Amex"]
# dropdown_bandeira = tk.OptionMenu(frame, combo_bandeira, *bandeiras)
# dropdown_bandeira.grid(row=1, column=1, padx=5, pady=5)

# botao_calcular = tk.Button(frame, text="Calcular", command=exibir_resultados)
# botao_calcular.grid(row=2, columnspan=2, pady=10)

# label_resultado = tk.Label(root, text="Resultados:")
# label_resultado.pack(padx=10, pady=5)

# texto_resultado = tk.Text(root, height=12, width=40, state=tk.DISABLED)
# texto_resultado.pack(padx=30, pady=50)

# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def calcular_valores_parcelas(valor_recebido, bandeira):
    taxas = {
        'Visa/Master': {
            1: 0.0358,
            2: 0.0698,
            3: 0.0759,
            4: 0.0847,
            5: 0.0934,
            6: 0.1018,
            7: 0.1103,
            8: 0.1188,
            9: 0.1238,
            10: 0.1259,
            11: 0.1299,
            12: 0.1308,
        },
        'Elo/Hipercard/Amex': {
            1: 0.0477,
            2: 0.0837,
            3: 0.0898,
            4: 0.0986,
            5: 0.1073,
            6: 0.1157,
            7: 0.1242,
            8: 0.1327,
            9: 0.1377,
            10: 0.1398,
            11: 0.1438,
            12: 0.1447,
        }
    }

    if bandeira not in taxas:
        return "Bandeira inválida."

    valores_parcelas = {}
    for parcelas, taxa in taxas[bandeira].items():
        valor_original = valor_recebido / (1 - taxa)
        valor_parcela = valor_original / parcelas
        valores_parcelas[parcelas] = (
            round(valor_original, 2), round(valor_parcela, 2))

    return valores_parcelas


def exibir_resultados():
    try:
        valor_recebido = float(entry_valor_recebido.get())
        bandeira = combo_bandeira.get()

        if valor_recebido <= 0:
            raise ValueError("O valor recebido deve ser positivo.")

        resultados = calcular_valores_parcelas(valor_recebido, bandeira)

        resultado_texto = ""
        for parcelas, (valor_total, valor_parcela) in resultados.items():
            if parcelas == 1:
                resultado_texto += f"{parcelas}x: Total R${valor_total:.2f}\n"
            else:
                resultado_texto += f"{parcelas}x: Total R${valor_total:.2f}, Parcela R${valor_parcela:.2f}\n"

        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, resultado_texto)
        texto_resultado.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


root = tk.Tk()
root.title("Simulador de Parcelamento Ton")

icon_path = 'transp.ico'
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Erro: Não foi possível carregar o ícone de {icon_path}\n{e}")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_valor_recebido = tk.Label(frame, text="Valor (R$):")
label_valor_recebido.grid(row=0, column=0, padx=5, pady=5)

entry_valor_recebido = tk.Entry(frame)
entry_valor_recebido.grid(row=0, column=1, padx=5, pady=5)

label_bandeira = tk.Label(frame, text="Bandeira do Cartão:")
label_bandeira.grid(row=1, column=0, padx=5, pady=5)

combo_bandeira = tk.StringVar(frame)
combo_bandeira.set("Escolha a bandeira")
bandeiras = ["Visa/Master", "Elo/Hipercard/Amex"]
dropdown_bandeira = tk.OptionMenu(frame, combo_bandeira, *bandeiras)
dropdown_bandeira.grid(row=1, column=1, padx=5, pady=5)

botao_calcular = tk.Button(frame, text="Calcular", command=exibir_resultados)
botao_calcular.grid(row=2, columnspan=2, pady=10)

label_resultado = tk.Label(root, text="Resultados:")
label_resultado.pack(padx=10, pady=5)

texto_resultado = tk.Text(root, height=12, width=50, state=tk.DISABLED)
texto_resultado.pack(padx=30, pady=50)

root.mainloop()
