import pandas as pd

from modules.similarity import uclidian_sim, pearson_sim, jaccard_sim

if __name__=="__main__":
    dataset = pd.read_csv("../datasets/ml-latest-small/ratings.csv")
    user1 = 1
    user2 = 100

    user1_ratings = dataset[dataset['userId'] == user1]
    user2_ratings = dataset[dataset['userId'] == user2]

    user1_movies = user1_ratings['movieId']
    user2_movies = user2_ratings['movieId']

    common_movies = pd.Series(list(set(user1_movies) & set(user2_movies)))
    user1_common_ratings = user1_ratings[user1_ratings['movieId'].isin(common_movies)]['rating']
    user2_common_ratings = user2_ratings[user2_ratings['movieId'].isin(common_movies)]['rating']

    ucl_sim = uclidian_sim(user1_common_ratings, user2_common_ratings)
    pear_sim = pearson_sim(user1_common_ratings, user2_common_ratings)

    user1_binary_ratings = user1_ratings.copy()
    user1_binary_ratings['rating'] = user1_ratings['rating'].apply(lambda x: 1 if x > 2.5 else 0)
    user2_binary_ratings = user2_ratings.copy()
    user2_binary_ratings['rating'] = user2_ratings['rating'].apply(lambda x: 1 if x > 2.5 else 0)

    user1_liked_movies = user1_binary_ratings[user1_binary_ratings['rating'] == 1]['movieId']
    user2_liked_movies = user2_binary_ratings[user2_binary_ratings['rating'] == 1]['movieId']

    jac_sim = jaccard_sim(set(user1_liked_movies), set(user2_liked_movies))





