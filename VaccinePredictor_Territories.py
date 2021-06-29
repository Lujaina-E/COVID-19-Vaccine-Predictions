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

occurance_up_YK = 0
occurance_down_YK = 0
occurance_up_NT = 0
occurance_down_NT = 0
occurance_up_NU = 0
occurance_down_NU = 0

print("Analysis Results:")
print("WARNING.")

if(x13 > 30):
    if(x23 > 30):
        occurance_up_YK = occurance_up_YK + 1
        occurance_up_NT = occurance_up_NT + 1
        occurance_down_NU = occurance_down_NU + 1
    elif(x23 < 30):
        occurance_up_YK = occurance_up_YK + 1
        occurance_up_NT = occurance_up_NT + 1
    else:
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NT = occurance_down_NT + 1

elif(x13 < 30):
    if(x23 > 30):
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NT = occurance_down_NT + 1
    elif(x23 < 30):
        occurance_up_NU = occurance_up_NU + 1
        occurance_down_YK = occurance_down_YK + 1
        occurance_down_NT = occurance_down_NT + 1

    else:
        occurance_up_NU = occurance_up_NU + 1
        occurance_down_NT = occurance_down_NT + 1
else:
    occurance_down_NU = occurance_down_NU + 1

if(x12 > 30):
    if(x23 > 30):
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NT = occurance_down_NT + 1
        occurance_down_NU = occurance_down_NU + 1
    elif(x23 < 30):
        occurance_down_NT = occurance_down_NT + 1
        occurance_up_NU = occurance_up_NU + 1

    else:
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NT = occurance_down_NT + 1
elif (x12 < 30):
    if(x23 > 30):
        occurance_down_NU = occurance_down_NU + 1
        occurance_up_NT = occurance_up_NT + 1

    elif(x23 < 30):
        occurance_down_YK = occurance_down_YK + 1
        occurance_up_NU = occurance_up_NU + 1
        occurance_up_NT = occurance_up_NT + 1

    else:
        occurance_up_NT = occurance_up_NT + 1
        occurance_down_YK = occurance_down_YK + 1

else:
    occurance_down_YK = occurance_down_YK + 1

if(x23 > 30):
    if(x12 < 30):
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NT = occurance_down_NT + 1

    elif(x12 > 30):
        occurance_down_NU = occurance_down_NU + 1
        occurance_up_YK = occurance_up_YK + 1
        occurance_up_NT = occurance_up_NT + 1

    else:
        occurance_up_YK = occurance_up_YK + 1
        occurance_down_NU = occurance_down_NU + 1

elif(x23 < 30):
    if(x12 < 30):
        occurance_up_NU = occurance_down_NU + 1

        occurance_down_YK = occurance_down_YK + 1
        occurance_down_NT = occurance_down_NT + 1    
    elif(x12 > 30):
        occurance_down_YK = occurance_down_YK + 1
        occurance_up_NT = occurance_up_NT + 1    

    else:
        occurance_down_YK = occurance_down_YK + 1
        occurance_up_NU = occurance_up_NU + 1
else:
    if(x12 > 30):
        occurance_up_NT = occurance_up_NT + 1    
        occurance_down_NU = occurance_down_NU + 1

    if (x12 < 30):
        occurance_up_NU = occurance_up_NU + 1
        occurance_down_NT = occurance_down_NT + 1    

if (occurance_up_YK > 1):
    occurance_up_YK = 1
if (occurance_down_YK > 1):
    occurance_down_YK = 1
if (occurance_up_NT > 1):
    occurance_up_NT = 1
if (occurance_down_NT > 1):
    occurance_down_NT = 1
if (occurance_up_NU > 1):
    occurance_up_NU = 1
if (occurance_down_NU > 1):
    occurance_down_NU = 1

if (occurance_up_YK == 1 and occurance_down_YK == 1):
    occurance_down_YK = 0
if (occurance_up_NT == 1 and occurance_down_NT == 1):
    occurance_down_NT = 0
if (occurance_up_NU == 1 and occurance_down_NU == 1):
    occurance_down_NU = 0

if (occurance_up_YK == 1):
    print("- increase rate of vaccinations in Yukon")
if (occurance_down_YK == 1):
    print("- decrease rate of vaccinations in Yukon")
if (occurance_up_NT == 1):
    print("- increase vaccination rates in the Northwest Territories")
if (occurance_down_NT == 1):
    print("- decrease vaccination rates in the Northwest Territories")
if (occurance_up_NU == 1):
    print("- increase vaccination rates in Nunavut")
if (occurance_down_NU == 1):
    print("- decrease vaccination rates in Nunavut")
