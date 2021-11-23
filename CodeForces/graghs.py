import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    "product name" : ["mouse", "keypad"],
    "purchase amount" : [2400,1320],
    "sale amount" : [2880,1620]
} # add your rest of the data

df = pd.DataFrame(data)

df.head()

df.plot(
    kind = "bar",
    x = "product name", # refer Q2.1
    y = ["purchase amount" , "sale amount"],
    color = ["green" , "red" ] # refer Q2.5
)
plt.xlabel("Product Name") # refer Q2.2
plt.ylabel("Amount") # refer Q2.3
plt.title("Item Details") # refer Q2.4
plt.show()