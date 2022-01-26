import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

beer_csv = pd.read_csv('df_streamlit.csv')

st.sidebar.write("How this tool works:")
st.sidebar.write(" ")
st.sidebar.write('Uses NLP (natural language processing) and a content-based'
            'recommendation system to predict a similar beer')

st.sidebar.write(" ")
st.sidebar.write("Data is taken from BeerAdvocate where we used beer ratings and reviews submitted by fellow beer"
    ' drinkers, as well as beer descriptions, mainly submitted by the breweries themselves.')

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("by Adam Larsen, Flatiron School DS Program, 2022 ")

    
beer_df = pd.DataFrame(beer_csv)

beer_choice = list(beer_df['name'])

st.title('Beer Recommender')
beer = st.selectbox('Pick your favorite beer:', beer_choice)


tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df = 1, max_features=200)

tfid_vec = tf.fit_transform(beer_df['combined_text'])
chosen_beer_df = beer_df[beer_df['name'] == beer]
closeness = cosine_similarity(tfid_vec, tfid_vec[chosen_beer_df.index])

beer_df['cosine'] = closeness
beer_df = (beer_df.sort_values(by=['cosine'], ascending=False)[:51])
chosen_beer_df = beer_df[beer_df['name'] == beer]

beerless_df = beer_df.drop(chosen_beer_df.index)


chosen_beer_df_array = np.array((chosen_beer_df[['look', 'smell', 'taste', 'feel', 'overall', 'score', 'cosine']]))
beerless_df_array = np.array((beerless_df[['look', 'smell', 'taste', 'feel', 'overall', 'score', 'cosine']]))


numerators = np.array([chosen_beer_df_array[0].dot(beers) for beers in beerless_df_array[0:]])
denominators = np.array([np.sqrt(sum(chosen_beer_df_array[0]**2)) *\
                         np.sqrt(sum(beers**2)) for beers in beerless_df_array[0:]])


results = pd.DataFrame((numerators / denominators), columns=['recommendation'])
beerless_rec = beerless_df.join(results)


final_df = beerless_rec.join(beerless_df, lsuffix=['_2'])
final_df = final_df.sort_values(by=['recommendation'], ascending=False)


st.write('You may also like the following:')
beers_rec = list((final_df['name'][:5]))
beer_style = list((final_df['style'][:5]))

st.write("1. {}, style: {}.".format(beers_rec[0], beer_style[0]))
st.write("2. {}, style: {}.".format(beers_rec[1], beer_style[1]))
st.write("3. {}, style: {}.".format(beers_rec[2], beer_style[2]))
st.write("4. {}, style: {}.".format(beers_rec[3], beer_style[3]))
st.write("5. {}, style: {}.".format(beers_rec[4], beer_style[4]))


st.write(" ")
st.write("Thanks for using my tool, hope you've enjoyed it!")
st.title("Cheers!")
