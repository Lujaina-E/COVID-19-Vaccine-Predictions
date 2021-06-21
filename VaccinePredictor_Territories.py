#%%
import pandas as pd
import numpy as np
#IMPORT DATA
dataset1 = pd.read_csv("Vaccine_Data_NT.csv")
dataset2 = pd.read_csv("Vaccine_Data_NU.csv")
dataset3 = pd.read_csv("Vaccine_Data_YT.csv")

#INTIALIZE DATA
x1 = dataset1["Days since December 19, 2020"].values.reshape(-1, 1)
y1 = dataset1["%full"].values
x2 = dataset2["Days since December 19, 2020"].values.reshape(-1, 1)
y2 = dataset2["%full"].values
x3 = dataset3["Days since December 19, 2020"].values.reshape(-1, 1)
y3 = dataset3["%full"].values
 # %%
from sklearn.linear_model import LinearRegression
#FITTING REGRESSION MODEL AND RETRIEVING GRAPH PROPERTIES
model_LinearRegression1 = LinearRegression()
model_LinearRegression1.fit(x1, y1)
slope1 = (model_LinearRegression1.coef_)
intercept1 = (model_LinearRegression1.intercept_)

model_LinearRegression2 = LinearRegression()
model_LinearRegression2.fit(x2, y2)
slope2 = (model_LinearRegression2.coef_)
intercept2 = (model_LinearRegression2.intercept_)

model_LinearRegression3 = LinearRegression()
model_LinearRegression3.fit(x3, y3)
slope3 = (model_LinearRegression3.coef_)
intercept3 = (model_LinearRegression3.intercept_)

# INTERSECTION CALCULATION
x12 = (intercept2 - intercept1) / (slope1 - slope2)
y12 = (slope1 * x12) + intercept1

x23 = (intercept3 - intercept2) / (slope2 - slope3)
y23 = (slope2 * x23) + intercept2

x13 = (intercept3 - intercept1) / (slope1 - slope3)
y13 = (slope1 * x13) + intercept1

#do some research on where the intersections should be, and place it here. 
# if statement will be for whether a warning sign is made to increase the 
# vaccines to a certain province. Consider both options to increase rates for one province or decrease rates for another province. 
#%%
import matplotlib.pyplot as plt

"""
#DATA PLOT
plt.scatter(x1, y1, color="black", linewidth=4)# Yukon
plt.scatter(x2, y2, color="grey", linewidth=4) # Nunavut
plt.scatter(x3, y3, color="blue", linewidth=4) # Northwest Territories 
#all three territories did really well on their vaccinations and its screwing up my data
"""

#TRENDLINE GRAPH
plt.plot(x1, model_LinearRegression1.predict(x1), color="#F9C80E", linewidth=3, label = "NT") 
plt.plot(x2, model_LinearRegression2.predict(x2), color="#253C78", linewidth=3, label = "NU") 
plt.plot(x3, model_LinearRegression3.predict(x3), color="#D36582", linewidth=3, label = "YT") 

#INTERSECTION PLOT
plt.scatter(x12, y12, color="black")
plt.scatter(x23, y23, color="black")
plt.scatter(x13, y13, color="black")

#GRAPHING VISUAL
plt.title("Territorial Growth of vaccinations since December 19, 2020")
plt.xlabel("Days since December 19, 2020")
plt.ylabel("Fully Vaccinated percent of population")
plt.legend(fontsize=7)

plt.tight_layout()
plt.show()

#INTERSECTION ANALYSIS
print("Analysis Results:")

print("WARNING.")
if(x13 > 30):
    if(x23 > 30):
        print("- increase rate of vaccinations in Yukon")
        print("- increase rate of vaccinations in the Northwest Territories")
        print("- decrease rate of vaccinations in Nunavut")
    elif(x23 < 30):
        print("- increase rate of vaccinations in Yukon")
        print("- increase rate of vaccinations in the Northwest Territories")
    else:
        print("- increase rate of vaccinations in Yukon")
        print("- decrease rate of vaccinations in the Northwest Territories")
elif(x13 < 30):
    if(x23 > 30):
        print("- increase rate of vaccinations in Yukon")
        print("- decrease rate of vaccinations in the Northwest Territories")
    elif(x23 < 30):
        print("- increase rate of vaccinations in Nunavut")
        print("- decrease rate of vaccinations in Yukon")
        print("- decrease rate of vaccinations in the Northwest Territories")
    else:
        print("- increase rate of vaccinations in Nunavut")
        print("- decrease rate of vaccinations in the Northwest Territories")
else:
    if(x23 > 30):
        print("- decrease rate of vaccinations in Nunavut")
    elif(x23 < 30):
        print("- decrease rate of vaccinations in Nunavut")


if(x12 > 30):
    if(x23 > 30):
        print("- increase rate of vaccinations in Yukon")
        print("- decrease vaccination rates in the Northwest Territories")
        print("- decrease vaccination rates in Nunavut")
    elif(x23 < 30):
        print("- decrease rate of vaccinations in the NorthWest Territories")
        print("- increase rate of vaccinations in Nunavut")
    else:
        print("- increase rate of vaccinations in Yukon")
        print("- decrease vaccination rates in the Northwest Territories")
elif (x12 < 30):
    if(x23 > 30):
        print("- decrease rate of vaccinations in Nunavut")
        print("- increase rate of vaccinations in the NorthWest Territories")
    elif(x23 < 30):
        print("- decrease rate of vaccinations in Yukon")
        print("- increase rate of vaccinations in Nunavut")
        print("- increase vaccination rates in the Northwest Territories")
    else:
        print("- increase vaccination rates in the Northwest Territories")
        print("- decrease rate of vaccinations in Yukon")
else:
    if(x23 > 30):
        print("- decrease rate of vaccinations in Yukon")
    if(x23 < 30):
        print("- decrease rate of vaccinations in Yukon")


if(x23 > 30):
    if(x12 < 30):
        print("- increase rate of vaccinations in Yukon")
        print("- decrease vaccination rates in the Northwest Territories")
    elif(x12 > 30):
        print("- decrease rate of vaccinations in Nunavut")
        print("- increase rate of vaccinations in Yukon")
        print("- increase vaccination rates in the Northwest Territories")
    else:
        print("- increase vaccination rates in Yukon")
        print("- decrease vaccination rates in Nunavut")
elif(x23 < 30):
    if(x12 < 30):
        print("- increase rate of vaccinations in Nunavut")
        print("- decrease vaccination rates in Yukon")
        print("- decrease vaccination rates in the Northwest Territories")
    elif(x12 > 30):
        print("- decrease rate of vaccinations in Yukon")
        print("- increase vaccination rates in the Northwest Territories")
    else:
        print("- decrease vaccination rates in Yukon")
        print("- increase vaccination rates in Nunavut")
else:
    if(x12 > 30):
        print("- increase vaccination rates in the Northwest Territories")
        print("- decrease vaccination rates in Nunavut")
    if (x12 < 30):
        print("- increase vaccination rates for Nunavut")
        print("- decrease vaccination rates for the Northwest Territories")

# to do: make sure suggestions only pop up once and aren't contradicting. 
# Use a count variable every time something has been printed. If 
# it has already been printed, do not print it again. 
