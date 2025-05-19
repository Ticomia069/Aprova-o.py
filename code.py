class aluno_de_escola: # classe
    def __init__(self, nome, nota, frequencia):
        self.nome = nome
        self.nota = nota
        self.frequencia = frequencia

    def verificar_aprovacao(self):
        if self.nota >= 7 and self.frequencia >= 0.75:
            print(f"{self.nome} foi aprovado!")
        else:
            print(f"{self.nome} foi reprovado!")
            print(f"Nota: {self.nota}")
            print(f"Frequencia: {self.frequencia}%")  # printa a frequencia com o simbolo de porcentagem

    def ler_nota(self):
        nota = int(input("Digite a nota do aluno: "))
        self.nota = nota
        return nota

    def ler_frequencia(self):
        frequencia = float(input("Digite a frequencia do aluno: "))
        self.frequencia = frequencia
        return frequencia
        # printa a frequencia com o simbolo de porcentagem

    def ler_nome(self):
        nome = input("Digite o nome do aluno: ")
        self.nome = nome
        return nome
        # printa o nome do aluno

def main():
    aluno = aluno_de_escola("", 0, 0)
    aluno.ler_nome()
    aluno.ler_nota()
    aluno.ler_frequencia()
    aluno.verificar_aprovacao()

if __name__ == "__main__":
    main()
