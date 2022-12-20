import pymysql.cursors 

def conectar():
    connection = pymysql.connect(
        host='localhost',  
        user='root', 
        password='kladjucireis', 
        database='prova03',    
        charset='utf8mb4',  
        cursorclass=pymysql.cursors.DictCursor) 
    return connection

class Funcao():
  def __init__(self, cod:str, nome: str):
    self.nome = nome
    self.cod = cod
  
  @staticmethod
  def pesquisar_funcao():
    nov_cod = input('Digite o codigo: ')
    connection=conectar()
    with connection.cursor() as c:
        sql="select * from funcao where cod = %s"
        c.execute(sql, (nov_cod))
        resp=c.fetchone()
        print(resp)
    connection.close()
    return resp

  @staticmethod
  def tratamento6():
    connection=conectar()
    with connection.cursor() as c:
        sql="select * from funcao "
        c.execute(sql)
        resp=c.fetchone()
    connection.close()
    return resp


  @staticmethod
  def editar_funcao():
    cod = input('Digite o codigo da funcao que deseja alterar: ')
    aux = 1
    while aux != 0:
      print('1 - Alterar nome')
      print('2 - Alterar codigo')
      print('0 - Sair')
      opc = int(input('Digite a opcao que deseja: '))
      if opc == 1:
          nov_nome=input('Digite o novo nome: ')
          connection=conectar()
          with connection.cursor() as cursor:
              sql = "UPDATE funcao SET nome=%s WHERE cod=%s"
              cursor.execute(sql, (nov_nome,cod))
          connection.commit()
          connection.close()
      elif opc == 2:
          nov_cod=input('Digite o novo codigo: ')
          connection=conectar()
          with connection.cursor() as cursor:
              sql = "UPDATE  funcao set cod=%s WHERE cod=%s"
              cursor.execute(sql,(nov_cod,cod))
          connection.commit()
          connection.close()  
      elif opc == 0:
        aux = 0

  @staticmethod
  def deletar_funcao():
    cod = input('Digite o codigo da linha que deseja deletar: ')
    connection=conectar()
    try: 
        with connection.cursor() as cursor:
            sql = "DELETE from funcao where cod = %s"
            cursor.execute(sql,(cod))
        connection.commit()
        connection.close()
    except:
        print('Nao e possivel fazer essa operacao!') 


class Funcionario:

  def __init__(self,funcao:Funcao):
    self.cpf = input('Cpf: ')
    self.nome = input('Nome: ')
    self.salario = float(input('Salario: '))
    self.telefone = input('Telefone: ')
    self.funcao = funcao

  @staticmethod
  def pesquisar_funcionario():
     pegar_cpf = input('Digite o CPF: ')
     connection=conectar()
     with connection.cursor() as c:
        sql="select * from funcionario where cpf = %s"
        c.execute(sql,(pegar_cpf))
        resp=c.fetchone()
        print(resp)
     connection.close()
  @staticmethod
  def editar_funcionario():
    cpf = input('Digite o cpf do funcionario que deseja editar: ')
    opc=1
    while opc!= 0:
        print('1 - Alterar nome')
        print('2 - Alterar cpf')
        print('3 - Alterar salario')
        print('4 - Alterar telefone')
        print('0 - Sair')
        opc = int(input('Digite a opcao que deseja: '))
        if opc == 1:
            nov_nome=input('Digite o novo nome: ')
            connection=conectar()
            with connection.cursor() as cursor:
                sql = "UPDATE funcionario SET nome=%s WHERE cpf=%s"
                cursor.execute(sql, (nov_nome,cpf))
            connection.commit()
            connection.close()

        elif opc == 2:
            nov_cpf=input('Digite o novo cpf: ')
            connection=conectar()
            with connection.cursor() as cursor:
                sql = "UPDATE  funcionario set cpf=%s WHERE cpf=%s"
                cursor.execute(sql,(nov_cpf,cpf))
            connection.commit()
            connection.close()     

        elif opc == 3:
            nov_salario=float(input('Digite o novo salario: '))
            connection=conectar()
            with connection.cursor() as cursor:
                sql = "UPDATE  funcionario set salario=%s WHERE cpf=%s"
                cursor.execute(sql,(nov_salario,cpf))
            connection.commit()
            connection.close()  

        elif opc == 4:
            nov_telefone=input('Digite o novo telefone: ')
            connection=conectar()
            with connection.cursor() as cursor:
                sql = "UPDATE  funcionario set telefone=%s WHERE cpf=%s"
                cursor.execute(sql,(nov_telefone,cpf))
            connection.commit()
            connection.close()    

  @staticmethod
  def deletar_funcionario():
    cpf = input('Digite o cpf da linha que deseja deletar: ')
    connection=conectar()
    with connection.cursor() as cursor:
        sql = "DELETE from funcionario where cpf = %s"
        cursor.execute(sql,(cpf))
    connection.commit()
    connection.close()


