#%%
import pandas as pd
#IMPORT DATA
dataset1 = pd.read_csv("Vaccine_Data_AB.csv")
dataset2 = pd.read_csv("Vaccine_Data_BC.csv")
dataset3 = pd.read_csv("Vaccine_Data_MB.csv")
dataset4 = pd.read_csv("Vaccine_Data_NB.csv")
dataset5 = pd.read_csv("Vaccine_Data_NL.csv")
dataset6 = pd.read_csv("Vaccine_Data_NS.csv")
dataset7 = pd.read_csv("Vaccine_Data_ON.csv")
dataset8 = pd.read_csv("Vaccine_Data_PE.csv")
dataset9 = pd.read_csv("Vaccine_Data_QC.csv")
dataset10 = pd.read_csv("Vaccine_Data_SK.csv")


#INTIALIZE DATA
x1 = dataset1["Days since December 19, 2020"].values.reshape(-1, 1)
y1 = dataset1["%full"].values
x2 = dataset2["Days since December 19, 2020"].values.reshape(-1, 1)
y2 = dataset2["%full"].values
x3 = dataset3["Days since December 19, 2020"].values.reshape(-1, 1)
y3 = dataset3["%full"].values
x4 = dataset4["Days since December 19, 2020"].values.reshape(-1, 1)
y4 = dataset4["%full"].values
x5 = dataset5["Days since December 19, 2020"].values.reshape(-1, 1)
y5 = dataset5["%full"].values
x6 = dataset6["Days since December 19, 2020"].values.reshape(-1, 1)
y6 = dataset6["%full"].values
x7 = dataset7["Days since December 19, 2020"].values.reshape(-1, 1)
y7 = dataset7["%full"].values
x8 = dataset8["Days since December 19, 2020"].values.reshape(-1, 1)
y8 = dataset8["%full"].values
x9 = dataset9["Days since December 19, 2020"].values.reshape(-1, 1)
y9 = dataset9["%full"].values
x10 = dataset10["Days since December 19, 2020"].values.reshape(-1, 1)
y10 = dataset10["%full"].values

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

model_LinearRegression4 = LinearRegression()
model_LinearRegression4.fit(x4, y4)
slope4 = (model_LinearRegression4.coef_)
intercept4 = (model_LinearRegression4.intercept_)

model_LinearRegression5 = LinearRegression()
model_LinearRegression5.fit(x5, y5)
slope5 = (model_LinearRegression5.coef_)
intercept5 = (model_LinearRegression5.intercept_)

model_LinearRegression6 = LinearRegression()
model_LinearRegression6.fit(x6, y6)
slope6 = (model_LinearRegression6.coef_)
intercept6 = (model_LinearRegression6.intercept_)

model_LinearRegression7 = LinearRegression()
model_LinearRegression7.fit(x7, y7)
slope7 = (model_LinearRegression7.coef_)
intercept7 = (model_LinearRegression7.intercept_)

model_LinearRegression8 = LinearRegression()
model_LinearRegression8.fit(x8, y8)
slope8 = (model_LinearRegression8.coef_)
intercept8 = (model_LinearRegression8.intercept_)

model_LinearRegression9 = LinearRegression()
model_LinearRegression9.fit(x9, y9)
slope9 = (model_LinearRegression9.coef_)
intercept9 = (model_LinearRegression9.intercept_)

model_LinearRegression10 = LinearRegression()
model_LinearRegression10.fit(x10, y10)
slope10 = (model_LinearRegression10.coef_)
intercept10 = (model_LinearRegression10.intercept_)

# INTERSECTION CALCULATION

# try to only graph the ones that intersect rather than every
#  possible intersection
x12 = (intercept2 - intercept1) / (slope1 - slope2)
y12 = (slope1 * x12) + intercept1
x13 = (intercept3 - intercept1) / (slope1 - slope3)
y13 = (slope1 * x13) + intercept1
x14 = (intercept4 - intercept1) / (slope1 - slope4)
y14 = (slope1 * x14) + intercept1
x15 = (intercept5 - intercept1) / (slope1 - slope5)
y15 = (slope1 * x15) + intercept1
x16 = (intercept6 - intercept1) / (slope1 - slope6)
y16 = (slope1 * x16) + intercept1
x17 = (intercept7 - intercept1) / (slope1 - slope7)
y17 = (slope1 * x17) + intercept1
x18 = (intercept8 - intercept1) / (slope1 - slope8)
y18 = (slope1 * x18) + intercept1
x19 = (intercept9- intercept1) / (slope1 - slope9)
y19 = (slope1 * x19) + intercept1
x110 = (intercept10 - intercept1) / (slope1 - slope10)
y110 = (slope1 * x110) + intercept1

