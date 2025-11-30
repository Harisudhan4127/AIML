# Histogram - HSC Distribution

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data\AIML_Data.csv")

plt.hist(df["HSC"], bins=5)
plt.title("Histogram - HSC Distribution")
plt.xlabel("HSC")
plt.ylabel("Frequency")
plt.show()
