from pprint import pprint
import requests
import pandas as pd
import csv
import random

def get_menu(categoryId):
  #楽天レシピランキングAPI
  url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?'

  #urlのパラメータ
  param = {
    'applicationId': '1009872609305787297', #アプリID
    'affiliateId' : '2a9888c4.bec2f7b5.2a9888c5.a4048f48',
    'format': 'json',
    'formatVersion': 2,
    'categoryId' : categoryId
  }
  
  #APIを実行して結果を得る
  response = requests.get(url,params = param)
  item_data = response.json()

  #各レシピ情報の格納用に、データフレーム用意
  df_rank = pd.DataFrame(columns=[
    'rank', #順位
    'recipeId', #レシピID
    'recipeTitle', #レシピタイトル
    'recipeDescription', #レシピ説明文
    'recipeUrl', #レシピURL
    'foodImageUrl', #料理画像URL
    'recipeCost', #予算
    'recipeIndication', #料理時間
    'recipeMaterial',  #レシピ材料
    'recipePublishday' #レシピ発行日
  ])
  for recipe in item_data['result']:
        df_rank = df_rank.append(
            {'rank':recipe['rank'],
             'recipeId':recipe['recipeId'],
             'recipeTitle':recipe['recipeTitle'],
             'recipeDescription':recipe['recipeDescription'],
             'recipeUrl':recipe['recipeUrl'],
             'foodImageUrl':recipe['foodImageUrl'],
             'recipeCost':recipe['recipeCost'],
             'recipeIndication':recipe['recipeIndication'],
             'recipeMaterial':recipe['recipeMaterial'],
             'recipePublishday':recipe['recipePublishday'],},
            ignore_index=True)
  random_number = random.randrange(3)
  recommend_menu = df_rank.loc[random_number]
  menu = recommend_menu["recipeTitle"]
  recipeMaterial = ",".join(recommend_menu["recipeMaterial"][:5])
  url = recommend_menu["recipeUrl"]
  recommend_text = "今日の献立に「"+menu+"」はいかがですか?\n\n主な材料は"+recipeMaterial+"などです！\n"+url
  return recommend_text
