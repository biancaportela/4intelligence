#%%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import missingno as msno


#%%%
df = pd.read_csv("F:/4intelligence/case_2/dados/UCI_Credit_Card.csv")

#%%
df.head()
# %%
df.shape
# %%
df.info()
# %%
df.duplicated().sum()

# %%
df.isnull().sum()
# %%
msno.matrix(df)

# %%
