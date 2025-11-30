# Bar Chart - HSC by Name
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data\AIML_Data.csv")

plt.bar(df["Name"], df["HSC"])
plt.title("HSC Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("HSC Marks")
plt.xticks(rotation=45)
plt.show()