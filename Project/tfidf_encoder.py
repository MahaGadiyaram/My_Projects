import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import config

# load in parsed recipe dataset 
df_recipes= pd.read_csv(config.PARSED_PATH)
df_recipes['ingredients_parsed'] = df_recipes.ingredients_parsed.values.astype('U')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])


