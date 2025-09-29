import json
import os
import customtkinter as ctk
from abc import ABC, abstractmethod
# -----------------------

class BaseJanela(ctk.CTkToplevel, ABC):
    def __init__(self, master, title = "Janela", size = "500x300"):
        super().__init__(master)
        self.title = title
        self.geometry(size)
        self.build_widget()
    
    @abstractmethod
    def build_widget(self):
        ''' Cada classe deve construir seus próprios widgets :)'''
        pass

class new_record(BaseJanela):
    def build_widget(self):
        label = ctk.CTkLabel(self, text="Nova Ficha", font=("Arial", 20))
        label.pack(pady=20)

        botao = ctk.CTkButton(self, text="Fechar", command=self.destroy)
        botao.pack(pady=20)

class JanelaConfig(BaseJanela):
    def build_widget(self):
        label = ctk.CTkLabel(self, text="Configurações", font=("Arial", 18))
        label.pack(pady=20)

        check = ctk.CTkCheckBox(self, text="Ativar modo caótico")
        check.pack(pady=10)

app = ctk.CTk()
app.title("Criador de Fichas")
app.geometry("550x300")

campo_1 = ctk.CTkLabel(app, text="Bem-vindo!", font=("Arial", 25))
campo_1.pack(pady=20)

btn1 = ctk.CTkButton(app, text="Abrir Ficha", command=lambda: new_record(app, "Ficha"))
btn1.pack(pady=10)

btn2 = ctk.CTkButton(app, text="Abrir Config", command=lambda: JanelaConfig(app, "Config"))
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
