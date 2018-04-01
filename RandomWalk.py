'''
Created on Mar 23, 2018

@author: Olivia Chan
Goal 1 : Complete the last module of  DataCamp's Intermediate Python for Data Science course
Goal 2: Add to the complexity of the task by adding a 2nd dimension to the question: 
             Have a 50 x 50 square. When is the visitor, who starts in the middle, going to reach any of the 4 sides?
Goal 3: Generating additional statistical values 
'''
#Import all necessary packages/libraries
from random import seed, randint
import pandas as pd

#set the seed, in this case, to everyone's favorite number
seed(31415)

#define starting coordinates, df
n=1;
start = [1,1]
walk=[]
allwalks=[]
df=pd.DataFrame()

n=int(input("Enter integer length of the traversable square:"))
start=[int(n/2),int(n/2)]
walk.append(start)
print(walk)

step=int(input("How large can each step be? Please enter an integer value: "))

def move2D(n, l=[]):
    xrand= l[-1][0]+randint(1,n)
    yrand = l[-1][1]+randint(1,n)
    l.append([xrand,yrand])

def run(n,step,l=[]):
    while(l[-1][0]>0 and l[-1][0]<(n-1) and l[-1][1]>0 and l[-1][1]<(n-1)):
        move2D(step, l)


cases=int(input("How many cases do you want to generate? Please enter an integer value:"))
print("Now generating cases and adding them to a DataFrame \n")

for i in range(cases):
    run(n,step,walk)
    df = df.append(walk, ignore_index= True)
    allwalks.append(walk)
    walk=[start]

df = pd.DataFrame(allwalks)
print(df)




