import datetime
import time
import re
import os

alunos = []
cpfs = []
matriculas = []
emails = []
materias = [[], [], [], []]
ultimaModificacao = time.strftime("%d/%m/%Y %H:%M", time.localtime(os.path.getmtime(__file__)))
cursos = ["TIPI", "ADM", "MA", "EDF"]

class NovoAluno:
    def __init__(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade
    def setCpf(self, cpf):
        self.cpf = cpf
    def setEmail(self, email):
        self.email = email
    def setCurso(self, curso):
        self.curso = curso
    def setMatricula(self, matricula):
        self.matricula = matricula
    def setNotas(self, notas):
        self.notas = notas
        notas = []


def painelProfessor():
    while True:
        opcao = str(input("\
        \n├ Digite 1 ⇒  Cadastrar matérias\
        \n├ Digite 2 ⇒  Cadastrar aluno\
        \n├ Digite 3 ⇒  Editar um aluno\
        \n├ Digite 4 ⇒  Buscar um aluno\
        \n├ Digite 5 ⇒  Lista de alunos\
        \n├ Digite 6 ⇒  Voltar\
        \n├ Opção: "))
        if opcao == "1":
            editarMaterias()
        elif opcao == "2":
            cadastrarAluno()
        elif opcao == "3":
            painelEditarAluno()
        elif opcao == "4":
            pesquisarAluno()
        elif opcao == "5":
            listaAlunos()
        elif opcao == "6":
            break
        else:
            print("├ ERRO: Digite um NÚMERO válido.\n")
            
def creditos():
    print(f"\n┌───────── Créditos ──────────\
        \n├ Autor: Miguel Migliorelli Bringhenti\
        \n├ Data de início: 19/12/2022 00:21\
        \n├ Última modificação: {ultimaModificacao}")
    
def fechar():
    print("Saindo...")
    quit()
    
def editarMaterias():
    while True:
        curso = input("├ Curso a ser editado: ")
        if curso not in cursos:
            print("├ ERRO: Digite um CURSO válido.\n")
        else:
            break
    while True:
        quantidadeMaterias = input("├ Quantidade de materias a serem cadastradas: ")
        if quantidadeMaterias.isdigit() == False:
            print("├ ERRO: Digite um NÚMERO válido.\n")
        else:
            quantidadeMaterias = int(quantidadeMaterias)
            break
    cursoIndex = cursos.index(curso)
    if len(materias[cursoIndex]) == 0:
        print("├ O curso não possui matérias cadastradas.")
    else:
        print(f"├ Matérias disponíveis para o curso {curso}:")
        for i in range(len(materias[cursoIndex])):
            print(f"├ {i+1}ª Matéria: {materias[cursoIndex][i]}")
    print(f"├ Cadastrando {quantidadeMaterias} matérias no curso {curso}:")
    for i in range(quantidadeMaterias):
        materia = input(f"├ {i+1}ª Matéria: ")
        materias[cursoIndex].append(str(materia))
    print()

def cadastrarAluno():
    global nome, idade, cpf, email, curso, matricula
    print("\n┌────────── Cadastrar Aluno ──────────")
    nome = input("├ Nome do aluno: ")
    while verificarNome(nome) == False:
        nome = input("├ Nome do aluno: ")
    alunos.append(nome)
    idade = input("├ Data de nascimento do aluno (DD/MM/AAAA): ")
    while verificarIdade(idade) == False:
        idade = input("├ Data de nascimento do aluno (DD/MM/AAAA): ")
    cpf = input("├ CPF do aluno: ")
    while verificarCpf(cpf) == False:
        cpf = input("├ CPF do aluno: ")
    cpfs.append(cpf)
    email = input("├ E-mail do aluno: ")
    while verificarEmail(email) == False:
        cpf = input("├ E-mail do aluno: ")
    emails.append(email)
    curso = input("├ Curso do aluno: ")
    while verificarCurso(curso) == False:
        curso = input("├ Curso do aluno: ")
    matricula = input("├ Matricula do aluno: ")
    while verificarMatricula(matricula) == False:
        matricula = input("├ Matrícula do aluno: ")
    matriculas.append(matricula)
    
    alunos[-1] = NovoAluno(nome)
    alunos[-1].setIdade(idade)
    alunos[-1].setCpf(cpf)
    alunos[-1].setEmail(email)
    alunos[-1].setCurso(curso)
    alunos[-1].setMatricula(matricula)
    
    cursoIndex = cursos.index(curso)
    materiaIndex = materias[cursoIndex]
    notasAluno = []
    print("\n┌────────── Cadastrar Notas do Aluno ──────────")
    for i in range(len(materiaIndex)):
        nota = input(f"├ Nota ⇒ {materiaIndex[i]}: ")
        while verificarNota(nota) == False:
            nota = input(f"├ [ERRO] Nota inválida.\n├ Nota ⇒ {materiaIndex[i]}: ")
        notinha = f"{situacaoNota} ⇒  {materiaIndex[i]}: {nota}"
        notasAluno.append(notinha)
    print(f"Notas: {notasAluno} Index: {materiaIndex}")
    alunos[-1].setNotas(notasAluno)
    
    print(f"\n┌──────────── Cadastro de {nome} ────────────\
        \n├ Nome               ⇒  {alunos[-1].nome}\
        \n├ Data de Nascimento ⇒  {alunos[-1].idade}\
        \n├ CPF                ⇒  {alunos[-1].cpf}\
        \n├ E-mail             ⇒  {alunos[-1].email}\
        \n├ Curso              ⇒  {alunos[-1].curso}\
        \n├ Matrícula          ⇒  {alunos[-1].matricula}")
    print(f"\n┌──────────── Notas de {nome} ────────────")
    for i in range(len(materiaIndex)):
        print(f"├ {alunos[-1].notas[i]}")

def pesquisarAluno():
    print("\n┌─────────────── Buscar Aluno ───────────────")
    alunoPesquisa = input("├ Digite a matrícula do aluno: ")
    while True:
        if alunoPesquisa in alunos:
            alunoIndex = alunos.index(alunoPesquisa)
            break
        if alunoPesquisa in matriculas:
            alunoIndex = matriculas.index(alunoPesquisa)
            break
        alunoPesquisa = input("├ ERRO: Matrícula não encontrada.\n├ Digite a matrícula do aluno: ")
        
    curso = alunoPesquisa[re.sub(r'[0-9]+', '', alunoPesquisa)]
    cursoIndex = cursos.index(curso)
    materiaIndex = materias[cursoIndex]
    
    print(f"\n┌─────────────── Cadastro de {alunos[alunoIndex].nome} ───────────────\
        \n├ Nome               ⇒  {alunos[alunoIndex].nome}\
        \n├ Data de Nascimento ⇒  {alunos[alunoIndex].idade}\
        \n├ CPF                ⇒  {alunos[alunoIndex].cpf}\
        \n├ E-mail             ⇒  {alunos[alunoIndex].email}\
        \n├ Curso              ⇒  {alunos[alunoIndex].curso}\
        \n├ Matrícula          ⇒  {alunos[alunoIndex].matricula}")
    print(f"\n┌──────────── Notas de {alunos[alunoIndex].nome} ────────────")
    for i in range(len(materiaIndex)):
        print(f"├ {alunos[alunoIndex].notas[i]}")

def listaAlunos():
    if len(alunos) == 0:
        print("┌───────── Nenhum aluno cadastrado ───────")
    else:
        for i in range(len(alunos)):
            print("\n┌────────────────── Alunos ───────────────────")
            for i in range (len(alunos)):
                print(f"├ Matrícula: {alunos[i].matricula} ⇒  Aluno: {alunos[i].nome}")

def painelEditarAluno():
    while True:
        opcao = str(input("\n┌─────────────── Editar um ALuno ───────────────\
            \n├ Digite 1 ⇒ Editar informações\
            \n├ Digite 2 ⇒ Editar notas\
            \n├ Digite 3 ⇒ Voltar\
            \n├ Opção: "))
        if opcao == "1":
            editarAluno()
        elif opcao == "2":
            print("FALTA FAZER => editarNotas()")
        elif opcao == "3":
            break
        else:
            print("├ ERRO: Digite um NÚMERO válido.\n")
    
def editarAluno():
    print("\n┌─────────────── Editar Aluno ───────────────")
    alunoPesquisa = input("├ Digite a matrícula do aluno: ")
    while (alunoPesquisa in alunos or alunoPesquisa in matriculas) == False:
        alunoPesquisa = input("├ ERRO: Matrícula não encontrada.\n├ Digite a matrícula do aluno: ")

    if alunoPesquisa in alunos:
        indexAluno = alunos.index(alunoPesquisa)
    if alunoPesquisa in matriculas:
        indexAluno = matriculas.index(alunoPesquisa)

    nome = input("├ Novo nome do aluno: ")
    while verificarNome(nome) == False:
        nome = input("├ Novo nome do aluno: ")
    alunos[indexAluno]= nome
    idade = input("├ Nova data de nascimento do aluno (DD/MM/AAAA): ")
    while verificarIdade(idade) == False:
        idade = input("├ Nova data de nascimento do aluno (DD/MM/AAAA): ")
    cpf = input("├ Novo CPF do aluno: ")
    while verificarCpf(cpf) == False:
        cpf = input("├ Novo CPF do aluno: ")
    cpfs[indexAluno] = cpf
    email = input("├ Novo e-mail do aluno: ")
    while verificarEmail(email) == False:
        email = input("├ Novo e-mail do aluno: ")
    emails[indexAluno] = email
    
    curso = alunoPesquisa[re.sub(r"[0-9]+", "", alunoPesquisa)]
    matricula = alunoPesquisa
    
    alunos[indexAluno] = NovoAluno(nome)
    alunos[indexAluno].setIdade(idade)
    alunos[indexAluno].setCpf(cpf)
    alunos[indexAluno].setEmail(email)
    alunos[indexAluno].setCurso(curso)
    alunos[indexAluno].setMatricula(matricula)
    
    print(f"\n┌─────────────── Novas informações de {nome} ───────────────\
        \n├ Nome               ⇒  {alunos[indexAluno].nome}\
        \n├ Data de Nascimento ⇒  {alunos[indexAluno].idade}\
        \n├ CPF                ⇒  {alunos[indexAluno].cpf}\
        \n├ E-mail             ⇒  {alunos[indexAluno].email}\
        \n├ Curso              ⇒  {alunos[indexAluno].curso}\
        \n├ Matrícula          ⇒  {alunos[indexAluno].matricula}")


def verificarNota(nota):
    global situacaoNota
    if not nota.isnumeric():
        print("├ ERRO: Nota inválida.")
        return False
    if int(nota) > 100 or int(nota) < 0:
        print("├ ERRO: Nota inválida.")
    if int(nota) >= 60:
        situacaoNota = "├ Aprovado             "
    if int(nota) == 100:
        situacaoNota = "├ Aprovado c/ distinção"
    if int(nota) < 60:
        situacaoNota = "├ Reprovado            "

def verificarNome(nome):
    nomeErro = "\"'!@#$%¨&*()-_=+§/?/´°<,>.:;^~}]º{[ª´`│\¹²³£¢¬§/?°ªº₢°\""
    if any(map(str.isdigit, nome)) == True:
        print("├ [ERRO] Nome só pode conter letras e espaços.")
        return False
    if any(c in nomeErro for c in nome):
        print("├ [ERRO] Nome só pode conter letras e espaços.")
        return False
    if len(nome) <= 3:
        print("├ [ERRO] Nome deve conter mais que 3 caracteres.")
        return False
    if nome in alunos:
        print("├ [ERRO] Nome já cadastrado.")
        return False

def verificarIdade(idade):
    anoAtual = int(datetime.date.today().year)
    if len(idade) != 10:
        print("├ [ERRO] Formatação incorreta.")
        return False
    dia = idade[:2]
    mes = idade[3:5]
    ano = idade[-4::]
    if "/" in ano or "/" in mes or "/" in dia:
        print("├ [ERRO] Formatação incorreta.")
        return False
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        print("├ [ERRO] Data não pode conter letras.")
        return False
    if int(ano) < (anoAtual - 22) or int(ano) > (anoAtual - 15):
        print(f"├ [ERRO] Ano inválido.")
        return False
    if int(mes) > 12 or int(mes) < 0:
        print("├ [ERRO] Mês inválido.")
        return False
    if int(dia) > 31 or  int(dia) < 0:
        print("├ [ERRO] Dia inválido.")
        return False

def verificarCpf(cpf):
    cpf = [int(char) for char in cpf if char.isdigit()]
    if len(cpf) != 11:
        print("├ [ERRO] CPF inválido.")
        return False
    if cpf == cpf[::-1]:
        print("├ [ERRO] CPF inválido.")
        return False
    if cpf in cpfs:
        print("├ [ERRO] CPF já cadastrado.")
        return False

def verificarEmail(email):
    if not("@" in email and ".com" in email):
        print("├ [ERRO] E-mail inválido.")
        return False
    if email in emails:
        print("├ [ERRO] E-mail já cadastrado.")
        return False

def verificarCurso(curso):
    if curso not in cursos:
        print("├ [ERRO] Curso inválido")
        return False

def verificarMatricula(matricula):
    if curso == "TIPI":
        if len(matricula) != 13:
            print("├ [ERRO] Matrícula inválida.")
            return False
        if not(matricula[-4::].isnumeric()):
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula[5:9] != "TIPI":
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula in matriculas:
            print("├ [ERRO] Matrícula já cadastrada.")
            return False
    elif curso == "ADM" or curso == "EDF":
        if len(matricula) != 12:
            print("├ [ERRO] Matrícula inválida.")
            return False
        if not(matricula[-4::].isnumeric()):
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula[5:8] != "ADM" or matricula[5:8] != "EDF":
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula in matriculas:
            print("├ [ERRO] Matrícula já cadastrada.")
            return False
    else:
        if len(matricula) != 11:
            print("├ [ERRO] Matrícula inválida.")
            return False
        if not(matricula[-4::].isnumeric()):
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula[5:7] != "MA":
            print("├ [ERRO] Matrícula inválida.")
            return False
        if matricula in matriculas:
            print("├ [ERRO] Matrícula já cadastrada.")
            return False

while True:
    opcao = str(input("\n┌─────────────── Setup - Acadêmico com Classes ───────────────\
        \n├ Digite 1 ⇒  Painel do Professor\
        \n├ Digite 2 ⇒  Créditos\
        \n├ Digite 3 ⇒  Fechar programa\
        \n├ Opção: "))
    if opcao == "1":
        painelProfessor()
    elif opcao == "2":
        creditos()
    elif opcao == "3":
        fechar()
    else:
        print("├ ERRO: Digite um NÚMERO válido.\n")


'''
O que falta fazer:

⇒ Configurar o sistema de notas{
    ⇒ cadastro de notas
    ⇒ edição de notas
    ⇒ Tenta adicionar a edição de matérias e exclusão de notas das excluidas
}
'''