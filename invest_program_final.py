import matplotlib.pyplot as plt 
import numpy as np
import math as m
import pandas as pd

#Investment Program

def simple_interest():
    print("Simple Interest")
    return f"{I:.2f}"
    #return f"Interest with all variables given is ${I:.2f}"
#print(simple_interest()) 

def continously_compounded_interest():
    print("Continously Compounded Interest")
    #Future Value
    A = P*(m.e**(r*t))
    return F"{A:.2f}"
#print(continously_compounded_interest())

def compounded_interest():
    print("Compounded Interest")
    #Future Value
    A = P*(1+(r/n))**(n*t)
    return F"{A:.2f}"

print("Type S, C, or CC")
ziech = input("What investment do you want to do: (Simple, Compound, Cont. Compound): ").upper()
if ziech == "S":
    #Principal Balance
    P = float(input("What is your principal balance?: "))
    #Interest rate
    r = (float(input("Interest rate: ")))
    r /=100
    #Time
    t = (float(input("How long do you want to invest it for (in years): ")))
    #Interest
    I = P*r*t
    vin = simple_interest()
    vin = float(vin)
    print(vin)

elif ziech == "C":
    #Principle
    P = float(input("What is your principal balance?: "))
    #Interest rate
    r = (float(input("Intrest rate: ")))
    r /=100
    #Time
    t = (float(input("How long do you want to invest it for (in years): ")))
    #Compounded time
    print(" ")
    print("Charge interest when?")
    com = int(input("Compounded annually(1), semi-annually(2), Quarterly(4): "))
    if com in [1,2,4]:
        n = com
    vin = compounded_interest()
    vin = float(vin)
    print(vin)

elif ziech == "CC":
    #Principle
    P = float(input("What is your principal balance?: "))
    #Interest rate
    r = (float(input("Intrest rate: ")))
    r /=100
    #Exponential
    e = m.e
    #Time
    t = (float(input("How long do you want to invest it for (in years): ")))
    vin = continously_compounded_interest()
    vin = float(vin)
    print(vin)
else:
    print("Invalid try again")

#Percentages
annual_returns = np.array([2.31,-.81,1.02,2.00,-.30])
#Actual Number
annual_returns /=100
# ziech = P
# print(ziech)

new_ziech = np.array([vin])

annual_returns = annual_returns * new_ziech

list_returns = []
balance = 5
for i in range(1, 6):
    balance = balance + annual_returns[i - 1]
    list_returns.append(balance)
    print(balance)


years = [2020,2021,2022,2023,2024]
print(np.array2string(annual_returns, precision=2, suppress_small=True))

Returning_Reports = pd.Series(list_returns).round(2)

print("Returnings Reports")
print(Returning_Reports)


plt.xlabel("Years") 
plt.ylabel("Returns")
plt.title("Annual Returns")
plt.plot(years, list_returns, marker=".",
                                markersize=20,
                                markerfacecolor="black")
plt.show()




