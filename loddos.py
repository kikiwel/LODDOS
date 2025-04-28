import requests
import time
import os
import subprocess
from colorama import Fore, init

# Инициализация colorama
init(autoreset=True)


# Функция для создания градиентного текста
def create_gradient_text(text, start_color, end_color):
    def interpolate_color(start, end, factor):
        return round(start + (end - start) * factor)

    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    gradient_text = ""
    length = len(text)
    for i, char in enumerate(text):
        factor = i / length
        r = interpolate_color(start_color[0], end_color[0], factor)
        g = interpolate_color(start_color[1], end_color[1], factor)
        b = interpolate_color(start_color[2], end_color[2], factor)
        gradient_text += rgb_to_ansi(r, g, b) + char
    gradient_text += Fore.RESET
    return gradient_text

# Определение начального и конечного цветов (RGB)
start_color = (255, 0, 0)  # Красный
end_color = (0, 0, 255)    # Синий

# ASCII арт
ascii_art = """
  
 ####      #####   ##   ##  #####             #####    #####     #####    #####
  ##      ##   ##  ##   ##   ## ##             ## ##    ## ##   ##   ##  ##   ##
  ##      ##   ##  ##   ##   ##  ##            ##  ##   ##  ##  ##   ##  #
  ##      ##   ##  ##   ##   ##  ##            ##  ##   ##  ##  ##   ##   #####
  ##   #  ##   ##  ##   ##   ##  ##            ##  ##   ##  ##  ##   ##       ##
  ##  ##  ##   ##  ##   ##   ## ##             ## ##    ## ##   ##   ##  ##   ##
 #######   #####    #####   #####             #####    #####     #####    #####

       OWNER: @DEATH_BTW |Version 1.0                                       
 """

def run_ddos_script():
    subprocess.run(['python', 'DDos.py'])

print(ascii_art)
time.sleep(3) # Пауза после вывода ASCII арта

print("[1] DDoS attack")

choose = int(input("Выбор: "))
if choose == 1:
    run_ddos_script()

