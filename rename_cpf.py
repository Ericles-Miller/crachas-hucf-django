import os, time
from pathlib import Path
import mysql.connector
import shutil

list_id = list()

def connect():
    com = mysql.connector.connect(host='localhost',database='crachas',user='root',password='', port='3307')
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
        rename_image(lista)
    else:
        time.sleep(300)
        view()

def rename_image(lista):

    for i in range(len(lista)):
        id = lista[i]['id']   
        cpf = lista[i]['cpf']
        imagem = lista[i]['imagem']
        imagem = imagem[8:]
        
        addrees =Path(r'C:\Users\Administrador\Desktop\cracha\crachas-hucf-django\imagens')
        new_addrees = Path(r'C:\Users\Administrador\Desktop\cracha\crachas-hucf-django\imagens_renomeadas')
        cpf = '{}.jpg'.format(cpf)
        
        old_name = os.path.join(addrees, imagem)
        new_file = os.path.join(new_addrees, imagem)
        if not os.path.isfile(new_file):
            shutil.copy(old_name,new_file)
            new_name = os.path.join(new_addrees, cpf)
            if not os.path.isfile(new_name):
                os.rename(new_file, new_name)
                #os.remove(new_file)
        else:
            os.remove(new_file)
    time.sleep(300)
    view()

view()