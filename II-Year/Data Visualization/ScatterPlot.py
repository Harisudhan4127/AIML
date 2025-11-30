# Scatter Plot - HSC vs Enroll

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data\AIML_Data.csv")

plt.scatter(df["Enroll"], df["HSC"])
plt.title("Enroll No vs HSC Marks")
plt.xlabel("Enroll No")
plt.ylabel("HSC Marks")
plt.show()
