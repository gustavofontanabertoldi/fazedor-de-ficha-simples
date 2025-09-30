import json
import os
import customtkinter as ctk
from abc import ABC, abstractmethod
# -----------------------
import customtkinter as ctk

import customtkinter as ctk

class JanelaFicha(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ficha")
        self.geometry("600x600")
        self.build_widgets()

    def build_widgets(self):
        # Configura o grid da janela
        self.grid_rowconfigure(0, weight=0)   # label
        self.grid_rowconfigure(1, weight=1)   # frame_1
        self.grid_rowconfigure(2, weight=1)   # frame_2
        self.grid_rowconfigure(3, weight=1)   # frame_3
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        label = ctk.CTkLabel(self, text="Nova Ficha", font=("Arial", 20))
        label.grid(row=0, column=1, pady=20)

        frame_1 = ctk.CTkFrame(self, corner_radius=5, fg_color="gray30")
        frame_1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        frame_2 = ctk.CTkFrame(self, corner_radius=5, fg_color="gray30")
        frame_2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        frame_3 = ctk.CTkFrame(self, corner_radius=5, fg_color="gray30")
        frame_3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        label_frame_1_nome = ctk.CTkLabel(frame_1, text="Nome do personagem:", fg_color='gray', corner_radius=5)
        entry_frame_1_nome = ctk.CTkEntry(frame_1, placeholder_text="Digite aqui o nome")
        label_frame_1_nome.pack(pady=10)
        entry_frame_1_nome.pack()
        label_frame_2_nome = ctk.CTkLabel(frame_1, text="Idade do personagem:", fg_color='gray', corner_radius=5)
        entry_frame_2_nome = ctk.CTkEntry(frame_1, placeholder_text="Digite aqui a idade")
        label_frame_2_nome.pack(pady=10)
        entry_frame_2_nome.pack()


class JanelaConfig(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Configurações")
        self.geometry("400x300")
        self.build_widgets()

    def build_widgets(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text="Configurações", font=("Arial", 18))
        label.grid(row=0, column=0, pady=20)

        check = ctk.CTkCheckBox(self, text="Ativar modo caótico")
        check.grid(row=1, column=0, pady=10)


# Janela principal
app = ctk.CTk()
app.title("Criador de Fichas")
app.geometry("600x400")

# Configurar grid principal
app.grid_rowconfigure(0, weight=0)   # topo
app.grid_rowconfigure(1, weight=1)   # meio
app.grid_rowconfigure(2, weight=0)   # botões
app.grid_columnconfigure(0, weight=1)

frame_top = ctk.CTkFrame(app, corner_radius=10, fg_color="gray20")
frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_bottom = ctk.CTkFrame(app, corner_radius=10, fg_color="gray30")
frame_bottom.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

label_1 = ctk.CTkLabel(frame_top, text="Bem Vindo!", font=("Arial", 20))
label_1.pack(pady=20)  # aqui pode usar pack porque está DENTRO do frame_top, não na mesma hierarquia

btn1 = ctk.CTkButton(frame_bottom, text="Abrir Ficha", command=lambda: JanelaFicha())
btn1.pack(pady=10)

btn2 = ctk.CTkButton(frame_bottom, text="Abrir Config", command=lambda: JanelaConfig())
btn2.pack(pady=10)

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
