import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class Insights:
	def __init__(self, data):
		self.data = data

	def automate_analysis(self):
		print("\n")
		print("The Dataset has {} rows & {} columns \n".format(self.data.shape[0],self.data.shape[1]))
		print("\n**********************************************************\n")
		print(self.data.info())
		print("\n**********************************************************\n")
	
		print("The following are the plots for categorical columns: \n")	
		for i in self.data.columns:
			if self.data[i].dtypes == object:
				df = pd.DataFrame(self.data[i].value_counts().sort_values(ascending=False).head(20))
				plot1= df.plot(kind='bar',figsize=(12,6))
				plt.xlabel(i,fontsize=15)
				plt.ylabel('Frequency',fontsize=15)
				plt.yscale('log')
				plt.xticks(fontsize=12)
				plt.show(plot1)	
				print("\n {} has {} unique values and {} percentage of null values \n".
				      format(i,self.data[i].nunique(),round((self.data[i].isna().sum()/self.data.shape[0])*100,3)))
		
		print("The following are the plots for numeric columns: \n")
		for i in self.data.columns:
			if self.data[i].dtypes != object:
				plt.figure(figsize=(12,9))
				plot2= sns.distplot(self.data[i], bins = 25, kde = False)
				plt.xlabel(i,fontsize=15)
				plt.ylabel('Frequency',fontsize=15)
				plt.yscale('log')
				plt.xticks(fontsize=12)
				plt.show(plot2)
				print("\n {} has {} unique values and {} percentage of null values \n".
				      format(i,self.data[i].nunique(),round((self.data[i].isna().sum()/self.data.shape[0])*100,3)))	

		print("The following is the heatmap to show the NA values in columns")
		plt.figure(figsize=(12,9))
		plot3 = sns.heatmap(self.data.isnull(), cbar=False)
		plt.show(plot3)
