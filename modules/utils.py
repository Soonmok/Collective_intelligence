import pandas as pd


def total_common_movies(dataset, user_ids):
    common_movies = pd.Series(list(set(dataset['movieId'])))
    for user_id in user_ids:
        user_movies = dataset[dataset['userId'] == user_id]['movieId']
        common_movies = pd.Series(list(set(common_movies) & set(user_movies)))

    return common_movies
