import csv


filename = "twitter_result_ネップリ.csv"
filename = "twitter_result_1126_1205.csv"
seven_and_famima_and_roson_count = 0
famima_and_roson_count = 0
famima_count = 0
seven_count = 0
roson_count = 0
other_count = 0
all_count = 0

with open (filename, encoding='utf-8') as f:
    csvreader=csv.reader(f)

    for i, row in enumerate(csvreader):
        

        if ("セブン" in row[10]) & ("ファミマ" in row[10])& ("ローソン" in row[10]) :
            seven_and_famima_and_roson_count += 1
        elif ("ファミマ" in row[10]) & ("ローソン" in row[10]):
            famima_and_roson_count += 1
        elif ("ファミマ" in row[10]) & ("セブン" not in row[10])& ("ローソン" not in row[10]):
            famima_count += 1
        elif ("セブン" in row[10]) & ("ファミマ" not in row[10])& ("ローソン" not in row[10]):
            seven_count += 1
        elif ("ローソン" in row[10]) & ("ファミマ" not in row[10]) & ("セブン" not in row[10]):
            roson_count += 1
        else:
            other_count += 1
    all_count = i
    
print("ツイート分析期間 11/26~12/05")
print("'ネップリ'と'番号'の文字列を含むtweet数 : " + str(i))
print("'セブン'と'ファミマ'と'ローソン'の文字列を含むtweet数 : " + str(seven_and_famima_and_roson_count))
print("'ローソン'と'ファミマ'の文字列を含むtweet数 : " + str(famima_and_roson_count))
print("'ファミマ'の文字列を含み、ローソンとセブンの文字列を含まないtweet数 : " + str(famima_count))
print("'セブン'の文字列を含み、ローソンとファミマの文字列を含まないtweet数 : " + str(seven_count))
print("'ローソン'の文字列を含み、ファミマとセブンの文字列を含まないtweet数 : " + str(roson_count))
print("その他(おそらくツイートの画像にファミマかセブンでの指定を記載) : " + str(other_count))



