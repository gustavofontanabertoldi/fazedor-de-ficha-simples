import json
import os
import customtkinter as ctk
# -----------------------
ctk.set_appearance_mode("dark")

def open_window():
    new_win = ctk.CTkToplevel(app)
    new_win.title("Nova Ficha")
    new_win.geometry("500x400")
    label = ctk.CTkLabel(
        new_win,
        text="Nova ficha",
        font=("Arial", 18),
    )
    label.pack(pady=20)
    button_break = ctk.CTkButton(
        new_win,
        text="Fechar",
        command=new_win.destroy,
    )
    button_break.pack(pady=20)

app = ctk.CTk()
app.title("Criador de Fichas")
app.geometry("500x200")

campo_1 = ctk.CTkLabel(
    app,
    text="Olá, bem vindo ao criador de fichas!",
    font=("Arial", 25),
    corner_radius=10,
)
campo_1.pack(pady=20)
button_1 = ctk.CTkButton(app, text='Criar uma Ficha', command=open_window)
button_1.pack(pady=20, expand=True)

app.mainloop()

#------------------------
# class ficha_jogador:
#     def __init__(self, nome, raca, aparencia, historia, habilidade, atributos):
#         self.nome = nome
#         self.raca = raca
#         self.aparencia = aparencia
#         self.historia = historia
#         self.habilidade = habilidade
#         self.atributos = atributos
    
    

#     def para_dict(self):
#         return {
#             "nome": self.nome,
#             "raca": self.raca,
#             "aparencia": self.aparencia,
#             "historia": self.historia,
#             "habilidade": self.habilidade,
#             "Atributos": self.atributos
#         }
    
# nome = input("Digite o nome do personagem: ")
# raca = input("Digite a raça: ")
# aparencia = input("Descreva a aparência: ")
# historia = input("Conte um pouco da história: ")
# habilidade = input("Descreva a habilidade especial: ")
# os.system('cls' if os.name == 'nt' else 'clear')
# print("Você tem 5 pontos para distribuir nos atributos.")

# pontos_disponiveis = 5
# atributos = {
#             "forca": 0,
#             "destreza": 0,
#             "inteligencia": 0,
#             "carisma": 0,
#             "vontade": 0
#             }

# for chave in atributos:
#     try:
#         valor = int(input(f"Quantos pontos em {chave}? (Pontos restantes: {pontos_disponiveis}) "))
#         if 0 <= valor <= pontos_disponiveis:
#             atributos[chave] = valor
#             pontos_disponiveis -= valor
#         else:
#             print("Valor inválido. Tente novamente.")
#     except ValueError:
#         print("Por favor, digite um número inteiro.")


# personagem = ficha_jogador(nome, raca, aparencia, historia, habilidade, atributos)

# os.system('cls' if os.name == 'nt' else 'clear')

# with open(f"{nome}.json", "w", encoding="utf-8") as arquivo:
#     json.dump(personagem.para_dict(), arquivo, indent=4, ensure_ascii= False)

# print(f"Ficha salva com sucesso no arquivo: {nome}.json")
