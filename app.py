import json
import os
import customtkinter as ctk

# -------------------------
# MODELO (dados da ficha)
# -------------------------
class FichaJogador:
    def __init__(self, nome="", idade="", historia="", atributos=None):
        self.nome = nome
        self.idade = idade
        self.historia = historia
        self.atributos = atributos or {
            "Força": 0,
            "Destreza": 0,
            "Inteligência": 0,
            "Carisma": 0,
            "Vontade": 0,
        }

    def para_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "historia": self.historia,
            "atributos": self.atributos,
        }

    @classmethod
    def de_dict(cls, data):
        return cls(
            nome=data.get("nome", ""),
            idade=data.get("idade", ""),
            historia=data.get("historia", ""),
            atributos=data.get("atributos", {}),
        )

# -------------------------
# SERVIÇOS (salvar/carregar)
# -------------------------
class FichaService:
    @staticmethod
    def salvar(ficha: FichaJogador, pasta="fichas"):
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, f"{ficha.nome}.json")
        with open(caminho, "w", encoding="utf-8") as arq:
            json.dump(ficha.para_dict(), arq, indent=4, ensure_ascii=False)
        return caminho

    @staticmethod
    def carregar(caminho: str) -> FichaJogador:
        with open(caminho, "r", encoding="utf-8") as arq:
            data = json.load(arq)
        return FichaJogador.de_dict(data)

# -------------------------
# INTERFACE (Tkinter)
# -------------------------
class JanelaFicha(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ficha RPG")
        self.geometry("800x600")

        self.entry_nome = None
        self.entry_idade = None
        self.textbox_historia = None
        self.entries_atributos = {}

        self.build_widgets()

    def build_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # MENU LATERAL
        frame_menu = ctk.CTkFrame(self, fg_color="gray20", corner_radius=10)
        frame_menu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        side_label = ctk.CTkLabel(frame_menu, text="Atributos", font=("Arial", 18))
        side_label.pack(pady=10)

        for atributo in ["Força", "Destreza", "Inteligência", "Carisma", "Vontade"]:
            row = ctk.CTkFrame(frame_menu, fg_color="gray25")
            row.pack(fill="x", padx=5, pady=2)
            lbl = ctk.CTkLabel(row, text=atributo, width=80, anchor="w")
            lbl.pack(side="left", padx=5)
            entry = ctk.CTkEntry(row, width=40)
            entry.insert(0, "0")
            entry.pack(side="right", padx=5)
            self.entries_atributos[atributo] = entry

        # ÁREA PRINCIPAL
        frame_main = ctk.CTkFrame(self, fg_color="gray25", corner_radius=10)
        frame_main.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        label_title = ctk.CTkLabel(frame_main, text="Nova Ficha", font=("Arial", 20))
        label_title.pack(pady=10)

        # FORMULÁRIO
        frame_form = ctk.CTkFrame(frame_main, fg_color="gray30", corner_radius=10)
        frame_form.pack(fill="both", expand=True, padx=20, pady=10)

        self.entry_nome = self._add_field(frame_form, "Nome:", 0)
        self.entry_idade = self._add_field(frame_form, "Idade:", 1)

        lbl_hist = ctk.CTkLabel(frame_form, text="História:")
        lbl_hist.grid(row=2, column=0, padx=5, pady=5, sticky="ne")
        self.textbox_historia = ctk.CTkTextbox(frame_form, width=300, height=150)
        self.textbox_historia.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        frame_form.grid_columnconfigure(1, weight=1)
        frame_form.grid_rowconfigure(2, weight=1)

        # BOTÕES
        frame_bottom = ctk.CTkFrame(self, fg_color="gray20", corner_radius=10)
        frame_bottom.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        btn_salvar = ctk.CTkButton(frame_bottom, text="Salvar", command=self.salvar_ficha)
        btn_salvar.pack(side="right", padx=10, pady=5)

        btn_cancelar = ctk.CTkButton(frame_bottom, text="Cancelar", command=self.destroy)
        btn_cancelar.pack(side="right", padx=10, pady=5)

    def _add_field(self, master, label, row):
        lbl = ctk.CTkLabel(master, text=label)
        lbl.grid(row=row, column=0, padx=5, pady=5, sticky="e")
        entry = ctk.CTkEntry(master)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky="we")
        return entry

    def salvar_ficha(self):
        atributos = {k: int(v.get() or 0) for k, v in self.entries_atributos.items()}
        ficha = FichaJogador(
            nome=self.entry_nome.get(),
            idade=self.entry_idade.get(),
            historia=self.textbox_historia.get("1.0", "end").strip(),
            atributos=atributos
        )
        caminho = FichaService.salvar(ficha)
        print(f"Ficha salva em: {caminho}")

# -------------------------
# APP PRINCIPAL
# -------------------------
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.geometry("400x200")

    label = ctk.CTkLabel(app, text="Bem Vindo!", font=("Arial", 20))
    label.pack(pady=20)

    btn_open = ctk.CTkButton(app, text="Abrir Ficha", command=lambda: JanelaFicha(app))
    btn_open.pack(pady=20)

    app.mainloop()
