input_score = input('得点を入力　：') #　成績値入力
score = float(input_score)            #  キャスト
limit = 60                            # ボーダーライン
upper = 90                            # A判定
if score >= upper :
     print('合格　A判定')
elif score >= limit :
     print('合格')
else :
      under_score = limit - score
      print_text = f'不合格　不足点　＝　{under_score}'
      print(print_text)