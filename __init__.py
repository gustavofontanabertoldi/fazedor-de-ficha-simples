import json

class ficha_jogador:
    def __init__(self, nome, raca, aparencia, historia, habilidade):
        self.nome = nome
        self.raca = raca
        self.aparencia = aparencia
        self.historia = historia
        self.habilidade = habilidade

    def para_dict(self):
        return {
            "nome": self.nome,
            "raca": self.raca,
            "aparencia": self.aparencia,
            "historia": self.historia,
            "habilidade": self.habilidade
        }
    
nome = input("Digite o nome do personagem: ")
raca = input("Digite a raça: ")
aparencia = input("Descreva a aparência: ")
historia = input("Conte um pouco da história: ")
habilidade = input("Descreva a habilidade especial: ")

personagem = ficha_jogador(nome, raca, aparencia, historia, habilidade)

with open(f"{nome}.json", "w", encoding="utf-8") as arquivo:
    json.dump(personagem.para_dict(), arquivo, indent=4, ensure_ascii= False)

print(f"Ficha salva com sucesso no arquivo: {nome}.json")