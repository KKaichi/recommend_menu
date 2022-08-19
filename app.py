import csv
import twitter
import rakuten
import tweet_decomposition as td
import random

def main():
  item_categoryId = {}
  with open('category_id.csv', mode='r') as categoryId_file:
    reader = csv.reader(categoryId_file)
    categoryId_list = [rows[1] for rows in reader]
  categoryId = random.choice(categoryId_list)
  recommend_text = rakuten.get_menu(categoryId)
  twitter.tweet(recommend_text)

  return 0
main()  