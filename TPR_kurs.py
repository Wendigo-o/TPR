import random
import matplotlib.pyplot as plt
from tkinter import *

window = Tk()
window.title("Принятие решений с использованием имитационной модели задачи управления запасами") #название окна
window.geometry('1200x320') #размер окна

lblT = Label(window, text="Период: ")  
lblT.grid(column=0, row=0)

txtT = Entry(window,width=10)  
txtT.grid(column=1, row=0)
txtT.insert(0,30)

lblV = Label(window, text="Обьем склада: ")  
lblV.grid(column=0, row=1)

txtV = Entry(window,width=10)  
txtV.grid(column=1, row=1)
txtV.insert(0,200)


lblArenda = Label(window, text="Аренда склада за ед.: ")  
lblArenda.grid(column=2, row=1)

txtArenda = Entry(window,width=10)  
txtArenda.grid(column=3, row=1)
txtArenda.insert(0,10)


lblZapas0 = Label(window, text="Кол-во запаса на складе: ")  
lblZapas0.grid(column=0, row=2)

txtZapas0 = Entry(window,width=10)  
txtZapas0.grid(column=1, row=2)
txtZapas0.insert(0,100)


lblTovarDohod = Label(window, text="Прибыль за ед. товара: ")  
lblTovarDohod.grid(column=0, row=3)

txtTovarDohod = Entry(window,width=10)  
txtTovarDohod.grid(column=1, row=3)
txtTovarDohod.insert(0,40)


lblShtrafSklad = Label(window, text="Стоимость хранения кажд. оставшейся ед. на складе: ")  
lblShtrafSklad.grid(column=0, row=4)

txtShtrafSklad = Entry(window,width=10)  
txtShtrafSklad.grid(column=1, row=4)
txtShtrafSklad.insert(0,1)


lblShtrafDef = Label(window, text="Штраф за дефицит за кажд. ед.: ")  
lblShtrafDef.grid(column=2, row=4)

txtShtrafDef = Entry(window,width=10)  
txtShtrafDef.grid(column=3, row=4)
txtShtrafDef.insert(0,20)


lblZakazConst = Label(window, text="Фикс. стоимость на поставку: ")  
lblZakazConst.grid(column=0, row=5)

txtZakazConst = Entry(window,width=10)  
txtZakazConst.grid(column=1, row=5)
txtZakazConst.insert(0,200)


lblZakazCount = Label(window, text="Цена на поставку за кадж. ед.: ")  
lblZakazCount.grid(column=2, row=5)

txtZakazCount = Entry(window,width=10)  
txtZakazCount.grid(column=3, row=5)
txtZakazCount.insert(0,100)


lblOtZakazDoPost = Label(window, text="Интервал от заказа до поставки: ")  
lblOtZakazDoPost.grid(column=4, row=7)

txtOtZakazDoPost = Entry(window,width=10)  
txtOtZakazDoPost.grid(column=5, row=7)
txtOtZakazDoPost.insert(0,0)


lblIntervalPost = Label(window, text="Интервал поставок: ")  
lblIntervalPost.grid(column=6, row=4)

txtIntervalPost = Entry(window,width=10)  
txtIntervalPost.grid(column=7, row=4)
txtIntervalPost.insert(0,0)

#Интервал поставок---------------------
lblIntervalPostPopolnNa = Label(window, text="Пополнение на: ")  #Интервал поставок
lblIntervalPostPopolnNa.grid(column=6, row=5)

txtIntervalPostPopolnNa = Entry(window,width=10)  
txtIntervalPostPopolnNa.grid(column=7, row=5)
txtIntervalPostPopolnNa.insert(0,0)

lblIntervalPopolnenieOtcl = Label(window, text="Ср. отклонение от пополнения: ")   #Интервал поставок
lblIntervalPopolnenieOtcl.grid(column=6, row=6)

txtIntervalPopolnenieOtcl = Entry(window,width=10)  
txtIntervalPopolnenieOtcl.grid(column=7, row=6)
txtIntervalPopolnenieOtcl.insert(0,5)

