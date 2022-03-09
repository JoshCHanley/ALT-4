import matplotlib.pyplot as plt
import numpy as np
PATH = 'C:/Users/Josh/OneDrive/Desktop/ALT/CSV files (Josh)/'

def loadData(fileName, path=PATH, floatconv=False):
    dataIn = open(f"{path}/{fileName}",'r').read()
    listOut = [i.replace('\n', '') for i in dataIn.split(',')]
    if floatconv:
        return [float(i) for i in listOut]
    return listOut

def barChart(listx, listy, title, rotation=30, size=8):
    plt.bar(listx, listy)
    plt.title(title)
    plt.xticks(rotation=rotation, size=size)
    plt.show()

areaList = loadData('Dublin Areas Thonny File.csv') # floatconv defaults False
crimeList = loadData('Dublin Crime Thonny File.csv', floatconv=True)
populationList = loadData('Dublin Population Thonny File.csv', floatconv=True)
populationDensityList = loadData('Dublin Population Density Thonny File.csv', floatconv=True)
crimeRateList = loadData('Dublin Crime Rate Thonny File.csv', floatconv=True)

barChart(areaList, crimeList, 'Incidences of Crime')
barChart(areaList, populationList, 'Population')
barChart(areaList, crimeRateList, 'Crime Rates (per 1000 people)')
barChart(areaList, populationDensityList, 'Population Density')

#Scatter plot and correlation coefficient between population density and crime rate

x = np.array(populationDensityList)
y = np.array(crimeRateList)
m, b = np.polyfit(x, y, 1)

rho = np.corrcoef(x,y)[0, 1]

plt.plot(x, y, 'o')
plt.plot(x, m*x + b)
plt.title('Correlation between Population Density and Crime Rate')
plt.xlabel('Population Density (Inhabitants per 1km²)')
plt.ylabel('Crime Rate (per 1000 people)')

box_style=dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.text(2500, 12.5, f'r = {rho:.03f}',{'color':'blue','weight':'heavy','size':10},bbox=box_style)

index = 0
for x,y in zip(x,y):

    label = areaList[index]
    index +=1
    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,15), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.show()
