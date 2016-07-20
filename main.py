# -- coding: utf-8 --
from __future__ import unicode_literals

from tkinter import *


def calcTotalLength():
    totalLength = int(length.get()) * 2
    print(totalLength)
    return totalLength


def calcNumberOfTrucks():
     number = float(size.get())/float(truckVolume.get())
     if number > int(number):
         return int(number) + 1
     else:
         return int(number)


def calcCostPerTruck(length, serviceCost):
    numberCentKm = float(length)/100.0
    fuelCost = numberCentKm * (float(fuelMax.get()) + float(fuelMin.get()))
    return serviceCost + fuelCost


def fillCase(numberOfTrucks, costPerTruck, transportCost, totalTaxes, totalCost, totalProfit, cleanProfit):
    text2show = "Случай #{0}:\n\
    Расход топлива с нагрузкой: {1} л/100км\n\
    Расход топлива без нагрузки: {2} л/100км\n\
    Стоимость топлива: {3} руб\n\
    Расходы на обслуживание машин: {4} руб\n\
    Вместимость грузовиков: {5} шт\n\
    Размер партии: {6} шт\n\
    Расстояние до получателя: {7} км\n\
    Прибыль с единицы в партии: {8} руб\n\
    Налог с единицы в партии: {9} руб\n\n\
    Необходимо грузовиков: {10}\n\
    Каждый грузовик будет стоить: {11} руб\n\
    Полные расходы на транспорт: {12} руб\n\
    Полные расходы на налоги: {13} руб\n\
    Все расходы: {14} руб\n\n\
    Вся прибыль: {15} руб\n\n\
    Чистая прибыль: {16} руб\n\n\n".format(case,
                                   round(float(fuelMax.get()), 2),
                                   round(float(fuelMin.get()), 2),
                                   round(float(fuelCost.get()), 2),
                                   round(float(truckService.get()), 2),
                                   int(truckVolume.get()),
                                   int(size.get()),
                                   int(length.get()),
                                   round(float(profit.get()), 2),
                                   round(float(tax.get()), 2),
                                   numberOfTrucks,
                                   round(costPerTruck, 2),
                                   round(transportCost, 2),
                                   round(totalTaxes, 2),
                                   round(totalCost, 2),
                                   round(totalProfit, 2),
                                   round(cleanProfit, 2))
    result.insert(END, text2show)


def calculateTotal(event):
    kilometers = int(length.get())
    numberOfTrucks = calcNumberOfTrucks()
    costPerTruck = calcCostPerTruck(kilometers, int(truckService.get()))
    transportCost = numberOfTrucks * costPerTruck
    totalTaxes = float(tax.get()) * int(size.get())
    totalCost = transportCost + totalTaxes + int(cost.get())

    totalProfit = int(profit.get()) * int(size.get())

    cleanProfit = totalProfit - totalCost

    fillCase(numberOfTrucks, costPerTruck, transportCost, totalTaxes, totalCost, totalProfit, cleanProfit)

    global case
    case += 1

case = 1

root = Tk()

root.title("Счетчик затрат")

fuelMaxLabel = Label(root, text="Топливо (л/100км)\nС нагрузкой").grid(row=1, column=1)
fuelMax = Entry(root)
fuelMax.grid(row=1, column=2)

fuelMinLabel = Label(root, text="Топливо (л/100км)\nБез нагрузки").grid(row=2, column=1)
fuelMin = Entry(root)
fuelMin.grid(row=2, column=2)

fuelCostLabel = Label(root, text="Стоимость топлива (руб/л)").grid(row=3, column=1)
fuelCost = Entry(root)
fuelCost.grid(row=3, column=2)

truckServiceLabel = Label(root, text="Обслуживание машин (руб)").grid(row=4, column=1)
truckService = Entry(root)
truckService.grid(row=4, column=2)

truckVolumeLabel = Label(root, text="Вместимость грузовика (шт)").grid(row=5, column=1)
truckVolume = Entry(root)
truckVolume.grid(row=5, column=2)

costLabel = Label(root, text="Себестоимость ед (руб)").grid(row=6, column=1)
cost = Entry(root)
cost.grid(row=6, column=2)

sizeLabel = Label(root, text="Размер партии (шт)").grid(row=7, column=1)
size = Entry(root)
size.grid(row=7, column=2)

lengthLabel = Label(root, text="Расстояние до получателя (км)").grid(row=8, column=1)
length = Entry(root)
length.grid(row=8, column=2)

profitLabel = Label(root, text="Прибыль с ед (руб)").grid(row=9, column=1)
profit = Entry(root)
profit.grid(row=9, column=2)

taxLabel = Label(root, text="Налог с ед. партии (руб)").grid(row=10, column=1)
tax = Entry(root)
tax.grid(row=10, column=2)

button = Button(root, text="Посчитать")
button.bind("<Button-1>", calculateTotal)
button.grid(row=11, column=1)


result = Text(root, font='Arial 14', wrap=WORD)
scrollbar = Scrollbar(root)
scrollbar['command'] = result.yview
result['yscrollcommand'] = scrollbar.set
result.grid(row=1, column=3, rowspan=11)

root.mainloop()