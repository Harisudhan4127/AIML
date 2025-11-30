# Pie Chart Student Quota Distribution

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data\AIML_Data.csv")

quota_count = df["Quota"].value_counts()

plt.pie(quota_count, labels=quota_count.index, autopct="%1.1f%%")
plt.title("Student Quota Distribution")
plt.show()