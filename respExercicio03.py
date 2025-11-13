class professor():
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def apresentar(self):
        return f"Professor {self.nome}, Disciplina: {self.disciplina}"
        