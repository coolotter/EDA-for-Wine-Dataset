
####Project 1 ND

#######PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import confusion_matrix


data = pd.read_csv('c:\datauv.csv')
datanp = np.array(data.iloc[:,1:10])
target= np.array(data.iloc[:,0])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(datanp)

#Principle Component Analysis
pca = PCA(n_components=2) #Create PCA using 10 components
X_pca = pca.fit_transform(X_scaled)
principalDf = pd.DataFrame(data=X_pca, columns=['principal component 1'
                       ,'principal component 2'])
finalDf = pd.concat([principalDf, data[['Classification']]], axis=1)
fig = plt.figure(figsize =(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize= 15)
ax.set_ylabel('Principal Component 2', fontsize= 15)
ax.set_title('2 component PCA', fontsize= 20)
targets = [' 1,2-Naphthylethylamine', 'Binary', 'Phenylethylamine']
colors = ['c', 'r', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['Classification']== target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'],
               c= color, s=50)
    ax.legend(targets)
    ax.grid()

print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

#Classification using LDA

y= np.array(data.iloc[:,0])
lda = LDA(n_components=2)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y,
                                                    test_size = .30,
                                                    random_state=42)

lda_object= lda.fit(X_train, y_train)
print(lda_object.score(X_test,y_test))


#Plotting LDA
X_r2= lda.fit(X_scaled, y).transform(X_scaled)
principalDf = pd.DataFrame(data=X_r2, columns=['LD1'
                       ,'LD2'])
finalDf = pd.concat([principalDf, data[['Classification']]], axis=1)
fig = plt.figure(figsize =(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('LD1', fontsize= 15)
ax.set_ylabel('LD2', fontsize= 15)
ax.set_title('LDA Scatter Plot', fontsize= 20)
targets = [' 1,2-Naphthylethylamine', 'Binary', 'Phenylethylamine']
colors = ['c', 'r', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['Classification']== target
    ax.scatter(finalDf.loc[indicesToKeep, 'LD1'],
               finalDf.loc[indicesToKeep, 'LD2'], c= color, s=50)
    ax.legend(targets)
    ax.grid()


plt.show()
#Confusion matrix
y_pred= lda_object.predict(X_test)
cm= confusion_matrix(y_test, y_pred)

ax= plt.subplot()
sns.heatmap(cm, annot=True); #annot=True to annotate cells
targets = ['Naphthyl', 'Binary', 'Phenyl']


# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax.set_title('Confusion Matrix');
ax.xaxis.set_ticklabels(targets);
ax.yaxis.set_ticklabels(targets);
