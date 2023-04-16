#!/usr/bin/env python
# coding: utf-8

# # Exploration des données de l'entreprise Sell4All :

# # Réalisé par Abdellah Badou

# # Introduction :

# Cette base de données contient des informations sur les utilisateurs (clients), et leurs dépenses sur le site Web de Sell4All. Avec 505 lignes et 11 colonnes.

# Importation des bibliothèques :

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# Informations sur les 5 premières lignes du fichier CSV :

# In[4]:


Sell4All_data = pd.read_csv('dataset-sell4all.csv')
Sell4All_data.head(5)


# Résumé technique des données :

# In[5]:


print('Forme de la base de données : {}\n'.format(Sell4All_data.shape))
print('Nombre de lignes : ', len(Sell4All_data.index))
print('\nLes types de données des champs du fichier CSV :\n')
Sell4All_data.info()


# # Explication :

# D'apres le résumé technique on a 505 lignes et 11 colonnes, 7 colonnes sont qualitatives, 2 colonnes sont quantitatives (Age : entier naturel), Customer spendings : entier naturel) et les 2 autres sont temporelles (Last date of connection, Last time of connection). Ainsi toutes les valeurs sont non nulles (non null).

# La moyenne de la colonne Age :

# In[6]:


Sell4All_data['Age'].mean()


# La médiane de la colonne Age :

# In[8]:


Sell4All_data['Age'].median()


# La moyenne de la colonne Customer spendings :

# In[9]:


Sell4All_data['Customer spendings'].mean()


# La médiane de la colonne Customer spendings :

# In[10]:


Sell4All_data['Customer spendings'].median()


# La médiane d’âge pour chaque pays :

# In[11]:


Sell4All_data.groupby('Country')['Age'].median()


# Visualisation des données du graphique à barres qui montre les dépenses des clients par pays :

# In[12]:


country = Sell4All_data['Country'].head(300)
customer_spendings = Sell4All_data['Customer spendings'].head(300)

plt.figure(figsize = (12, 8))

plt.barh(country, customer_spendings)

plt.xlabel('Countrys')
plt.ylabel('Customers spendings');

plt.show()


# # Interprétation du graphique :

# On constate qu'il y a des pays où les dépenses des clients sont très inférieures par rapport aux autres (moins de 400 €) par exemple (United Kingdom, Norway, Belgium).

# Suppression de toutes les lignes d'utilisateurs ayant dépensé moins de 10 € sur le site :

# In[13]:


Sell4All_data.drop(Sell4All_data.index[Sell4All_data['Customer spendings'] < 10])


# Remarque : Ona 3 lignes dont la dépense du client est moins de 10 € sur le site.

# Suppression de toutes les lignes qui apparaissent plus d’une fois dans les données :

# In[14]:


Sell4All_data.drop_duplicates()


# In[15]:


column_list = ['Country','Age','Gender','Customer spendings']

Sell4All_data.to_csv('Abdellah_Badou.csv', index=False, columns = column_list, sep='|')


# In[ ]:




