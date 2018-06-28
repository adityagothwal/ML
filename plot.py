#Matplotlib different graph plots

#PIE CHART 
import matplotlib.pyplot as plt

lables = 'Python', 'C++', 'Ruby', 'Java'

sizes = [240, 160, 225, 140]

colors = [ 'cyan', 'yellowgreen', 'orange', 'skyblue']

#Exploding the first slice
explode = (0.1, 0, 0, 0) 

plt.pie(sizes, explode=explode, labels=lables, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.show()

#BAR PLOT

#scores
x=[100,125,76,90]

#player names
y=["DK","The Wall","Dhoni","Yuvraj"]

plt.ylabel("Score")

plt.xlabel("Player Name")

plt.bar(y,x,label="Overs")

plt.legend()

plt.grid(color='r')

plt.show()

#Line Graph

x = [1,5]
y = [2,7]

x1 = [9,2]
y1 = [3,6]

plt.plot(x,y,label='river',c='skyblue')

plt.plot(x1,y1,label='grass',c='yellowgreen')

plt.xlabel("Time")

plt.ylabel("Speed")

plt.legend()

plt.grid(color='red')

plt.show()


#Scatter Plot

x = [2,2,7,1]
y = [4,8,9,0]

x1 = [3,5,10,9]
y1 = [3,7,12,4]

plt.scatter(x,y,label='river',c='blue',marker='x',s=120)

plt.scatter(x1,y1,label='grass',c='green',s=120)

plt.xlabel("Time")

plt.ylabel("speed")

plt.legend()

plt.grid(color='grey')

plt.show()











