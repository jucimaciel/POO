
import pymysql.cursors
from funcionario.classes import *

def conectar():
    connection = pymysql.connect(
        host='localhost',  
        user='root', 
        password='kladjucireis', 
        database='prova03',    
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor) 
    return connection
    
def menu_rei():
    print('---------MENU---------\n')
    print('1 - Manter Funcao')
    print('2 - Manter Funcionario')
    print('0 - SAIR')
    opc = 1
    while opc != 0:
        opc = int(input('Digite a opcao que deseja: '))

        if opc == 1:
            menu_principe() 
        elif opc == 2:
            f=Funcao.tratamento6()
            if f != None:
                menu_nobre()  

            else:
                print('Não existe função cadastrada!')
 

def menu_principe():
    aux = 1
    while aux != 0:
        print('---------MENU---------\n')
        print('1-Cadastrar Funcao')
        print('2-Pesquisar Funcao')
        print('3-Editar Funcao')
        print('4-Deletar Funcao')
        print('0-Sair')
        opcao = int(input('\nINFORME UMA OPÇÃO DE MENU PARA PROSSEGUIR: '))

        j = Funcao.tratamento6()
        if j == None:
            if opcao == 1:
                nome = (input('Informe o nome da funcao: '))
                cod = (input('Informe o codigo: '))
                f=Funcao(cod,nome)
                connection = conectar()
                with connection.cursor() as c:
                    sql = "INSERT INTO funcao (cod, nome) VALUES (%s,%s)"
                    c.execute(sql, (f.cod,f.nome))
                connection.commit()
                connection.close()
            elif opcao == 0:
                aux = 0
            else:
                print('Nao existe funcao')        
        else:        
            if opcao == 1:
                nome = (input('Informe o nome da funcao: '))
                cod = (input('Informe o codigo: '))
                f=Funcao(cod,nome)
                connection = conectar()
                with connection.cursor() as c:
                    sql = "INSERT INTO funcao (cod, nome) VALUES (%s,%s)"
                    c.execute(sql, (f.cod,f.nome))
                connection.commit()
                connection.close()
                
            elif opcao == 2:
                Funcao.pesquisar_funcao()
                



            

            elif opcao == 3:
                Funcao.editar_pesquisar()
                

                            

            elif opcao == 4:
                Funcao.deletar_funcao()  
        
            elif opcao == 0:
                print('encerrando programa...')
                aux = 0
                
            
            

def menu_nobre():
    aux = 1
    while aux != 0:
        print('---------MENU---------\n')
        print('1-Cadastrar Funcionario')
        print('2-Pesquisar Funcionario')
        print('3-Editar Funcionario')
        print('4-Deletar Funcionario')
        print('0-Sair')
        opcao = int(input('\nInforme uma opcao de menu para prosseguir: '))

        if opcao == 1:
            resp=Funcao.pesquisar_funcao()
            if resp!=None:
                f=Funcionario(Funcao(resp['cod'],resp['nome']))   
                connection=conectar()                   
                with connection.cursor() as c:
                    sql = "INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES (%s, %s, (select funcao.id from funcao where cod = %s), %s,%s)"
                    c.execute(sql, (f.cpf, f.nome, f.funcao.cod, f.salario, f.telefone))
                connection.commit()
                connection.close()

        elif opcao == 2:
            Funcionario.pesquisar_funcionario()

        elif opcao == 3:
            Funcionario.editar_funcionario()

        elif opcao == 4:
            Funcionario.deletar_funcionario()

        elif opcao == 0:
            print('encerrando programa...')
            aux = 0
            
        else:
            print('erro')
            



menu_rei()
print('Passa a gente, por favor! Abraço!')
    
    

