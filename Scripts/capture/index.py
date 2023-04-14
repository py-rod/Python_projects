import pyscreenshot
import pyautogui

width, height = pyautogui.size()


nombre = input("Ingresar nombre de captura de pantalla: ")
extencion = input("Ingresar tipo de extencion: ")


img = pyscreenshot.grab(bbox= (0,0, width, height))


img.save(f"{nombre}.{extencion}")


