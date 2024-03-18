# ●入力された複数の英単語からリストを作る
# その後、昇順に並べる

user_tango = input('英単語をカンマ区切りで入力してください→')
tango_list = user_tango.split(',')
tango_list.sort()

print(tango_list)
