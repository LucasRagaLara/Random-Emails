import yagmail
import random
import csv
import getpass

def obtener_archivo_aleatorio():
    with open('./csv/archivos.csv', 'r') as abrir_csv:
        leer_csv = csv.DictReader(abrir_csv, delimiter=';')
        for linea in leer_csv:
            archivos = linea['archivos_adjuntos']
        lista_archivos = archivos.split(",")
        print("estp es la lista de archivos", lista_archivos)

    cantidad = random.randint(1,2)
    if cantidad == 1:
        envio_archivo = random.choice(lista_archivos)
        print(envio_archivo)
        manejador_archivo = open(envio_archivo, 'rb')
    elif cantidad == 2:
        envio_archivo = ", ".join(random.sample(lista_archivos, 2))
        print( "esto es el archivo a enviar", envio_archivo)
        manejador_archivo = [open(ruta, 'rb') for ruta in envio_archivo]
    return manejador_archivo

def lectura_csv():
    with open("./csv/fichero.csv", 'r') as abrir_fichero:
        leer_csv = csv.DictReader(abrir_fichero, delimiter=';')
        lista_csv = [linea for linea in leer_csv]
    return lista_csv    

def enviar_correo():
    correo = input("introduce el correo: ")
    password = getpass.getpass(prompt="Introduce la contraseña asociada: ")
    yag = yagmail.SMTP(correo, password)
    csv_fichero = lectura_csv()
    for linea in csv_fichero:
        random_archivo = obtener_archivo_aleatorio()
        yag.send(
            to=linea['correo'],
            subject=linea['asunto'],
            contents=linea['cuerpo'],
            attachments=random_archivo
        )
    return "Correo enviado de forma satisfactoria."

print(enviar_correo())