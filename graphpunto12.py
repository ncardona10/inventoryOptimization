import pandas as pd 
import seaborn as sns 

df = pd.read_csv("punto12.dat",delimiter = " ")
df.set_index("Bloque")

# print(df)
df = df.pivot("s_min", "s_max", "xyu")
ax = sns.heatmap(df, linewidths=.5,annot=True,cmap="YlGnBu")
fig = ax.get_figure()
fig.savefig("punto12.png")