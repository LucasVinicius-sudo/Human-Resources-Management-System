import sys


def create_profile(nome,idade,data_nascimento,genero,numero_celular,id_numero,data_admissao,posicao,local_trabalho,salario,conta_bancaria):#Gerenciamento de Perfis do usuário

    f = open("file.txt", "a")
    f.write("Perfil de Funcionário: \n")
    f.write("-------------------------\n")
    f.write("Nome: " + nome + "\n")#lines[2]
    f.write("Idade: " + str(idade) + "\n")#lines[3]
    f.write("Data de nascimento: " + data_nascimento + "\n")#lines[4]
    f.write("Genero: " + genero + "\n")#lines[5]
    f.write("Celuar: "+ numero_celular + "\n")#lines[6]
    f.write("ID: " + id_numero + "\n")#lines[7]
    f.write("Departamento: " + data_admissao + "\n")#lines[8]
    f.write("Posição : " + posicao + "\n")#lines[9]
    f.write("Local de Trabalho: "+ local_trabalho + "\n")#lines[10]
    f.write("Salario :" +  str(salario) + "Reais" + "\n")#lines[11]
    f.write("Conta Bancaria: " + conta_bancaria + "\n")#lines[12]

    f.close()

def edit_profile():#Não está pronto ainda
    f = open("file.txt", "r")
    lines = f.readlines()
    change = input("Qual mudança deseja fazer?  ")
    if(change == 'Nome'):
        lines[2] = "João"

    elif(change == 'Idade'):
        print("here2")
    elif(change == 'Nascimento'):
        print("here3")
    elif(change == 'Genero'):
        print("here4")
    elif(change == 'Celular'):
        print("here5")
    elif(change == 'ID'):
        print("here6")
    elif(change == 'Departamento'):
        print("here7")
    elif(change == 'Posicao'):
        print("posicao")
    elif(change == 'Local'):
        print("Local Trabalho ")
    elif(change == 'Salario'):
        print("Salario do Funcionário")
    elif(change == 'Conta'):
        print("Conta")

    f.close()

def attendence_time(entrada,presenca,saida):
    f = open("time.txt", "a")
    f.write("Presença: " +presenca +"\n")
    f.write("Horario entrada:" +entrada +"\n")
    f.write("Horário de Saida" +saida + "\n")

    f.close()


def payroll_processing(salario):
    mes = int(input("Qual o mes que está sendo pago esse salãrop?"))
    if(mes == 12):
        print("Será pago o 13ª" + 2*salario)
    elif(mes != 12 and mes < 12):
        print("Será pago o salário Normal" + str(salario))


def recruitment():
    f = open("postings.txt" , "a")
    warnings = input("Caso há vagas para essa empresa escrever e questões similares?")
    print(warnings)

def evalution(desempenho):
    f = open("evalution.txt" , "a")
    f.write("O Desempenho do funcionário foi:" +desempenho)
    f.close()

def leave_management():
    motivo = input("Caso tenha motivo para pedir licença ou similares :")
    f = open("license.txt", "a")
    f.write("Gostaria de solicitar formalmente uma licença no período de 30 dias, por motivos que explicarei mais a frente Durante minha ausência, estou comprometido(a) a garantir uma transição suave das minhas responsabilidades, disponibilizando documentação necessária e orientando meus colegas, se necessário. Estou ciente da importância do meu papel na equipe e asseguro que farei todos os esforços para minimizar qualquer impacto decorrente da minha ausência. Agradeço antecipadamente pela sua compreensão e estou à disposição para discutir quaisquer detalhes adicionais ou providenciar alternativas para garantir a continuidade das atividades da equipe.Atenciosamente,mais especificamente pelo motivo de " +motivo)
    f.close()

def compliance():
    motivo = input("Foi infrijido alguma regra ou lei de compliance e semelhantes? ")
    f = open("compliance.txt", "a")
    f.write("Uma regra ou foi quebrada pelo motivo de" +motivo)
    f.close()

def main():
    nome = input("Qual seu Nome:")
    idade = int(input("Qual sua idade:"))
    data_nascimento = input("Qual sua data de Nascimento:")
    genero = input("Qual seu genero:")
    numero_celular = input("Qual seu numero:")
    id_numero = input("ID de Número de Identificação: ")
    departamento = input("Qual o departamento: ")
    data_admissao = input("Qual a sua data de admissão: ")
    posicao = input("Qual seu posição na empresa: ")
    local_trabalho = input("Qual seu local trabalho(Presencial - Remoto): ")
    salario = int(input("Qual seu salario em Reais: "))
    conta_bancaria = input("Qual o número da conta: ")
    create_profile(nome,idade,data_nascimento,genero,numero_celular,id_numero,data_admissao,posicao,local_trabalho,salario,conta_bancaria)
    #edit_profile()
    presenca = input("Confirma Presença(Negado ou Confirmado)")
    entrada = input("Horário no formato xx-xx-xx de entrada")
    saida = input("Horário no formato xx-xx-xx de saída")
    attendence_time(entrada,presenca,saida)
    payroll_processing(salario)
    desempenho = input("Como está O desempenho do funcionário?")
    evalution(desempenho)
    print("Se vocẽ deseja utilizar um ")
    necessity_license = int(input())
    if(necessity_license == 1):
        leave_management()
    elif(necessity_license != 1):
        print("Funcionário continuára trabalhando de maneira consistente? ")
    print("")
    compliance_status = int(input())
    if(compliance_status == 1):
        compliance()
    elif(complice_status != 1):
        print("Estamos seguindo as regras de Compliance")



main()
