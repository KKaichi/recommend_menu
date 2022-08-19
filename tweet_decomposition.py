import MeCab

def decomposition(text):
  mecab = MeCab.Tagger()
  meishi_list = [] #meishi = 名詞
  for word in mecab.parse(text).splitlines():
    word_detail=word.split()
    if(len(word_detail) == 2): #EOFを除く処理
      word_information = word_detail[1].split(',')
      hinshi = word_information[0] #hinshi = 品詞
      if(hinshi == '名詞'):
        meishi_list.append(word_detail[0]) #word_detail[0]は単語

  return meishi_list

