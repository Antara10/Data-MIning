
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_excel(r"C:\Users\bipro\OneDrive\Documents\Data Mining\Association Rule Mining\my k-means dataset.xlsx")

df.head()

plt.scatter(df['AGE'], df['DATA MINING'])

km = KMeans(n_clusters = 6)

y_predicted = km.fit_predict(df[['AGE', 'DATA STRUCTURE', 'MACHINE LEARNING', 'SOFTWARE ENGINEERING', 'DATA MINING']])

y_predicted 

df['CLUSTER'] = y_predicted

df.head()

df1 = df[df.CLUSTER==0]
df2 = df[df.CLUSTER==1]
df3 = df[df.CLUSTER==2]
df4 = df[df.CLUSTER==3]
df5 = df[df.CLUSTER==4]
df6 = df[df.CLUSTER==5]

plt.scatter(df1.AGE, df1['DATA MINING'], color='green')
plt.scatter(df2.AGE, df2['DATA MINING'], color='red')
plt.scatter(df3.AGE, df3['DATA MINING'], color='blue')
plt.scatter(df4.AGE, df4['DATA MINING'], color='yellow')
plt.scatter(df5.AGE, df5['DATA MINING'], color='grey')
plt.scatter(df6.AGE, df6['DATA MINING'], color='pink')

plt.xlabel('Age')
plt.ylabel('Marks')
plt.legend()   
