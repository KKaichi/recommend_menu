from pprint import pprint
import requests
import pandas as pd

def get_category():
  base_url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426' #ジャンル検索APIのベースとなるURL
  item_parameters = {
            'applicationId': '1009872609305787297',
            'format': 'json',
            'formatVersion': 2,
  }
 
  #全カテゴリレベルの前データ抽出
  r = requests.get(base_url, params=item_parameters)
  item_data = r.json()
 
  #データ格納用にデータフレームを準備
  df_category = pd.DataFrame(columns=['categoryName','categoryId'])
 
  #大カテゴリ
  for category in item_data['result']['large']:
    df_category = df_category.append(
        {'categoryName':category['categoryName'],
        'categoryId':category['categoryId']},
        ignore_index=True)
 
  #中カテゴリ
  #小カテゴリの時のカテゴリID作成用に中カテゴリの親(大)カテゴリの辞書を用意
  parent_dict = {} 
  for category in item_data['result']['medium']:
      df_category = df_category.append(
        {'categoryName':category['categoryName'],
        'categoryId':str(category['parentCategoryId'])+"-"+str(category['categoryId'])},
        ignore_index=True)
      parent_dict[str(category['categoryId'])] = category['parentCategoryId']
 
  #小カテゴリ
  for category in item_data['result']['small']:
      df_category = df_category.append(
        {'categoryName':category['categoryName'],
        'categoryId':parent_dict[category['parentCategoryId']]+"-"+str(category['parentCategoryId'])+"-"+str(category['categoryId'])},
        ignore_index=True)
  df_category.to_csv('category_id.csv', index=False,  encoding='utf_8_sig')

  return 0

get_category()