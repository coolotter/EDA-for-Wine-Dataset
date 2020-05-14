# Exploratory Data Analysis for Wine Dataset

# Motivation
Exploratory data analysis (EDA) is one of the most crucial part in data science, yet it is often overlook. Yes, algorithm is fun, but we need to look closely to our data in order to derive important insights 

Here, I have provided an example of EDA on a famous dataset: wine quality dataset. This dataset can be found here: https://archive.ics.uci.edu/ml/datasets/wine+quality. We can get essential information regarding our data prior to analysis
# Prerequisites
To view this project properly, you're recommended to have the latest versions of the followings:
* [Python 3](https://www.python.org/downloads/)
* [Jupyter Notebook](https://jupyter.org/index.html)
* [Pandas](https://pandas.pydata.org)
* [Reverse Geocoder](https://github.com/thampiman/reverse-geocoder)
* [Matplotlib](https://matplotlib.org)
* [Seaborn](https://seaborn.pydata.org)

# Files
In this repo, there is only one file:
- winedataset.ipynb

The file contains all the code ran for the project and some notes. 

# Project Summary
Here we are trying to derive some insights from our dataset just by using EDA. We will try to answer the following questions:
-How does the data look?
-How does our data correlate with one and another 
-What are other interesting relationships that can be derived from exploring the data?


# Summary
Some of the insights from EDA:
- If we look at our table and box plot, our pH values fall between 2.74–4.01, which falls under "acidic" category.
50 percent of our dataset for pH falls within a very narrow range, this can be illustrated by our boxplot. Looking at our summary table, our interquartile range falls between 3.21–3.40. That's only 0.79 difference between the upper and lower quartile, very small change in pH! 
- The lack of correlation between pH and our data might have something to do with the fact that all of our dataset falls under the "acidic" category. This is why we see pH having little impact to the quality of the wine. 
- However, one interesting thing to note is that the type of acid might impact the quality of wine, this is demonstrated through our correlation matrix. 
- Volatile acidity (or acetic acid) has a negative correlation with wine. Acetic acid is the main ingredient for vinegar, it would make sense that higher concentration of acetic acid might negatively impact the taste and hence the quality.
- Despite standardizing acid data, we still don't have different result on our volatile acidity vs. pH. This is odd because the higher acid concentration we have, technically we would have lower pH. We can still argue that the range of pH still falls under "acidic" category anyway.
- Additionally, volatile acid is inversely correlated with fixed acidity and citric acid, why is that? We can also see that fixed acidity and citric acid is positively correlated to each other. Does this also explain the fact that the pH goes up when citric acid concentration goes up?
- Alcohol is the most strongly correlated with quality of wine and also inversely correlated with density. Let's try to think about this: the alcohol in wine is ethyl alcohol and it has a density of 0.7892 g/mL. On the other hand, water has a density of 1 g/mL . So our finding makes sense: the more alcohol we have, the less dense our wine will be due to the difference in density between ethyl alcohol and water.
Through EDA, we have derived all of those informations that can be useful for future analysis. To learn more, please refer to the notebook, you will see the graphs and code. 

# Licensing, Authors and  Acknowledgements
The dataset comes from: https://archive.ics.uci.edu/ml/datasets/wine+quality. Acknowledgement to UCI for providing the data

