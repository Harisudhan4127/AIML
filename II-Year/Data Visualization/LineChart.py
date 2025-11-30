# HSC Mark Trend Line Chart

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data\AIML_Data.csv")

plt.plot(df["S_No"], df["HSC"])
plt.title("HSC Mark Trend")
plt.xlabel("S_No")
plt.ylabel("HSC Marks")
plt.show()
