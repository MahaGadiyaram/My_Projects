### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import config
from PIL import Image
import recommender
import plotly.graph_objs as go
import plotly.tools as tls

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
#import plotly.express as px
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import plotly.offline as py


st.set_page_config(page_title="Spicy Recipe Recommender",page_icon=":stew:",layout='wide')

header = st.container()
intro=st.container()
data=st.container()
model=st.container()

import nltk

try:
    nltk.data.find("./ingredeints.png")
except LookupError:
    nltk.download("wordnet")


rad=st.sidebar.radio("Contents",["EDA","KMeans Clustering","Recommender"])

if rad=="EDA":
    with header:
        st.title("Analysis of Nutrition Data")

    with data:
        nutrition_df=pd.read_csv("./final/nutri_eda_df.csv")
        
        ax=nutrition_df.groupby(['title'])["Calories kcal"].min().sort_values(ascending=True).head(10)
        st.subheader("Top 10 Low Calorie Recipes")
        st.bar_chart(ax)

        ax2=nutrition_df.groupby(['title'])["Iron mg"].max().sort_values(ascending=False).head(10)
        st.subheader("Top 10 Iron rich Recipes")
        st.bar_chart(ax2)

        ax3=nutrition_df.groupby(['title'])["Vitamin D µg"].max().sort_values(ascending=False).head(10)
        st.subheader("Top 10 Vitamin D rich Recipes")
        st.bar_chart(ax3)

        ax4=nutrition_df.groupby(['title'])["Calcium mg"].max().sort_values(ascending=False).head(10)
        st.subheader("Top 10 Calcium rich Recipes")
        st.bar_chart(ax4)

if rad=="KMeans Clustering":
    with header:
        st.title("KMeans Plots")

    #with data:
        # load in parsed recipe dataset 
        df_recipes= pd.read_csv(config.PARSED_PATH)
        df_recipes['ingredients_parsed'] = df_recipes.ingredients_parsed.values.astype('U')

# TF-IDF feature extractor 
        tfidf = TfidfVectorizer()
        tfidf.fit(df_recipes['ingredients_parsed'])
        tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

#PCA
        pca = PCA(n_components=5)
        X = pca.fit_transform(tfidf_recipe.todense())

        pca_df=pd.DataFrame(pca.explained_variance_ratio_)
        #st.bar_chart(pca_df)


        model = KMeans(n_clusters=10, random_state=20)
        clusters=model.fit_predict(tfidf_recipe)


        #recipe_kmeans=pd.read_csv("./final/recipe_kmeans.csv")
        #data =recommender.df_recipes
        st.header('KMeans Clusters')
        #st.subheader('Pairplot analysis')
        trace_Kmeans = go.Scatter(x=X[:, 0], y= X[:, 1], mode="markers",
                    showlegend=False,
                    text = df_recipes['title'],
                    hoverinfo = 'text',
                    marker=dict(
                            size=8,
                            color = clusters,
                            colorscale = 'Portland',
                            showscale=False, 
                            line = dict(
            width = 2,
            color = 'rgb(255, 255, 255)'
        )
                    ))
        layout = dict(title = 'KMeans Clustering',
                hovermode= 'closest',
                yaxis = dict(zeroline = False),
                xaxis = dict(zeroline = False),
                showlegend= False,
                width=600,
                height=600,
                )

        data = [trace_Kmeans]
        fig1 = dict(data=data, layout= layout)
# fig1.append_trace(contour_list)
        py.iplot(fig1, filename="svm")
        
        

        
        #st.pyplot(fig1)
        
        

if rad=="Recommender":

##Header Section
    with header:
        image =Image.open("./ingredeints.png").resize((680, 150))
        st.image(image)
        st.title("Guten Appetit!!!")
        st.subheader("Suggests recipes based on ingredients")
        st.write("The Recipe Recommender is built on a KMeans Clustering Model")
        st.write("[Complete Code is available in this Github link >](https://github.com/spicedacademy/naive-zatar-student-codes/tree/mahas/Final_Project)")

    with intro:
        st.write(".....")
        left_column,right_column=st.columns(2)
        with left_column:
            st.header("About the Project")
            st.write("##")
            st.write(
                """
                This app suggests recipes based on the ingredients,cooking time and dishtype(Breakfast,Main dish) as an input""" 
                )

    with data:
        st.write("Data is 800 recipes with ingredients,nutritional components,instructions from the Spoonacular API")
    
    

    

    #st.write(df_recipes.head())

    with model:
        st.header('Recipe Recommender')

        user_input=st.text_input('Here you can enter your ingredeints')
    

        sel_col,display_col=st.columns(2)

        Cooking_time=sel_col.slider('How many minutes you want to spend on cooking',value=[5,160])

        n_estimators =sel_col.selectbox('Do you want a breakfast dish or a main dish',options=['breakfast','main dish'])
        #recommender.recommender([user_input],n_estimators)

        if st.button("Give me recommendations!"):
            st.write(recommender.recommender([user_input],n_estimators))
            #st.dataframe(output)