lblIntervalPostPopolnOtZakazDoPost = Label(window, text="Интервал от заказа до поставки: ")  #Интервал поставок
lblIntervalPostPopolnOtZakazDoPost.grid(column=6, row=7)

txtIntervalPostPopolnOtZakazDoPost = Entry(window,width=10)  
txtIntervalPostPopolnOtZakazDoPost.grid(column=7, row=7)
txtIntervalPostPopolnOtZakazDoPost.insert(0,0)
#Интервал поставок-------------------------

lblSprosSr = Label(window, text="Среднее значение спроса: ")  
lblSprosSr.grid(column=4, row=0)

txtSprosSr = Entry(window,width=10)  
txtSprosSr.grid(column=5, row=0)
txtSprosSr.insert(0,100)


lblSprosOtcl = Label(window, text="Отклонение от ср.знач. спроса: ")  
lblSprosOtcl.grid(column=4, row=1)

txtSprosOtcl = Entry(window,width=10)  
txtSprosOtcl.grid(column=5, row=1)
txtSprosOtcl.insert(0,15)


lblPopolnenieOt = Label(window, text="Пополнение от: ")  
lblPopolnenieOt.grid(column=4, row=4)

txtPopolnenieOt = Entry(window,width=10)  
txtPopolnenieOt.grid(column=5, row=4)
txtPopolnenieOt.insert(0,100)


lblPopolnenieConst = Label(window, text="Пополнение на: ")  
lblPopolnenieConst.grid(column=4, row=5)

txtPopolnenieConst = Entry(window,width=10)  
txtPopolnenieConst.grid(column=5, row=5)
txtPopolnenieConst.insert(0,100)


lblPopolnenieOtcl = Label(window, text="Ср. отклонение от пополнения: ")  
lblPopolnenieOtcl.grid(column=4, row=6)

txtPopolnenieOtcl = Entry(window,width=10)  
txtPopolnenieOtcl.grid(column=5, row=6)
txtPopolnenieOtcl.insert(0,15)


def Standart():
    Start(1)
def NormalRaspr():
    Start(2)

btnStandart = Button(window, text="Расчитать стабильный привоз", command=Standart)  
btnStandart.grid(column=6, row=1)

btnNormalRaspr = Button(window, text="Расчитать привоз по норм.распр.", command=NormalRaspr)  
btnNormalRaspr.grid(column=6, row=2) 

dohod_list = [] # список доходов по дням

def NormRasrp (n,sr,otcl): #добавляет в список рандомные числа по нормальному распределению
    xList = []
    for i in range(n):
        xList.append(abs(random.normalvariate(sr,otcl)))
    return xList
