def bmi(tall,weight):           # BMIの関数　入力は身長と体重
    tall = float(tall)          # 型変換
    weight = float(weight)      # 型変換
    bmi = weight / tall / tall  # 計算式
    bmi = round(bmi,2)          # 小数点2桁で丸める
    print(bmi)                  # 25以上は肥満
    return

input_tall = input('あなたの身長をメートルで入力　：')  # 身長
input_weight = input('あなたの体重を㎏で入力　：')      # 体重
bmi(input_tall,input_weight)  # 関数呼び出し