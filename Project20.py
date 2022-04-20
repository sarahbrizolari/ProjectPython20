import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Project20"] #nome do data base
mycol = mydb["auxilios_concedidos"] #nome da colection

x = 0
y = 0

while x == 0:
   y = int(input("Digite: \n1- Adicionar o arquivo CSV à base de dados \n2- Adicionar arquivos à base de dados"
                  " \n3- Fazer a leitura no banco de dados e gerar um arquivo txt\n4- apagar dados da base de dados\n5 - Sair\n "))
   if y == 1 :
       arq = open("C:/Users/Sarah Brizolari/PycharmProjects/ProjectPython20/auxilios_concedidos.csv",encoding="utf8")
       for line in arq:
        column = line.split(',')  #separados por linhas, split cada vez que tem virgula na linha ele gera um vetor
        mydict =[
            {"Id_beneficiado": column[0], "Matricula_discente" : column[1], "Tipo_auxilio": column[2], "Sexo": column[3],
                  "Idade": column[4], "Raça": column[5], "Pais": column[6], "Curso": column[7], "Nivel": column[8],
                  "Modalidade": column[9], "Estado" : column[10], "Forma_ingresso": column[11], "Ano_ingresso": column[12],
                  "Discente_situacao": column[13],}
            ]

        j = mycol.insert_many(mydict)
        print(j.inserted_ids)

   elif y == 2:
        listaData = {
        "Id_beneficiado": input("Digite o ID do beneficiado: "),
        "Matricula_discente": input("Digite a matricula: "),
        "Tipo_auxilio": input("Digite o tipo de auxilio: "),
        "Sexo": input("Digite o sexo: "),
        "Idade": input("Digite a idade: "),
        "Raça": input("Digite a raça: "),
        "Pais": input("Digite o pais: "),
        "Curso": input("Digite o curso: "),
        "Nível": input("Digite o nivel: "),
        "Modalidade": input("Digite a modalidade: "),
        "Estado": input("Digite o estado: "),
        "Froma_ingresso": input("Digite a forma de ingresso: "),
        "Ano_ingresso": input("Digite o ano do ingresso: "),
        "Discente_situacao": input("Digite a situaçao: ")}

        ins = mycol.insert_one(listaData)
        print(ins.inserted_id)

   elif y == 3:
        dados = []
        arq = open('C:/Users/Sarah Brizolari/PycharmProjects/ProjectPython20/txt/aux_conc.txt', 'w')

        for lines in mycol.find({}, {'_id': 0}): #cada iteração do for ele faz a leitura da linha na coleção
            dados.append(str(lines) + "\n")      #nesse comando a linha liga append é atribuida ao vetor dados
            arq.writelines(dados) #escreve no arqtxt o q contem no vetor dados
            print(lines)
        arq.close()
   elif y == 4 :
       delete = mycol.delete_many({})
       print(delete.deleted_count, "registros apagados")

   elif y == 5:
       x = 1

   else:
        print("Opcao invalida! Por favor escolha uma opção Válida: ")