import subprocess
from colorama import init, Fore
init()


FOLDER_ORDER = "~/Descargas"

FILES = [".txt", ".pdf", ".docx", ".epub", ".mp3",
         ".mp4", ".jpg", ".png", ".jpge", ".gif", ".svg", ".iso", ".zip", ".rar"]


for file in FILES:
    # ARCHIVOS
    if file == ".txt" or file == ".pdf" or file == ".docx" or file == ".epub":
        try:
            subprocess.run(f"mv {FOLDER_ORDER}/*{file} ~/Documentos",
                           shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            print(Fore.RED +
                  f"Archivos {file} no encontrados en la carpeta {FOLDER_ORDER}")
        else:
            print(Fore.GREEN +
                  f"Archivos {file} encontrados y movidos a ~/Documentos")

    # VIDEOS O AUDIOS
    elif file == ".mp4" or file == ".mp3":
        try:
            subprocess.run(f"mv {FOLDER_ORDER}/*{file} ~/Vídeos",
                           shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            print(Fore.RED +
                  f"Archivos {file} no encontrados en la carpeta {FOLDER_ORDER}")
        else:
            print(Fore.GREEN +
                  f"Archivos {file} encontrados y movidos a ~/Vídeos")

    # JUEGOS PSP
    elif file == ".iso":
        try:
            subprocess.run(f"mv {FOLDER_ORDER}/*{file} ~/Descargas/Juegos_psp",
                           shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            print(Fore.RED +
                  f"Archivos {file} no encontrados en la carpeta {FOLDER_ORDER}")
        else:
            print(Fore.GREEN +
                  f"Archivos {file} encontrados y movidos a ~/Descargas/Juegos_psp")

    # ARCHIVOS COMPRIMIDOS
    elif file == ".zip" or file == ".rar" or file == ".tar":
        try:
            subprocess.run(f"mv {FOLDER_ORDER}/*{file} ~/Descargas/Zips",
                           shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            print(Fore.RED +
                  f"Archivos {file} no encontrados en la carpeta {FOLDER_ORDER}")
        else:
            print(Fore.GREEN +
                  f"Archivos {file} encontrados y movidos a ~/Descargas/Zips")

    # IMAGENES
    else:
        try:
            subprocess.run(f"mv {FOLDER_ORDER}/*{file} ~/Imágenes/Imagenes_Descargadas/",
                           shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            print(Fore.RED +
                  f"Archivos {file} no encontrados en la carpeta {FOLDER_ORDER}")
        else:
            print(Fore.GREEN +
                  f"Archivos {file} encontrados y movidos a ~/Imágenes/Imagenes_Descargadas/")
