import json
import os
import customtkinter as ctk
from abc import ABC, abstractmethod
# -----------------------
import customtkinter as ctk

import customtkinter as ctk

import customtkinter as ctk

class JanelaFicha(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ficha RPG")
        self.geometry("800x600")
        self.build_widgets()

    def build_widgets(self):
        # Configuração do grid principal
        self.grid_rowconfigure(0, weight=1)   # conteúdo
        self.grid_rowconfigure(1, weight=0)   # botões embaixo
        self.grid_columnconfigure(0, weight=0)  # menu lateral
        self.grid_columnconfigure(1, weight=1)  # conteúdo principal

        # --- MENU LATERAL (como no exemplo)
        frame_menu = ctk.CTkFrame(self, fg_color="gray20", corner_radius=10)
        frame_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        # btn_nome = ctk.CTkButton(frame_menu, text="Nome")
        # btn_nome.pack(pady=10, padx=10)

        # btn_historia = ctk.CTkButton(frame_menu, text="História")
        # btn_historia.pack(pady=10, padx=10)

        # btn_atributos = ctk.CTkButton(frame_menu, text="Atributos")
        # btn_atributos.pack(pady=10, padx=10)

        # --- ÁREA PRINCIPAL
        frame_main = ctk.CTkFrame(self, fg_color="gray25", corner_radius=10)
        frame_main.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # dividir a área principal em grid
        frame_main.grid_rowconfigure(0, weight=0)  # título
        frame_main.grid_rowconfigure(1, weight=1)  # formulário
        frame_main.grid_columnconfigure(0, weight=1)

        label_title = ctk.CTkLabel(frame_main, text="Nova Ficha", font=("Arial", 20))
        label_title.grid(row=0, column=0, pady=10)

        # Sub-frame com campos
        frame_form = ctk.CTkFrame(frame_main, fg_color="gray30", corner_radius=10)
        frame_form.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Campos dentro do formulário
        label_nome = ctk.CTkLabel(frame_form, text="Nome:")
        label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_nome = ctk.CTkEntry(frame_form, placeholder_text="Digite o nome")
        entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        label_idade = ctk.CTkLabel(frame_form, text="Idade:")
        label_idade.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_idade = ctk.CTkEntry(frame_form, placeholder_text="Digite a idade")
        entry_idade.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        label_historia = ctk.CTkLabel(frame_form, text="História:")
        label_historia.grid(row=2, column=0, padx=5, pady=5, sticky="ne")
        textbox_historia = ctk.CTkTextbox(frame_form, width=300, height=150)
        textbox_historia.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        # Deixar a coluna 1 expandir
        frame_form.grid_columnconfigure(1, weight=1)
        frame_form.grid_rowconfigure(2, weight=1)

        # --- BOTÕES EMBAIXO
        frame_bottom = ctk.CTkFrame(self, fg_color="gray20", corner_radius=10)
        frame_bottom.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        btn_salvar = ctk.CTkButton(frame_bottom, text="Salvar")
        btn_salvar.pack(side="right", padx=10, pady=5)

        btn_cancelar = ctk.CTkButton(frame_bottom, text="Cancelar")
        btn_cancelar.pack(side="right", padx=10, pady=5)

# Teste rápido
if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("900x700")

    btn_open = ctk.CTkButton(app, text="Abrir Ficha", command=lambda: JanelaFicha(app))
    btn_open.pack(pady=20)

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
