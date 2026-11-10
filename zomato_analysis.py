import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import nltk
import time

con = sqlite3.connect(r"C:\Users\admin\Downloads\Resources\zomato_rawdata.sqlite")
df= pd.read_sql_query("select * from users", con)
print(df)
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.columns)
missing_percentage = df.isnull().sum()/len(df) * 100
print(missing_percentage)
print(df["rate"])
print(df["rate"].isnull().sum())
df["rate"]= df["rate"].replace(("NEW", "-"),np.nan)
print(df["rate"])
print(df["rate"].isnull().sum())
df["rate"]= df["rate"].apply(lambda x: float(x.split("/")[0])if type(x)== str else x)
print(df["rate"])
print(df["rate"].isnull().sum())
x= pd.crosstab(df["rate"], df["online_order"])
print(x)
print(x.sum(axis=1).astype(float))

normalize_df= x.div(x.sum(axis=1), axis=0)
print(normalize_df)
print(normalize_df *100)


(normalize_df *100).plot(kind="bar", stacked=True)

plt.xlabel("Category")
plt.ylabel("Percentage")
plt.title("category by 100 percentage")
plt.legend()
plt.savefig("visuals/category by 100 precentage.png")
plt.show()

print(df["rest_type"].isnull().sum())
data= df.dropna(subset=["rest_type"])
print(data)
print(data["rest_type"].isnull().sum())
print(data["rest_type"].unique())
print(data["rest_type"].shape)
Quick_bites_df= data[data["rest_type"].str.contains("Quick Bites")]
print(Quick_bites_df)
print(Quick_bites_df.shape)
print(Quick_bites_df.columns)
print(Quick_bites_df["reviews_list"])
print(Quick_bites_df["reviews_list"].index)


from nltk.tokenize import RegexpTokenizer
tokenizer= RegexpTokenizer("[a-zA-Z]+")
print(tokenizer)
print(Quick_bites_df["reviews_list"].index)
tokenizer_reviews= Quick_bites_df["reviews_list"].apply(tokenizer.tokenize)[3]
print(tokenizer_reviews)
sample= data[0:10000]
review_tokens = sample["reviews_list"].apply(tokenizer.tokenize)
print(review_tokens)

from nltk.corpus import stopwords
stop_words= stopwords.words("english")
print(stop_words)
stop_words.extend(["RATED", "n", "nan", "x", "Rated","rated"])
print(stop_words)

rev3= review_tokens[3]
print(rev3)
print([token for token in rev3 if token not in stop_words])
review_tokens_clean= review_tokens.apply(lambda each_review : [token for token in each_review if token not in stop_words])
print(review_tokens_clean.dtype)
print(review_tokens_clean.head(5))
total_reviews_2D = list(review_tokens_clean)
total_reviews_1D= []
for review in total_reviews_2D:
    for word in review:
        total_reviews_1D.append(word)
print(total_reviews_1D)
from collections import Counter
total_reviews_1D_count = Counter(total_reviews_1D).most_common(20)
print(total_reviews_1D_count)
words = [item[0] for item in total_reviews_1D_count]
counts = [item[1] for item in total_reviews_1D_count]
plt.plot(words, counts)
plt.xticks(rotation=90)
plt.title("Top 20 Most Frequently Used Words in Zomato Reviews")
plt.savefig("visuals/total_reviews.png")
plt.show()

from nltk import FreqDist, bigrams, trigrams
bi_grams = bigrams(total_reviews_1D)
fd_bigrams = FreqDist()
for bigram in bi_grams:
    fd_bigrams[bigram] = fd_bigrams[bigram] + 1
print(fd_bigrams.most_common(20))

tri_grams = trigrams(total_reviews_1D)
fd_trigrams = FreqDist()

for trigram in tri_grams:
    fd_trigrams[trigram] = fd_trigrams[trigram] + 1

print(fd_trigrams.most_common(20))

print(df["location"].isnull().sum())
print(df["location"].unique())
print(df["location"].nunique())

df_copy = df.dropna(subset=["location"]).copy()

print(df_copy.shape)
print(df_copy["location"].isnull().sum())

df_copy = df.dropna(subset=["location"]).copy()

print(df_copy.shape)
print(df_copy["location"].isnull().sum())

df_copy["location"] = df_copy["location"] + ", Bangalore, Karnataka, India"

print(df_copy["location"].head())

location = df_copy["location"].unique()

print(location)
print(len(location))

location = pd.DataFrame({"name": location})

print(location.head())
print(location.shape)

from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="zomato_analysis", timeout=10)


lat = []
lon = []


for loc in location["name"]:
    try:
        result = geolocator.geocode(loc)

        if result is None:
            lat.append(np.nan)
            lon.append(np.nan)
        else:
            lat.append(result.latitude)
            lon.append(result.longitude)

    except Exception:
        lat.append(np.nan)
        lon.append(np.nan)

    time.sleep(1)


location["latitude"] = lat
location["longitude"] = lon

print(location)

print(location.isnull().sum())
print(location[location['latitude'].isna()])


import warnings
from warnings import filterwarnings
filterwarnings('ignore')

location['latitude'][45] = 12.9764122
location['longitude'][45] = 77.6017437

location[location['latitude'].isna()]
location['latitude'][79] = 13.0163
location['longitude'][79] = 77.6785

location['latitude'][85] = 13.0068
location['longitude'][85] = 77.5813

df_copy = df_copy.dropna(subset=["cuisines"]).copy()

north_india = df_copy[
    df_copy["cuisines"].str.contains("North Indian", na=False)
]


print(north_india.head(5))
print(location.head(5))
print(north_india.shape)
north_india_rest_count = north_india['location'].value_counts()
print(north_india_rest_count)
north_india_rest_count= north_india_rest_count.reset_index()
print(north_india_rest_count)
north_india_rest_count= north_india_rest_count.rename(columns={"index":"name", "location":"count"})
print(north_india_rest_count)
north_india_rest_count.columns = ["name", "count"]
print(north_india_rest_count.columns)
print(location.columns)
print(location)
print(df["location"].head(10).tolist())
print(location["name"].head(10).tolist())
heatmap_df = north_india_rest_count.merge(location , on='name' , how='inner')
print(heatmap_df)
geo_df = heatmap_df.dropna(subset=["latitude", "longitude"]).copy()
print(geo_df)
plt.figure(figsize=(12, 8))
plt.scatter(
    geo_df["longitude"],
    geo_df["latitude"],
    s=geo_df["count"] * 10,
    alpha=0.6
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("North Indian Restaurant Distribution Across Bangalore")
plt.grid(True)
plt.savefig("visuals/north_indian_restaurant_distribution.png")
plt.show()