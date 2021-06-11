#%%
import pandas as pd

dataset = pd.read_csv("data.csv")
x_coord = dataset["Height"].values.reshape(-1, 1)
y_coord = dataset["Weight"].values

#%%
from sklearn.linear_model import LinearRegression
model_LinearRegression = LinearRegression()
model_LinearRegression.fit(x_coord, y_coord)

#%%
import matplotlib.pyplot as plt
plt.scatter(x_coord, y_coord, color="green", linewidth=4)
plt.plot(x_coord, model_LinearRegression.predict(x_coord), color="blue", linewidth=3)
plt.show