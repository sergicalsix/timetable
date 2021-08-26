import pandas as pd
import glob
import jaconv 

def to_hankaku(df):
    """
    in: pd.DataFrame
    out: pd.DataFrame
    """
    for col in df:
        value_list = df[col].values.tolist()
        new_list = []
        for li in value_list:
            try:
                li = jaconv.z2h(li,digit=True, ascii=True,kana=True)
            except:
                pass
            new_list.append(int(li))
        df[col] = new_list
    return df



csv_file_list = glob.glob('data/*.csv')
print(f"Total file num is {len(csv_file_list)}")

df = pd.read_csv(csv_file_list[0])
df = to_hankaku(df)


for csv_file in csv_file_list[1:]:
    df_ =  pd.read_csv(csv_file)
    df_ = to_hankaku(df_)
    df += df_

df = df.drop('0',axis = 1)
print(df)
print("空いている時間:")
#  全体で空いている時間を出力
for col in df:
    ans_time:list = []
    for index_ in range(5):
        if df[col][index_] == 0:
            ans_time.append(index_ + 1)
    if len(ans_time) != 0 :
        print(f"{col}: {ans_time}")
                
            
