# ●入力された複数の数値からから合計や平均を求める。
# ユーザーにカンマ区切りで数値を入力させる
# 入力された数値の合計と平均を出力する

score = input('数値をカンマ区切りで入力してください→')

# print(sum(score))だとscoreが文字列型なので合計が求められない。
# score  = int(input())だとカンマが入るのでエラー

# ↓splitメソッドを使い、リスト型に変更。
score_list = score.split(',')

# ↓map関数を使いmap型に変更後、list関数でリストにする。
score_list = list(map(int,score_list))

# ↓合計
print(f'合計は{sum(score_list)}')
# ↓平均
print(f'平均は{sum(score_list)//len(score_list)}')