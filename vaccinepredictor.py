#%%
import pandas as pd
#IMPORT DATA
dataset1 = pd.read_csv("Vaccine_Data_AB.csv")
dataset2 = pd.read_csv("Vaccine_Data_BC.csv")
dataset3 = pd.read_csv("Vaccine_Data_MB.csv")
dataset4 = pd.read_csv("Vaccine_Data_NB.csv")
dataset5 = pd.read_csv("Vaccine_Data_NL.csv")
dataset6 = pd.read_csv("Vaccine_Data_NT.csv")
dataset7 = pd.read_csv("Vaccine_Data_NS.csv")
dataset8 = pd.read_csv("Vaccine_Data_NU.csv")
dataset9 = pd.read_csv("Vaccine_Data_ON.csv")
dataset10 = pd.read_csv("Vaccine_Data_PE.csv")
dataset11 = pd.read_csv("Vaccine_Data_QC.csv")
dataset12 = pd.read_csv("Vaccine_Data_SK.csv")
dataset13 = pd.read_csv("Vaccine_Data_YT.csv")



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
x11 = dataset11["Days since December 19, 2020"].values.reshape(-1, 1)
y11 = dataset11["%full"].values
x12 = dataset12["Days since December 19, 2020"].values.reshape(-1, 1)
y12 = dataset12["%full"].values
x13 = dataset13["Days since December 19, 2020"].values.reshape(-1, 1)
y13 = dataset13["%full"].values

# %%
from sklearn.linear_model import LinearRegression
model_LinearRegression1 = LinearRegression()
model_LinearRegression1.fit(x1, y1)
model_LinearRegression2 = LinearRegression()
model_LinearRegression2.fit(x2, y2)
model_LinearRegression3 = LinearRegression()
model_LinearRegression3.fit(x3, y3)
model_LinearRegression4 = LinearRegression()
model_LinearRegression4.fit(x4, y4)
model_LinearRegression5 = LinearRegression()
model_LinearRegression5.fit(x5, y5)
model_LinearRegression6 = LinearRegression()
model_LinearRegression6.fit(x6, y6)
model_LinearRegression7 = LinearRegression()
model_LinearRegression7.fit(x7, y7)
model_LinearRegression8 = LinearRegression()
model_LinearRegression8.fit(x8, y8)
model_LinearRegression9 = LinearRegression()
model_LinearRegression9.fit(x9, y9)
model_LinearRegression10 = LinearRegression()
model_LinearRegression10.fit(x10, y10)
model_LinearRegression11 = LinearRegression()
model_LinearRegression11.fit(x11, y11)
model_LinearRegression12 = LinearRegression()
model_LinearRegression12.fit(x12, y12)
model_LinearRegression13 = LinearRegression()
model_LinearRegression13.fit(x13, y13)


#%%

#DATA PLOT
import matplotlib.pyplot as plt
plt.scatter(x1, y1, color="gray", linewidth=4) # Alberta
plt.scatter(x2, y2, color="grey", linewidth=4) # British Columbia  
plt.scatter(x3, y3, color="gray", linewidth=4) # Manitoba 
plt.scatter(x4, y4, color="gray", linewidth=4) # Bew Brunswick
plt.scatter(x5, y5, color="grey", linewidth=4) # Newfoundland & Labrador
plt.scatter(x6, y6, color="grey", linewidth=4) # Northwest Territories 
# the northwest territories are apparently doing really well on their vaccinations and its kind of screwing up my data
plt.scatter(x7, y7, color="grey", linewidth=4) # Nova Scotia
plt.scatter(x8, y8, color="grey", linewidth=4) # Nunavut
# Nunavut also has really high percentage rates
plt.scatter(x9, y9, color="grey", linewidth=4)# Ontario
plt.scatter(x10, y10, color="grey", linewidth=4)# PEI
plt.scatter(x11, y11, color="grey", linewidth=4)# Quebec
plt.scatter(x12, y12, color="grey", linewidth=4)# Saskatchewan
plt.scatter(x13, y13, color="grey", linewidth=4)# Yukon


#TRENDLINE GRAPH
plt.plot(x1, model_LinearRegression1.predict(x1), color="#383F51", linewidth=3, label = "AB")
plt.plot(x2, model_LinearRegression2.predict(x2), color="#DDDBF1", linewidth=3, label = "BC")
plt.plot(x3, model_LinearRegression3.predict(x3), color="#3C4F76", linewidth=3, label = "MB") 
plt.plot(x4, model_LinearRegression4.predict(x4), color="#D1BEB0", linewidth=3, label = "NB")
plt.plot(x5, model_LinearRegression5.predict(x5), color="#AB9F9D", linewidth=3, label = "NL") 
plt.plot(x6, model_LinearRegression6.predict(x6), color="#628B48", linewidth=3, label = "NT") 
plt.plot(x7, model_LinearRegression7.predict(x7), color="#6AB547", linewidth=3, label = "NS") 
plt.plot(x8, model_LinearRegression8.predict(x8), color="#EDD83D", linewidth=3, label = "NU") 
plt.plot(x9, model_LinearRegression9.predict(x9), color="#FCDE9C", linewidth=3, label = "ON") 
plt.plot(x10, model_LinearRegression10.predict(x10), color="#08B2E3", linewidth=3, label = "PE") 
plt.plot(x11, model_LinearRegression11.predict(x11), color="#90FFDC", linewidth=3, label = "QC") 
plt.plot(x12, model_LinearRegression12.predict(x12), color="#8C1C13", linewidth=3, label = "SK") 
plt.plot(x13, model_LinearRegression13.predict(x13), color="#C41E3D", linewidth=3, label = "YT") 


#GRAPHING VISUAL
plt.title("Growth of vaccinations since December 19, 2020")
plt.xlabel("Days since December 19, 2020")
plt.ylabel("Fully Vaccinated percent of provincial population")
plt.legend()
plt.show()

"""
Current problems
1. The legend is too long and covers the data
2. The values don't make sense to have negative ratios of the population who have been vaccinated
3. Should the data be plotted or just the trendlines... cluttering
4. The trendlines should be spaced out better, but cannot be bc
NU and NT percentages is too high
"""