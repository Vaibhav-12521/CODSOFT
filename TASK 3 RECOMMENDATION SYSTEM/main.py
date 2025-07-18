
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("dataset.csv")
movies['tags'] = movies['genre'] + movies['overview']
new_df = movies[['id', 'title', 'tags']]
cv = CountVectorizer(max_features=10000, stop_words='english')
vec = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()
sim = cosine_similarity(vec)

dist = sorted(list(enumerate(sim[0])), reverse = True, key=lambda vec:vec[1])

for i in dist[0:5]:
    print(new_df.iloc[i[0]].title)
    

def recommend(movies):
    index = new_df[new_df['title'] == movies].index[0]
    distance = sorted(list(enumerate(sim[index])), reverse = True, key=lambda vec:vec[1])
    print("I'll recommanded You: \n\n")
    for i in distance[0:5]:
        print(new_df.iloc[i[0]].title)
        
if __name__ == '__main__':
    while True:
        user = input("Enter Your fevourite Movie Name:").title()
        recommend(user)












