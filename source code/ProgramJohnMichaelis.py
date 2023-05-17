import pyautogui
import os
import pyperclip
import time
from bs4 import BeautifulSoup
import requests
import pygame
from tkinter import *




def clean():
  with open('John Michaelis XD.txt', 'r') as file :
    filedata = file.read()
  filedata = filedata.replace("*", "")
  filedata = filedata.replace(";", "")
  filedata = filedata.replace("'", "")
  filedata = filedata.replace("1", "")
  filedata = filedata.replace("2", "")
  filedata = filedata.replace("3", "")
  filedata = filedata.replace("4", "")
  filedata = filedata.replace("5", "")
  filedata = filedata.replace("6", "")
  filedata = filedata.replace("7", "")
  filedata = filedata.replace("8", "")
  filedata = filedata.replace("9", "")
  filedata = filedata.replace("0", "")
  filedata = filedata.replace("~", "")
  filedata = filedata.replace("/", "")
  filedata = filedata.replace("$", "")
  filedata = filedata.replace("`", "")
  filedata = filedata.replace(":", "")
  with open('John Michaelis XD.txt', 'w') as file:
    file.write(filedata)

def proverka():
  b = 0
  screens = 0
  with open('John Michaelis XD.txt', 'r') as file:
    time.sleep(5)
    pyautogui.click(171, 560)
    for line in file.readlines():
      b = b + 1
      if (b == 20):
        break
      pyperclip.copy(line)
      pyautogui.hotkey('ctrl', 'a', )
      pyautogui.press('backspace')
      pyautogui.hotkey('ctrl', 'v')
      pyautogui.click(419, 991)
      pyautogui.screenshot('C:\John_Michaelis\JMscreenshot\JohnMichaelis{}.png'.format(screens))
      screens = screens + 1
      pyautogui.click(171, 560)

def report():
  print('Сделано Старшим прокурором John Michaelis')
  b = 0
  url = 'https://forum.gta5rp.com/forums/zhaloby-v-prokuraturu.743/'
  timer = int(input('через какое количество секунд производить проверку страницы с жалобами?'))

  while True:
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Сейчас время:", local_time)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    themeorg = soup.find_all('div', class_='structItem-title')
    print(themeorg[1])
    solbi = str(themeorg[1])
    time.sleep(timer)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    themenoorg = soup.find_all('div', class_='structItem-title')
    print(themenoorg[1])
    b = b + 1
    t = themenoorg[1].find('a')['href']
    if (themenoorg == themeorg):
      print('Новых жалоб не найдено :(', )
      print('Выполненно проверок:', (b))


    else:
      print(
        'Что-то написали!!!!!!!!!!!!!!!!ALARM!!!!!!!!!!!ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('Выполненно проверок:', (b))
      pygame.mixer.init()
      pygame.mixer.music.load('trink.mp3')
      pygame.mixer.music.play()
      print('Сылка на жалобу:https://forum.gta5rp.com{}'.format(t))
      window = Tk()
      window.title("ALARM!!!")
      window.geometry('500x500')
      window.attributes("-topmost", True)
      lbl = Label(window, text="Кто-то что-то написал в жалобы", font=("Arial Bold", 25))
      lbl.grid(column=0, row=0)
      window.mainloop()
      time.sleep(100000)


print('Данная программа сделана бывшим старшим прокурором John Michaelis она включает в себя старрые функции которые были немного обновлены, а также одну новую\ndiscord:Frenk_Star#4769')
print('1.Название: МИНЕРВА\nОписание: данная функция очищает файл с именами от лишних символов\n2. Название: ФЕМИДА\nОписание:проверяет людей по ls.gov, чтобы использовать посмотрите гайд\n3. Название: АФИНА\nОписание:оповещает вас о новых жалобах в прокуратуру')
vibor = int(input('Выберите функцию (просто напишите цифру)'))

if (vibor==1):
  print('вы выбрали функцию МИНЕРВА')
  clean()
  print ('Функция МИНЕРВА успешно завершила свою работу')
  time.sleep(300)
if (vibor==2):
  print('вы выбрали функцию ФЕМИДА')
  proverka()
  print('Функция ФЕМИДА успешно завершила свою работу')
  time.sleep(300)
if (vibor==3):
  print('вы выбрали функцию АФИНА')
  report()
  print('Функция АФИНА успешно завершила свою работу')
  time.sleep(300)