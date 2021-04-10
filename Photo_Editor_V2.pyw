# -*- coding: utf-8 -*-
import os
import tkinter
import webbrowser
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class IMGFilter():
    def bright(): # Изменить яркость
        brightness = 2
        file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
        source = Image.open(file)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))

                red = int(r * brightness)
                red = min(255, max(0, red))

                green = int(g * brightness)
                green = min(255, max(0, green))

                blue = int(b * brightness)
                blue = min(255, max(0, blue))

                result.putpixel((x, y), (red, green, blue))

        new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
        result.save(new_name, "JPEG")


    def negative(): # Негатив
        file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
        source = Image.open(file)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                result.putpixel((x, y), (255 - r, 255 - g, 255 - b))

        new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
        result.save(new_name, "JPEG")


    def white_black():
        brightness = 1
        file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
        source = Image.open(file)
        result = Image.new('RGB', source.size)
        separator = 255 / brightness / 2 * 3
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                total = r + g + b
                if total > separator:
                    result.putpixel((x, y), (255, 255, 255))
                else:
                    result.putpixel((x, y), (0, 0, 0))

        new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
        result.save(new_name, "JPEG")


    def contrast():
        coefficient = 2
        file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
        source = Image.open(file)
        result = Image.new('RGB', source.size)

        avg = 0
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= source.size[0] * source.size[1]

        palette = []
        for i in range(256):
            temp = int(avg + coefficient * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                result.putpixel((x, y), (palette[r], palette[g], palette[b]))

        new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
        result.save(new_name, "JPEG")
        

class web():
    """Class open webbrowser http"""
    def my_sait():
        webbrowser.open("https://gariksukiasyan.ga")
    def my_tg():
        webbrowser.open("https://t.me/t_o_ma_s")
    def my_vk():
        webbrowser.open("http://vk.com/id575200203")
    def github():
        webbrowser.open("https://github.com/Shadow-G")
    def gamejolt():
        webbrowser.open("https://gamejolt.com/@G_Games_Shady")


class App(object):
    """Class App Img Editora"""
    def __init__(self):
        self.webb = web()
        self.ffilter= IMGFilter()

    def img_open(self):
        try:
            file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
            canvas = tkinter.Canvas(window, height=400, width=600, bg="grey") # Создаем поверхность
            image = Image.open(file) # открываем файл по пути 
        
            o_width, o_height = image.size
            width, height = image.size
            if width > 2000:
                width = width / 100 * 10
                height = height / 100 * 10
            elif width < 2000:
                width = width / 100 * 30
                height = height / 100 * 30

        #print(width, height)

            image = image.resize((int(width), int(height)), Image.ANTIALIAS) # устанавливаем размер картинки для показа
            photo = ImageTk.PhotoImage(image) # передаем все дальше
            image = canvas.create_image(100,75, anchor='nw', image=photo) #показываем картинку на созданой поверхности
    
            canvas.grid(column=0, row=0) # устанавливаем кординаты поверхностив  нашем окне

        #lbl2 = Label(window, text=f"Ширина:{o_width} Высота:{o_height}", font=("Arial Bold", 12))
        #lbl2.grid(column=0, row=0)

            window.mainloop()
        except:
            pass

#    def img_filter(self): # наложить фильтр на изображение 
#        try:
#            file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
#            img = Image.open(file)
#            new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
#            img.save(new_name.name)
#        except Exception as e:
#            pass
        
    def img_edit(self): # Обрезать изображение по кординатам
        try:
            file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
            # Процесс
            new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
            yourImage = Image.open(file)
            w, h = yourImage.size
            yourImage.crop((0, 30, w, h-30)).save(new_name)
        except Exception as e:
            pass

    def img_conver(self): # Конвертировать формат изображения 
        try:
            file = filedialog.askopenfilename(filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*"))) # получаем путь к изображению
            img = Image.open(file)
            new_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes = (("Изображения","*.png;*.jpg;*.jpeg"),("Все файлы","*.*")))
            img.save(new_name.name)
        except Exception as e:
            pass

    def info(self):
        backgraund = tkinter.Canvas(window, height=400, width=600, bg="grey")
        backgraund.grid(column=0, row=0)

        canvas = tkinter.Canvas(window, height=0, width=0, bg="grey") # Создаем поверхность
        lbl2 = Label(window, text=f"""
Программа была написана на Python 3.9 с использование библиотеки Tkinter.
Это тестовый мини проект, для работы с Tkinter.

Возможности программы: 
-наложить фильтр на картинку  
-повернуть изображение
""", font=("Arial Bold", 12))
        lbl2.grid(column=0, row=0)
        canvas.grid(column=0, row=0) # устанавливаем кординаты поверхностив  нашем окне

    def menu(self):
        window.title("Photo Editor|Версия 1") #Заголовок программы
        window.geometry('600x400') # устанавливаем размер окна 

        backgraund = tkinter.Canvas(window, height=400, width=600, bg="grey")
        backgraund.grid(column=0, row=0)

        menu = Menu(window) # Создаем меню 

        menu.add_cascade(label='Просмотр картинки', command=self.img_open)

        ffil = Menu(menu, tearoff=0)
        ffil.add_command(label='Понизить яркость', command=IMGFilter.bright)
        ffil.add_command(label='Негатив', command=IMGFilter.negative)
        ffil.add_command(label='Черно-белый', command=IMGFilter.white_black)
        ffil.add_command(label='Повысить контрасность', command=IMGFilter.contrast)
        menu.add_cascade(label='Наложить фильтр', menu=ffil)
        
        menu.add_cascade(label='Конвертировать', command=self.img_conver)

        menu.add_cascade(label='Обрезать', command=self.img_edit)

        menu.add_cascade(label='Информация', command=self.info) # раздел Информация

        sait = Menu(menu, tearoff=0) # Убираем хрень для плавания текста
        sait.add_command(label='Мой сайт', command=web.my_sait) # открываем картинку
        sait.add_command(label='Мой TG', command=web.my_tg) # Сохраняем картинку
        sait.add_command(label='Мой VK', command=web.my_vk)
        sait.add_command(label='GitHub', command=web.github)
        sait.add_command(label='GameJolt', command=web.gamejolt)
        menu.add_cascade(label='Страницы', menu=sait) # раздел Файл

        window.config(menu=menu)

        window.mainloop()


if __name__ == '__main__':
    window = Tk()
    prog = App()
    prog.menu()