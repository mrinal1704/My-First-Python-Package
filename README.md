# My-First-Python-Package

## Introduction
This repo contains the files of a python package developed by me which automates the task of getting basic insights from data. 

## Functions
This package helps in automating the following everyday tasks of data analysis:

      - Calculates the dimensions of the dataset
			- Shows the basic info of the data
			- Calculates number of Unique values
			- Calculates percentage of null values
			- Plots the bar chart for all categorical columns
			- Plots the histogram for all numeric columns
			- Makes a heatmap to show the null values
      
## How to install, import, and run
- You can either go to the link: https://test.pypi.org/project/Mrinal/#files
- Or download all the files in the repo and open command prompt in the same folder containing the
  setup.py file. 
  - Then execute "pip install ."
  - Then to import this in python, type "from Mrinal import Insights"
  - Then create an object: insight_1 = Insights(df) where df is the dataframe object of your data
  - Then run insight_1.automate_analysis(), this would execute all the above mentioned tasks
