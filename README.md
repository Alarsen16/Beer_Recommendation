# Beer_Recommendation

Table of Contents:
1. Introduction
2. Business Problem
3. Data
4. Modeling
5. Next Steps
6. Conclusion


## Introduction

The goal of my Beer Recommender system is to be able to predict what beers you'd enjoy, based on a user's input by choosing their favorite beer. At a very high level, we'll be using a recommendation system with NLP in order to come up with sound beer predictions.

## Business Problem

There is absolutely nothing worse than trying a new beer you end up HATING. You probably ordered that beer based off of some friend’s recommendation, an advertisement you saw on the subway or maybe it was the same style as a beer you’ve enjoyed previously. 

You sit there staring at a full glass hoping it would empty itself so you could go back to drinking something you know you’d enjoy. That’s where my model comes into play. Our predictions will allow you to stop making these miserable $8 mistakes and allow you to continue to try something new, with a strong guarantee you’ll enjoy it as well. 

## Data

To begin, I used various data from the BeerAdvocate website that included beer reviews provided by beer drinkers like us,  beer descriptions provided by the brewers and the styles of the beers. Examples of how this data looked like can be seen below.

Style: India Pale Ale, American Ale, German Witbier.

Reviews: “…hints of toasted bran, with a touch of malt sweetness balanced by a slightly heavy handed use of delicate noble hops to finish crisp and keep you coming…”

Descriptions: “...a combination of barley malts and rice. Its superior drinkability and refreshing flavor makes it the world’s favorite light beer.”

I then grabbed ratings for the same beers which were rated on a 5 category scale by website goers which consists of the mouth feel, how strong the taste was, how pungent the smell is, how cloudy or clear the beer was,  as well as an overall rating. Using these two sets of information, I began our modeling process. Ratings were on a scale of 1-5 that went up by 0.25 intervals.

Categories:
1. Taste
2. Mouth Feel
3. Appearance
4. Aroma
5. Overall rating

## Modeling

Using NLP or natural language processing, I used a term frequency model to determine which words or phrases (max of 3) were most common across the text reviews and descriptions. Some examples of the most frequent phrases were india pale ale, which was the most common style, bitter, hoppy, refreshing, crisp or certain hops such as Mosaic, Citra or Columbus.

I then used cosine similarity between our favourite beer description and our entire data set to find the top reviews and descriptions that seemed to match and created a new feature that gave us a rating of how similar our favorite beer was to our entire data set. As an example, a description of “fruity, bold and intense” would score pretty low when compared to “light, crisp and refreshing.”

We then ran a content based recommendation system off of the five categorical ratings and the new similarity score to come up with a list of predictions that both had similar reviews and descriptions but alike drinking experiences as well. 

As an example, we’ll be using Bud Light as our favourite beer to find similar beers.  Thinking about a bud light which I’m assuming most people in the room today have tried, we could almost all agree the color of the beer would be light with a thin layer of foam after pouring into a glass and the feel in your mouth would be crisp and effervescent and we’d hope that beer reviewers would agree. 

From our model and unsurprisingly, we see that Busch and Michelob Ultra, two extremely common light beers, have been identified, as well as some lesser known beers which I’d certainly love to try. 

The top recommended beer is 1811 Pre-Prohibition Lager, which is an American lager styled beer. At first, I was a bit surprised and a little bit defeated because it wasn’t what I was expecting however I dug into the data a bit more only to realize that reviews for both bud light and this been had extremely similar color and aroma ratings, as well as reviews consisted of tasting of corn and strong barley flavors, and that this recommendation was valid, and more accurate than I originally thought!

## Next Steps

As for next steps and items that are achievable within the next half a year, I’d love to try and enhance this model with more real-time data as well as more reviews from other websites such as Untappd as an example. I’d also love to be able to take a user’s preference in terms of certain tastes, hops and keywords to predict beers they should try. My last two steps would be to try and work with existing websites, such as BeerAdvocate, where the majority of this data stems from, to pitch my model as something they might be able to utilize on their website. Lastly, I’d love to see if BeerMenus would be willing to collaborate so that I could add an output of where a user might be able to find the beer, based on their zipcode. 

## Conclusion

Please use this model and let me know if you have any questions or ideas on how to improve it. Cheers on trying a new beer!

## Repository Structure
```
├── [workbook / data cleaning]
├── [data]
├── Final_BeerRecommender.ipynb
├── Procfile
├── app.py
├── df_streamlit.csv
├── .gitignore
├── README.md
├── setup.sh
└── requirements.txt
```