def Start(nButton):
    zapas0 = int(txtZapas0.get()) #начальный запас на складе
    sklad = [zapas0] # список товаров на складе по дням
    T = int(txtT.get()) # рассматриваемый период в днях 
    vMax = int(txtV.get()) #максимальный обьем склада 
    if zapas0 > vMax:
        zapas0 = vMax
    arenda = float(txtArenda.get())    
    zakazConst = float(txtZakazConst.get()) # фиксированная стоимость на поставку вне зависимости от его размера
    zakazCount = float(txtZakazCount.get())  # цена на поставку за каждую единицу товара

    tovarDohod = float(txtTovarDohod.get()) # прибыль от продажи товара

    shtrafSklad = float(txtShtrafSklad.get()) # "штраф" за товар который остался на складе
    strafDef = float(txtShtrafDef.get()) # штраф за дефицит

    sprosSr = int(txtSprosSr.get()) #средняя величина спроса на товар в день
    sprosOtcl = int(txtSprosOtcl.get()) # среднее отклонение

    popolnenieOt = int(txtPopolnenieOt.get()) # пополнение от какого предела товаров
    popolnenieConst = int(txtPopolnenieConst.get()) # пополнение склада на фикс. число
    popolnenieOtcl = int(txtPopolnenieOtcl.get())
    
    otZakazDoPost = int(txtOtZakazDoPost.get()) #Интервал от заказа до поставки
    intervalPost = int(txtIntervalPost.get()) #Интервал поставок
    
    intervalPostPopolnNa = int(txtIntervalPostPopolnNa.get())#Интервал поставок
    intervalPopolnenieOtcl = int(txtIntervalPopolnenieOtcl.get())#Интервал поставок
    intervalPostPopolnOtZakazDoPost = int(txtIntervalPostPopolnOtZakazDoPost.get())#Интервал поставок
    
    plt.figure(1).clf()
    plt.figure(2).clf()
    sklad = [zapas0]
    dohod_list = []
    
    spros_list = NormRasrp(T,sprosSr,sprosOtcl)
    otZakazDoPostDay = -1
    plt.figure(2)
    plt.plot([1,T],[0,0],c ='orange',alpha = 0.2)
    for day in range(1,T+1):
        sklad.append(sklad[day-1])
        dohodDay = 0 #доход в конкретный день
        dohodDay -= vMax*arenda #вычитаем из дохода аренду   
        if intervalPost!=0 and day % intervalPost == 0 and day >= intervalPostPopolnOtZakazDoPost:
            if nButton == 2:
                intervalPostPopolnNa = abs(random.normalvariate(int(txtIntervalPostPopolnNa.get()),intervalPopolnenieOtcl))
            else:
                intervalPostPopolnNa = int(txtIntervalPostPopolnNa.get())
            if sklad[day] + intervalPostPopolnNa > vMax:
                intervalPostPopolnNa = vMax - sklad[day]
            if intervalPostPopolnNa != 0:
                dohodDay -= (zakazConst + zakazCount*intervalPostPopolnNa) #вычитаем из дохода доставку товара
            plt.figure(1)
            plt.scatter(day-1,sklad[day],c ='red',alpha = 0.5,marker = 7)
            plt.figure(2)
            plt.scatter(day,0,c ='red',alpha = 0.5,marker = 7)
            sklad[day] += intervalPostPopolnNa
            
        if (sklad[day] < popolnenieOt) and(day > otZakazDoPostDay): #проверяем нужно ли пополнять наш склад
            otZakazDoPostDay = day + otZakazDoPost
            
        if (day == otZakazDoPostDay):
            if nButton == 2:
                popolnenieConst = abs(random.normalvariate(int(txtPopolnenieConst.get()),popolnenieOtcl))
            if sklad[day] + popolnenieConst > vMax:
                popolnenieConst = vMax - sklad[day]
            dohodDay -= (zakazConst + zakazCount*popolnenieConst) #вычитаем из дохода доставку товара
            plt.figure(1)
            plt.scatter(day-1,sklad[day],c ='red',alpha = 0.4,marker = 6)
            plt.figure(2)
            plt.scatter(day,0,c ='red',alpha = 0.4,marker = 6)
            sklad[day] += popolnenieConst
            popolnenieConst = int(txtPopolnenieConst.get())
        sklad[day] -= spros_list[day-1] #забрали со склада по спросу
        if sklad[day] < 0:
            dohodDay += tovarDohod*(spros_list[day-1] - abs(sklad[day])) - strafDef*abs(sklad[day]) #прибавляем к доходу прибыль и вычитаем из дохода штраф
            plt.figure(1)
            plt.scatter(day,sklad[day],c ='red',alpha = 1,marker ='x')
            plt.figure(2)
            plt.scatter(day,-strafDef*abs(sklad[day]),c ='red',marker ='x')
            sklad[day] = 0
        else:
            dohodDay += tovarDohod*spros_list[day-1] # а тут просто прибавляем к доходу сколько мы продали
            
        dohodDay -= shtrafSklad*sklad[day] # вычитаем из дохода штраф за каждую единицу оставшуюся на складе
        dohod_list.append(dohodDay) #заносим наш доход в список доходов
    
    plt.figure(1)
    plt.plot(sklad,c='lightpink',ls = '-',label = 'Товаров на складе') # показывает график спроса
    plt.legend()
    
    plt.figure(1)
    plt.plot([_ for _ in range(1,T+1)],spros_list,c='brown',ls = '-',label = 'Спрос') # показывает график спроса
    plt.legend()
    
    plt.figure(2)
    plt.plot([_ for _ in range(1,T+1)],dohod_list,c='orange',ls = '-',label = 'Доход') #показывает доход
    plt.legend()
    plt.show()

window.mainloop()