x23 = (intercept3 - intercept2) / (slope2 - slope3)
y23 = (slope2 * x23) + intercept2
x24 = (intercept4 - intercept2) / (slope2 - slope4)
y24 = (slope2 * x24) + intercept2
x25 = (intercept5 - intercept2) / (slope2 - slope5)
y25 = (slope2 * x25) + intercept2
x26 = (intercept6 - intercept2) / (slope2 - slope6)
y26 = (slope2 * x26) + intercept2
x27 = (intercept7 - intercept2) / (slope2 - slope7)
y27 = (slope2 * x27) + intercept2
x28 = (intercept8 - intercept2) / (slope2 - slope8)
y28 = (slope2 * x28) + intercept2
x29 = (intercept9- intercept2) / (slope2 - slope9)
y29 = (slope2 * x29) + intercept2
x210 = (intercept10 - intercept2) / (slope2 - slope10)
y210 = (slope2 * x210) + intercept2
#%%

import matplotlib.pyplot as plt

#DATA PLOT
"""
plt.scatter(x1, y1, color="gray", linewidth=4) # Alberta
plt.scatter(x2, y2, color="grey", linewidth=4) # British Columbia  
plt.scatter(x3, y3, color="gray", linewidth=4) # Manitoba 
plt.scatter(x4, y4, color="gray", linewidth=4) # Bew Brunswick
plt.scatter(x5, y5, color="grey", linewidth=4) # Newfoundland & Labrador
plt.scatter(x6, y6, color="grey", linewidth=4) # Nova Scotia
plt.scatter(x7, y7, color="grey", linewidth=4)# Ontario
plt.scatter(x8, y8, color="grey", linewidth=4)# PEI
plt.scatter(x9, y9, color="grey", linewidth=4)# Quebec
plt.scatter(x10, y10, color="grey", linewidth=4)# Saskatchewan
"""
#TRENDLINE GRAPH
plt.plot(x1, model_LinearRegression1.predict(x1), color="#aec7e8", linewidth=3, label = "AB")
plt.plot(x2, model_LinearRegression2.predict(x2), color="#ffbb78", linewidth=3, label = "BC")
plt.plot(x3, model_LinearRegression3.predict(x3), color="#98df8a", linewidth=3, label = "MB") 
plt.plot(x4, model_LinearRegression4.predict(x4), color="#ff988c", linewidth=3, label = "NB")
plt.plot(x5, model_LinearRegression5.predict(x5), color="#c5b0d5", linewidth=3, label = "NL") 
plt.plot(x6, model_LinearRegression6.predict(x6), color="#f7b6d2", linewidth=3, label = "NS") 
plt.plot(x7, model_LinearRegression7.predict(x7), color="#dbdb8d", linewidth=3, label = "ON") 
plt.plot(x8, model_LinearRegression8.predict(x8), color="#9edae5", linewidth=3, label = "PE") 
plt.plot(x9, model_LinearRegression9.predict(x9), color="#729ece", linewidth=3, label = "QC") 
plt.plot(x10, model_LinearRegression10.predict(x10), color="#8c564b", linewidth=3, label = "SK") 
plt.scatter(x12, y12, color="black")
plt.scatter(x13, y13, color="black")
plt.scatter(x14, y14, color="black")
plt.scatter(x15, y15, color="black")
plt.scatter(x16, y16, color="black")
plt.scatter(x17, y17, color="black")
#plt.scatter(x18, y18, color="blue")
plt.scatter(x19, y19, color="black")
plt.scatter(x110, y110, color="black")

#GRAPHING VISUAL
plt.title("Provincial growth of vaccinations since December 19, 2020")
plt.xlabel("Days since December 19, 2020")
plt.ylabel("Fully Vaccinated percent of population")
plt.legend(fontsize=7)

plt.tight_layout()
plt.show()

"""
To do
find the rest of the intersections for line3 with every line and so on
do intersection analysis
"""