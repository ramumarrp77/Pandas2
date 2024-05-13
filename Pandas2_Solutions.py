#Problem 1 : Article Views I 

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'id': views[views.author_id == views.viewer_id]['author_id'].unique()}).sort_values('id')
	
#Problem 2 :Invalid Tweets 	
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'tweet_id':tweets[tweets.content.str.len() > 15]['tweet_id']})