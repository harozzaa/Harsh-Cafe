import pyttsx3
from graphics import *
#A BILL MAKER FOR CUSTOMER WHICH HE CAN USE ON HIS OWN AND THEN SHOW THE BILL AT COUNTER TO GET ORDER

#START
#BRANDING
print(" "*93,"*\n"," "*91,"**\n"," "*90,"***\n"," "*89,"****\n"," "*88,"*****\n"," "*87,"******\n"," "*86,"*******\n",
      " "*85,"********\n"," "*84,"*********\n"," "*83,"**********\n"," "*82,"***********\n"," "*81,"************\n"," "*80,"*************")

print(" "*81,"HARSH'S  CAFE"," "*81)

print(" "*81,"*************\n"," "*80,"************\n"," "*80,"***********\n"," "*80,"**********\n"," "*80,"*********\n"," "*80,"********\n"," "*80,"*******\n",
      " "*80,"******\n"," "*80,"*****\n"," "*80,"****\n"," "*80,"***\n"," "*80,"**\n"," "*80,"*")
        
#WELCOMING
print("\nHello \nWelcome to Harsh's Cafe\nI hope you are doing well\n \nHere is an Menu for you ",
      "\nPlease choose the things you would like to have from Menu")

engine = pyttsx3.init()
engine.say("Hello")
engine. setProperty("rate", 130)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Welcome to Harsh's Cafe")
engine. setProperty("rate", 130)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("I hope you are doing well")
engine. setProperty("rate", 130)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Here is an Menu for you")
engine. setProperty("rate", 130)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Please choose the things you would like to have from Menu")
engine. setProperty("rate", 130)
engine.runAndWait()

#Dictionary
SNA={"VS":40,"CS":50,"GS":60,"SS":70,"BB":60,"CB":70,"MB":90,"SB":100,"GB":80,"ZB":90,"PB":90,"VP":80,"BP":100,"LP":130,"HP":200,"CT":20,
     "MT":30,"ST":40,"GT":40,"PT":50,"FC":40,"DC":45,"CC":60,"ES":70,"CO":80,"CL":20,"ST":30,"MF":40,"CS":40,"SS":50}
FOO={"VS":"Veggie Sandwich","CS":"Cheese Sandwich","GS":"Grill  Sandwich","SS":"H Spcl Sandwich",
     "BB":"Basic Burger","CB":"Chesseee Burger","MB":"MAdmax Burger","SB":"H Spcl Burger",
     "GB":"Garlic Bread","ZB":"MAnaza Garlic Bread","PB":"Palpuine Bread","VP":"Veg Pizza",
     "BP":"Chesse Burst Pizza","LP":"Grand Large Pizza","HP":"THE HHH PIZZA","CT":"Cream Tea",
     "MT":"Mint Tea","ST":"Masala Tea","GT":"Green Tea","PT":"Prime Tea","FC":"Filter Coffee",
     "DC":"Dark Coffee","CC":"Cold Coffee","ES":"Espresso","CO":"Cappucino","CL":"Cola",
     "ST":"Sprite","MF":"Mixed Fruit","CS":"Cherry Smoothie","SS":"Strawberry Slurpee"}
   


#MENU
print("_"*176)
print(" ")
print("*"*85,"MENU","*"*85)
print("_"*176)

print("\n")
print("_"*176)
print("Serial Number                                      CODE                           PRODUCT NAME                                        RATE(In ₹)                     ")
print("_"*176)

