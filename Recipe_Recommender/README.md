Overview:

This Project is a Recipe Recommender which takes a list of ingredeints as user input and suggests recipes. In this project I have taken data from an API called Spoonacular api . Data from the API was in JSON format, I have extracted the recipe information like recipe ID,recipe name, ingredients, instructions, nutritional values by flatenning the JSON file. I have used Pandas and Scikit Learn to extract and clean the data , later used Seabor and Matplotlib to Visualize the data. I took the ingredients data ,parsed them and applied TFIDF . I reduced the dimensionality of the TFIDF matrix by applying PDA and later used Elbow Method to determine the number of Clusers. The Elbow Method was not clear so I guessed the number of Clusters randomly and applied KMeans Clustering model to get the Clusters. I plotted it with Plotly. Now I determined the the most frequent words occuring in each Cluster and tried to label the Clusters. Now I defined a Recommendation function which takes ingredeints lists, type of dish(Breakfast,Lunch) and time a user wants to spend cooking it as input and Suggests Top 3 Recipes. Later I used Streamlit to present my Recipe Recommender.


Contents:

1.Scraper notebooks : To make API calls and get the data , I did basic Extraction and Cleaning of data here. Since I had       limited points to make API calls I created 9 scrapers to get random calls with API keys.
2. all_recipes: Merging all recipes from 9 scrapers and further Feature Engineering
3. ingredients_parser: To parse all ingredients and applied stopwords for some recurring words
4. Model: Took the parserd ingredients and applied tfidf on them and later KMeans Clustering. In this nitebook I also defined the Recommendation Function.Finally created a word cloud for app
5. streamlit app: Created app via Streamlit 
