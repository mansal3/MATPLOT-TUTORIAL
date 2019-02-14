#MATPLOT
#Matplot is the python pakcage used for 2D data graphics,It is used for Data Visualisation
# One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data
# in easily digestible visuals. Matplotlib consists of several plots like line, bar, scatter, histogram etc.
#
# Various Types of Plot:
# Histogram
# Barplot
# Scatter plot
# Hexagonal bin plot
# Area plot
# pieplot


from matplotlib import pyplot as plt


plt.plot([1,2,3],[4,5,1])
plt.show()

#now lets add some style in our graoh

from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

# #add color and other style
# from matplotlib import style
# style.use('ggplot')
# x=[2,3,4,5,6]
# y=[5,6,7,3,5]
#
# x1=[3,4,6,2]
# y1=[2,6,7,3,1,3,4]
# plt.plot(x,y,'g',label="line1",linewidth=5)
# plt.plot(x1,y1,'c',label="line2",linewidth=5)
# plt.title("line graph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
x = [ 5 , 2 , 9 , 4 , 7 ]

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot the bar
plt.bar ( x , y )

# function to show the plot
plt.show ()


# importing matplotlib module
from matplotlib import pyplot as plt

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot histogram
plt.hist ( y )

# Function to show the plot
plt.show ()

# x-axis values
x = [ 5 , 2 , 9 , 4 , 7 ]

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot scatter
plt.scatter ( x , y )

# function to show the plot
plt.show ()

# importing matplotlib module
from matplotlib import pyplot as plt

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot histogram
plt.hist ( y )

# Function to show the plot
plt.show ()

# x-axis values
x = [ 5 , 2 , 9 , 4 , 7 ]

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot scatter
plt.stackplot ( x , y )

# function to show the plot
plt.show ()

# importing matplotlib module
from matplotlib import pyplot as plt

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot histogram
plt.hist ( y )

# Function to show the plot
plt.show ()

# x-axis values
x = [ 5 , 2 , 9 , 4 , 7 ]

# Y-axis values
y = [ 10 , 5 , 8 , 4 , 2 ]

# Function to plot scatter
plt.pie ( x , y )

# function to show the plot
plt.show ()