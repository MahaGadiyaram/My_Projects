"""This code builds a recipe recommender based on the clusters of ingredients
Input is a list of ingredients and output is recipe information"""



##importing libraries

import pandas as pd
import json
import re
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import pprint
import warnings
warnings.simplefilter('ignore')
import pickle
from sklearn.cluster import KMeans
from sklearn import manifold
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
#import plotly.express as px
from matplotlib import pyplot as plt
#%matplotlib inline
import plotly.offline as py
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
#import time


##Import data

df_recipes= pd.read_csv('./final/recipe_kmeans.csv')
df_recipes['ingredients_parsed'] = df_recipes.ingredients_parsed.values.astype('U')
cluster_df=pd.read_csv('./final/cluster_df')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

##Call the KMeans model only once
with open('final_model.bin', 'rb') as fid:
    model = pickle.load(fid)


##defining recommender function
str_input=df_recipes.ingredients_parsed.to_list()

def cluster_predict(str_input):
    Y = tfidf.transform(list(str_input))
    cluster_nums = model.predict(Y)
    cluster_num=np.random.choice(cluster_nums)
    return cluster_num
#cluster_predict(['paneer','tomato','spinach'])

def recipe_predict(df_recipes,cluster_num,dish_type,min_time=5,max_time=60):
    if dish_type=='main dish':
        dish_type=1
    else:
        dish_type=0
    recipe_cluster=df_recipes[(df_recipes['clusters']==cluster_num)&(df_recipes['dish']==dish_type)]
    #print(recipe_cluster)
    recipe_title=recipe_cluster[(recipe_cluster['readyInMinutes']>=min_time) & (recipe_cluster['readyInMinutes']                                 <=max_time)][['title','ingredients','instructions','readyInMinutes','servings']].head(5)#.values
    #print(time_recipe)
    #recipe_ingredients=recipe_cluster[(recipe_cluster['readyInMinutes']>=min_time) & (recipe_cluster['readyInMinutes']<=max_time)]['ingredients'].values
    #recipe_title=time_recipe[time_recipe['Calories kcal']==time_recipe['Calories kcal'].min()]['title']
    #print(recipe_title)
    return recipe_title#,recipe_ingredients
#recipe_predict(df_recipes,0,'main dish',20,40) 

def recommender(str_input,dish_type,min_time=5,max_time=60):
    data=df_recipes
    cluster_num=cluster_predict(str_input)
    recipe_title=recipe_predict(data,cluster_num,dish_type,min_time,max_time)
    return recipe_title#['title']

if __name__=="__main__":
     print(recommender(['egg'],'breakfast',20,40))
