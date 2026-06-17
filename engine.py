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
def get_player_average_displacement(player):
    global df
    player-=1
    x=df.iloc[player::3][0].mean()
    y=df.iloc[player::3][1].mean()
    return (x,y)
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
        elif num==5:plot1_5()

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

def plot1_5():
    global df
    xs=np.array(["Player 1","Player 2","Player 3"])
    y0=[0,0,0]
    y1=[0,0,0]
    y5=[0,0,0]
    y10=[0,0,0]
    
    for ind in range( len(df)):
        player=ind%3+1
        score=get_score(df.iloc[ind][0],df.iloc[ind][1])
        if score==0:y0[player-1]+=1
        if score==1:y1[player-1]+=1
        if score==5:y5[player-1]+=1
        if score==10:y10[player-1]+=1
    y0=np.array(y0)
    y1=np.array(y1)
    y5=np.array(y5)
    y10=np.array(y10)

    plt.bar(xs,y0,label="0 Points",color="purple")
    plt.bar(xs,y1,label="1 Points",color="green",bottom=y0)
    plt.bar(xs,y5,label="5 Points",color="blue",bottom=y0+y1)
    plt.bar(xs,y10,label="10 Points",color="red",bottom=y0+y1+y5)
    plt.title("Frequency of Hits")
    plt.legend(loc="best")
    plt.show()

def option2():
    global df
    p1=get_player_score(1)
    p2=get_player_score(2)
    p3=get_player_score(3)
    scrs=[p1,p2,p3]
    p1a=get_player_average_displacement(1)
    p2a=get_player_average_displacement(2)
    p3a=get_player_average_displacement(3)
    print(f"""--- OVERALL SCORES ---
Player 1: {p1}
Player 2: {p2}
Player 3: {p3}\n &""")
    time.sleep(1.5)
    print(f"""=== AVERAGE DISPLACEMENTS (x,y) ===
Player 1: ({p1a[0]:.4f},{p1a[1]:.4f})
Player 2: ({p2a[0]:.4f},{p2a[1]:.4f})
Player 3: ({p3a[0]:.4f},{p3a[1]:.4f})
""")
    print("Considering All stats\nThe Winner is")
    time.sleep(.5)
    print("The Winner is.")
    time.sleep(.5)
    print("The Winner is..")
    time.sleep(.5)
    print("The Winner is...")
    time.sleep(.5)
    print("The Winner is....")
    time.sleep(.5)
    print(f"The Winner is Player {scrs.index(max(scrs))+1}\nCongratulations Player {scrs.index(max(scrs))+1}, nice hits.\n")
    
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
        elif num==2:
            option2()



if __name__=="__main__":
    global df
    df=pd.read_csv("data.csv",header=None)
    main_menu()
