import pandas as pd
import numpy as np
import time 
import math
import matplotlib.pyplot as plt
def responce():
    while True:
        try:
            num=int(input("Enter your choice: "))
            return num
        except ValueError:
            print("\nERROR! Use numbers!")

def get_score(x,y):
    r= math.sqrt(x*x+y*y)
    if r<=1:return 10
    if r<=2:return 5
    if r<=3:return 1
    return 0

def get_player_score(player):
    global df
    player-=1 #easier for index
    player_score=0
    
    for ind in range(player, len(df),3):
        row=df.iloc[ind]
        x=row[0]
        y=row[1]
        player_score+=get_score(x,y)
    return player_score

def option1():
    while True:
        print("""1. Scatter plot for Player 1\n2. Scatter plot for Player 2\n3. Scatter plot for Player 3\n4. Scatter plot for all three players\n5. Stacked bar chart showing score distribution for each player\n6. Go back""")
        num=responce()  
        while num not in [1,2,3,4,5,6]:
            print("\nERROR! Use specified numbers!")
            num=responce()
        if num in [1,2,3]:
            plot1_123(num)
        elif num ==4:
            plot1_4()
        
        elif num==6:break

def plot1_123(player):
    global df
    player-=1
    xs=[]
    ys=[]
    for ind in range(player,len(df),3 ):
        row=df.iloc[ind]
        xs.append(row[0])
        ys.append(row[1])
    xs=np.array(xs)
    ys=np.array(ys)
    plt.scatter(xs,ys,color="black",marker="+",linewidths=1)

    ax=plt.gca()
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    plt.title(f"Dart Hits for Player {player+1}",color="red")
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    plt.show()

def plot1_4():
    global df
    x1=[]
    x2=[]
    x3=[]
    y1=[]
    y2=[]
    y3=[]
    for ind in range( 0,len(df)):
        row=df.iloc[ind]
        var=ind%3+1
        if var==1:
            x1.append(row[0])
            y1.append(row[1])
        if var==2:
            x2.append(row[0])
            y2.append(row[1])
        if var==3:
            x3.append(row[0])
            y3.append(row[1])
    plt.scatter(x1,y1,marker="+",color="black",linewidths=1,label="Player 1")
    plt.scatter(x2,y2,marker="x",c="green",linewidths=1,label="Player 2")
    plt.scatter(x3,y3,marker=".",c="blue",linewidths=1,label="Player 3")
    
    ax=plt.gca()
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    plt.legend(bbox_to_anchor=(1.1,1.1))#better this way
    plt.title("Dart Hits for All Players",c="red")
    plt.show()



def main_menu():
    while True:
        print("""Choose an option:\n1. Plots\n2. Analyse Data\n3. Exit""")
        num=responce()
        while num not in [1,2,3]:
            print("\nERROR! Use specified numbers!")
            num=responce()
        if num==3:
            print("Exiting")
            exit()
        elif num==1:
            option1()



    
def main():
    global df
    df=pd.read_csv("data.csv",header=None)
    main_menu()















if __name__=="__main__":
    main()
    print("\nDONE\n")
