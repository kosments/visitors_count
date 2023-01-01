000

import pandas as pd
from pandas import read_csv
import numpy as np
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import codecs

pd.set_option('display.max_rows', 900)
pd.set_option('display.max_columns', 100)

# 1.CSVファイルを読み込む
# file = "habit-gym-24h__access_2022-11-14 21_10_21.csv"
file = "visitors_list.csv"
# csv_imput = read_csv(file)
# print(csv_imput)
with codecs.open(file, "r", "UTF-8", "ignore") as file:
    df = pd.read_table(file, delimiter=",")
    print(df)

# 重複行を削除
df_dup = df.drop_duplicates(subset='メンバーID')
print(df_dup)


# 2.入館者数をカウントする
# 出力用のdf
df_out =  pd.DataFrame(columns=['日付', 'メンズ会員', 'レディース会員', '合計']) 
print(df_out)

# メンズの合計

# レディースの合計




# 3.最終結果用xlを定義
wb_output = Workbook()
ws_output = wb_output["Sheet"]
wb_output.save("入館者ログ.xlsx")
