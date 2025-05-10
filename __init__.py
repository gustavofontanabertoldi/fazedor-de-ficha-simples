import json
import os

class ficha_jogador:
    def __init__(self, nome, raca, aparencia, historia, habilidade, atributos):
        self.nome = nome
        self.raca = raca
        self.aparencia = aparencia
        self.historia = historia
        self.habilidade = habilidade
        self.atributos = atributos
    
    

    def para_dict(self):
        return {
            "nome": self.nome,
            "raca": self.raca,
            "aparencia": self.aparencia,
            "historia": self.historia,
            "habilidade": self.habilidade,
            "Atributos": self.atributos
        }
    
nome = input("Digite o nome do personagem: ")
raca = input("Digite a raça: ")
aparencia = input("Descreva a aparência: ")
historia = input("Conte um pouco da história: ")
habilidade = input("Descreva a habilidade especial: ")
os.system('cls' if os.name == 'nt' else 'clear')
print("Você tem 5 pontos para distribuir nos atributos.")

pontos_disponiveis = 5
atributos = {
            "forca": 0,
            "destreza": 0,
            "inteligencia": 0,
            "carisma": 0,
            "resistencia": 0
            }

for chave in atributos:
    while True:
        try:
            valor = int(input(f"Quantos pontos em {chave}? (Pontos restantes: {pontos_disponiveis}) "))
            if 0 <= valor <= pontos_disponiveis:
                atributos[chave] = valor
                pontos_disponiveis -= valor
            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número inteiro.")


personagem = ficha_jogador(nome, raca, aparencia, historia, habilidade, atributos)

os.system('cls' if os.name == 'nt' else 'clear')

with open(f"{nome}.json", "w", encoding="utf-8") as arquivo:
    json.dump(personagem.para_dict(), arquivo, indent=4, ensure_ascii= False)

print(f"Ficha salva com sucesso no arquivo: {nome}.json")