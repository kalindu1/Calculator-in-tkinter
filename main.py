##################################
#    developer = kalindu1        #
#    started date = 2021.10.23   #
#    states = under development  #
#    finished date = 2021.10.26  #
##################################
from tkinter import *

root = Tk()

root.geometry("180x240")
root.title("Calculator")
root.config(bg="gray")
root.resizable(False, False)

Main_Frame = Frame(root, bg="gray")
Main_Frame.pack(padx=3)

Nums = []

Input = Entry(Main_Frame, width=12, font='Consolas 19', bg="#97a1a8", border=0)
Input.grid(column=0, row=1, columnspan=5, pady=5)



def One():
    global Nums
    Nums.append("1")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)


def Two():
    global Nums
    Nums.append("2")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Three():
    global Nums
    Nums.append("3")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)


def Four():
    global Nums
    Nums.append("4")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Five():
    global Nums
    Nums.append("5")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Six():
    global Nums
    Nums.append("6")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Seven():
    global Nums
    Nums.append("7")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Eight():
    global Nums
    Nums.append("8")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Nine():
    global Nums
    Nums.append("9")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Zero():
    global Nums
    Nums.append("0")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Plus():
    global Nums
    Nums.append("+")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Minus():
    global Nums
    Nums.append("-")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Devi():
    global Nums
    Nums.append("/")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Multi():
    global Nums
    Nums.append("*")
    for i in range(len(Nums)):
        N = Nums[i]
    Input.insert(100, N)

def Equal():
    ipt = Input.get()
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    plus_counter = 0
    Minus_counter = 0
    Devi_counter = 0
    Multi_counter = 0


    Plus_Super_int = 0
    Minus_Super_int = 0
    Devi_Super_int  = 0
    Multi_Super_int = 0

    for i in range(len(ipt)):
        if "+" == ipt[i]:

            if counter1 >= 1:
                plus_counter +=1

            if counter1 == 0 and plus_counter == 0:
                int1 = ipt.split("+")[-0]
                int2 = ipt.split("+")[-1]

                int1 = int(int1)
                int2 = int(int2)

                Sum = int1 + int2
                Plus_Super_int = int1 + int2
                counter1 += 1

                Input.delete(0, 'end')
                Input.insert(100, Plus_Super_int)

            if counter1 >= 1 and plus_counter >= 1:
                int2 = ipt.split("+")[-1]

                int2 = int(int2)

                Plus_Super_int = Plus_Super_int + int2
                counter1 += 1

                Input.delete(0, 'end')
                Input.insert(100, Plus_Super_int)

        if "-" == ipt[i]:

            if counter2 >= 1:
                Minus_counter +=1

            if counter2 == 0 and Minus_counter == 0:
                int1 = ipt.split("-")[-0]
                int2 = ipt.split("-")[-1]

                int1 = int(int1)
                int2 = int(int2)

                Sum = int1 - int2
                Minus_Super_int = int1 - int2
                counter2 += 1

                Input.delete(0, 'end')
                Input.insert(100, Minus_Super_int)

            if counter2 >= 1 and Minus_counter >= 1:
                int2 = ipt.split("-")[-1]

                int2 = int(int2)

                Minus_Super_int = Minus_Super_int - int2
                counter2 += 1

                Input.delete(0, 'end')
                Input.insert(100, Minus_Super_int)

        if "/" == ipt[i]:

            if counter3 >= 1:
                Devi_counter +=1

            if counter3 == 0 and Devi_counter == 0:
                int1 = ipt.split("/")[-0]
                int2 = ipt.split("/")[-1]

                int1 = int(int1)
                int2 = int(int2)

                Sum = int1 / int2
                Devi_Super_int = int1 / int2
                counter3 += 1

                Input.delete(0, 'end')
                Input.insert(100, Devi_Super_int)

            if counter3 >= 1 and Devi_counter >= 1:
                int2 = ipt.split("/")[-1]

                int2 = int(int2)

                Devi_Super_int = Devi_Super_int / int2
                counter2 += 1

                Input.delete(0, 'end')
                Input.insert(100, Devi_Super_int)

        if "*" == ipt[i]:

            if counter4 >= 1:
                Multi_counter +=1

            if counter4 == 0 and Multi_counter == 0:
                int1 = ipt.split("*")[-0]
                int2 = ipt.split("*")[-1]

                int1 = int(int1)
                int2 = int(int2)

                Sum = int1 * int2
                Multi_Super_int = int1 * int2
                counter4 += 1

                Input.delete(0, 'end')
                Input.insert(100, Multi_Super_int)

            if counter4 >= 1 and Multi_counter >= 1:
                int2 = ipt.split("*")[-1]

                int2 = int(int2)

                Multi_Super_int = Multi_Super_int * int2
                counter4 += 1

                Input.delete(0, 'end')
                Input.insert(100, Multi_Super_int)

def Clear():
    Input.delete(0, 'end')

Clear = Button(Main_Frame, text="C", font="Consolas 19 bold", border=0, bg="#db6565", command=Clear)
Clear.grid(column=0, row=2)

One = Button(Main_Frame, text="1", font="Consolas 19 bold", border=0, bg="gray", command=One)
One.grid(column=1, row=2)

Two = Button(Main_Frame, text="2", font="Consolas 19 bold", border=0, bg="gray", command=Two)
Two.grid(column=2, row=2)

Three = Button(Main_Frame, text="3",font="Consolas 19 bold", border=0, bg="gray", command=Three)
Three.grid(column=3, row=2)

Plus = Button(Main_Frame, text="+", font="Consolas 19 bold", border=0, bg="gray", command=Plus)
Plus.grid(column=0, row=3)

Equal = Button(Main_Frame, text="=", font="Consolas 19 bold", border=0, bg="#77aed9", command=Equal)
Equal.grid(column=4, row=2)

Four = Button(Main_Frame, text="4", font="Consolas 19 bold", border=0, bg="gray", command=Four)
Four.grid(column=1, row=3)

Five = Button(Main_Frame, text="5", font="Consolas 19 bold", border=0, bg="gray", command=Five)
Five.grid(column=2, row=3)

Six = Button(Main_Frame, text="6", font="Consolas 19 bold", border=0, bg="gray", command=Six)
Six.grid(column=3, row=3)

Minus = Button(Main_Frame, text="-", font="Consolas 19 bold", border=0, bg="gray", command=Minus)
Minus.grid(column=4, row=3)

Multi = Button(Main_Frame, text="*", font="Consolas 19 bold", border=0, bg="gray", command=Multi)
Multi.grid(column=0, row=4)

Seven = Button(Main_Frame, text="7", font="Consolas 19 bold", border=0, bg="gray", command=Seven)
Seven.grid(column=1, row=4)

Eight = Button(Main_Frame, text="8", font="Consolas 19 bold", border=0, bg="gray", command=Eight)
Eight.grid(column=2, row=4)

Nine = Button(Main_Frame, text="9", font="Consolas 19 bold", border=0, bg="gray", command=Nine)
Nine.grid(column=3, row=4)

Devi = Button(Main_Frame, text="/", font="Consolas 19 bold", border=0, bg="gray", command=Devi)
Devi.grid(column=4, row=4)

Zero = Button(Main_Frame, text="0", width=7, font="Consolas 19 bold", border=0, bg="gray", command=Zero)
Zero.grid(column=0, row=5, columnspan=5)


root.mainloop()