print("\nSnacks                                                 \n")
print("\nSandwich\n")
print("1)                                                 VS                            Veggie Sandwich                                         40 ")
print("2)                                                 CS                            Cheese Sandwich                                         50 ")
print("3)                                                 GS                            Grill  Sandwich                                         60 ")
print("4)                                                 SS                            H Spcl Sandwich                                         70 ")
print("\nBurgers\n")
print("5)                                                 BB                            Basic Burger                                            60 ")
print("6)                                                 CB                            Chesseee Burger                                         70 ")
print("7)                                                 MB                            MAdmax Burger                                           90 ")
print("8)                                                 SB                            H Spcl Burger                                           100 ")
print("\nGarlic Bread\n")
print("9)                                                 GB                            Garlic Bread                                            80 ")
print("10)                                                ZB                            MAnaza Garlic Bread                                     90 ")
print("11)                                                PB                            Palpuine Bread                                          90 ")
print("\nPizza\n")
print("12)                                                VP                            Veg Pizza                                               80 ")
print("13)                                                BP                            Chesse Burst Pizza                                      100 ")
print("14)                                                LP                            Grand Large Pizza                                       130 ")
print("15)                                                HP                            THE HHH PIZZA                                           200 ")
print("\nBeverages                                  ")   
print("\nCoffee\n")
print("16)                                                FC                            Fiter Coffee                                            40 ")
print("17)                                                DC                            Dark  Coffee                                            45 ")
print("18)                                                CC                            Cold Coffee                                             60 ")
print("19)                                                ES                            Espresso                                                70 ")
print("20)                                                CO                            Cappucino                                               80 ")
print("\nTea\n")  
print("21)                                                CT                            Cream Tea                                               20 ")
print("22)                                                MT                            Mint Tea                                                30 ")
print("23)                                                ST                            Masala Tea                                              40 ")
print("24)                                                GT                            Green Tea                                               40 ")
print("25)                                                PT                            Prime Tea                                               50 ")
print("\nCold Drink\n")  
print("26)                                                CL                            Cola                                                    20 ")
print("27)                                                ST                            Sprite                                                  30 ")
print("28)                                                MF                            Mixed Fruit                                             40 ")
print("29)                                                CS                            Cherry Smoothie                                         40 ")
print("30)                                                SS                            Strawberry Slurpee                                      50 ")

print("_"*176)
print("_"*176)

#LIST FOR ITEMS ORDERED
b=[]
g=[]

#ORDERING ITEMS
print("Enter the codes of the product below. Once you complete entering the codes enter 0")
engine = pyttsx3.init()
engine. setProperty("rate", 130)
engine.say("Enter the codes of the product below. Once you complete entering the codes enter 0")
engine.runAndWait()


for i in range (0,30):
    c=input("Enter the codes of the products you would like to have ?:")
    if c=="0":
        break
    else:
        b.append(SNA[c])
        g.append(FOO[c])

#TOTAL COST OF ORDER
total = 0


for ele in range(0, len(b)):
    total = total + b[ele]

#BILLING
    
T=('\n\n'.join(map(str, g)))
R=('\n\n'.join(map(str, b)))

print("You have ordered : ")
print(T)
print("You have to pay ₹",total)

P=str(T)
TB=str(total)
engine = pyttsx3.init()
engine. setProperty("rate", 130)
engine.say("You have ordered")
engine.runAndWait()

engine = pyttsx3.init()
engine. setProperty("rate", 130)
engine.say(T)
engine.runAndWait()

engine = pyttsx3.init()
engine. setProperty("rate", 130)
engine.say("You have to pay Rupees")
engine.runAndWait()

engine = pyttsx3.init()
engine. setProperty("rate", 130)
engine.say(TB)
engine.runAndWait()


#THE BILL

#WINDOW
win=GraphWin("PRoject", 500,830)
win.setBackground("red")

#LOGO
bcr=Point(250,100)
bc=Circle(bcr,100)
bc.setFill('light blue')
bc.draw(win)

hc=Text(bcr,"HARSH'S CAFE")
hc.setSize(20)
hc.setFill("blue")
hc.draw(win)

#BILL STATEMENT
mr=Rectangle(Point(20,220),Point(480,800))
mr.setFill("light green")
mr.draw(win)

mt1=Text(Point(150,260),"PRODUCT")
mt1.setFill("red")
mt1.draw(win)

mt2=Text(Point(350,260),"RATE")
mt2.setFill("red")
mt2.draw(win)

mt3=Text(Point(150,480),T)
mt3.draw(win)

mt4=Text(Point(350,480),R)
mt4.draw(win)

#TOTAL BILL
tb=Rectangle(Point(40,680),Point(460,710))
tb.setFill("gold")
tb.draw(win)

tb1=Text(Point(100,695),"TOTAL COST :")
tb1.setFill("red")
tb1.draw(win)

tb3=Text(Point(350,695),"₹")
tb3.setFill("red")
tb3.draw(win)

tb2=Text(Point(400,695), total)
tb2.setFill("red")
tb2.draw(win)

#WISHES
W=Text(Point(250,755),"ENJOY  YOUR  MEAL\nTHANK YOU  FOR  VISIT\nHAVE  A  NICE  DAY ")
W.setFill("blue")
W.draw(win)

#THE END
















     


    
