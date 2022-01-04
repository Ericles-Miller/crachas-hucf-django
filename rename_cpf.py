import os, time
from pathlib import Path
import mysql.connector

list_id = list()

def connect():
    com = mysql.connector.connect(host='localhost',database='crachas',user='root',password='')
    return com
def view():
    lista = []
    connection = connect()
    cursor = connection.cursor()
    #cursor.select_db('crachas')
    select_requests = "select *from app_servidor;"
    cursor.execute(select_requests)

    request = cursor.fetchall()

    for requests in request:
        view_dict = {'id': requests[0], 'nome':requests[1], 'cpf': requests[2], 'imagem':requests[3] }
        lista.append(view_dict)

    print(lista)
    if lista:
        for i in range(len(lista)):
            for j in range(len(list_id)):
                if lista[i]['id'] == list_id[j]:
                    lista.pop(i)
        rename_image(lista)
    else:
        time.sleep(300)
        view()

def rename_image(lista):

    for i in range(len(lista)):
        
        cpf = lista[i]['cpf']
        imagem = lista[i]['imagem']
        imagem = imagem[8:]
        
        addrees =Path('.\cracha\imagens')
        
        cpf = '{}.jpg'.format(cpf)

        old_name = os.path.join(addrees, imagem)
        new_name = os.path.join(addrees, cpf)
        os.rename(old_name, new_name)
        list_id.append(lista[i]['id'])

    for i in range(len(lista)):
        lista.pop(i)

    time.sleep(300)
    view()


view()