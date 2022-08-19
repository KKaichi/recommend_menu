import tweepy

def tweet(tweet_text):
  # 認証に必要なキーとトークン
  API_KEY = '2bVkQ0wKtnznogX91TCecNZtN'
  API_SECRET = 'i1iSIgbNoC5SPEyogrff8XrC2oYNpoPjwJr8cK1VQnCqIAgdY4'
  BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMiMgAEAAAAAQhTl1qUs5gJbzgaRI4N85Gqghh4%3D5kIRx33EoUkyVM21EDXxaLA2HwU1q56hDynEB4OEhKw4rq2ze3'
  ACCESS_TOKEN = '1539613748607844352-AaFIQgTNQSC8aZ7nyTguPDxvym9J38'
  ACCESS_TOKEN_SECRET = '9CKKwAXgvtcf87zh1OzJT9f9wiUC9HHeYKezDV7A7IH3e'

   # APIの認証
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

  #キーワードからツイートを取得
  api = tweepy.API(auth)
  api.update_status(tweet_text)

  return 0

