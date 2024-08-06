import numpy as np

# Sample data
data = {
    'PostSpon': ['user1', 'user2', 'user3', 'user4'],
    'PosterID': ['user1', 'userX', 'user3', 'userY']
}

df_ad = pd.DataFrame(data)

# Create new column based on condition using np.where
df_ad['NewColumn'] = np.where(df_ad['PostSpon'] == df_ad['PosterID'], '@' + df_ad['PostSpon'], None)

print(df_ad)
