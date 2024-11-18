import pandas as pd
from pathlib import Path
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

def read_csv_file(file_path: str, encoding: str = 'utf-8', **kwargs) -> pd.DataFrame:
    try:
        # 檢查檔案是否存在
        if not Path(file_path).is_file():
            raise FileNotFoundError(f"找不到檔案: {file_path}")
            
        # 讀取CSV檔案
        df = pd.read_csv(file_path, encoding=encoding, **kwargs)
        
        # 檢查是否有資料
        if df.empty:
            raise pd.errors.EmptyDataError("CSV檔案沒有資料")
            
        return df
        
    except UnicodeDecodeError:
        print(f"編碼錯誤，請嘗試其他編碼格式。目前使用的編碼為: {encoding}")
        raise
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {str(e)}")
        raise

def Transform_to_Discrete(data:pd.DataFrame)->pd.DataFrame:
    data = data.join(pd.get_dummies(data['Outlook']))
    data = data.drop(['Outlook'], axis=1)
    data = data.join(pd.get_dummies(data['Temperature']))
    data = data.drop(['Temperature'], axis=1)
    data['Humidity'] = data['Humidity'].map({'High':True, 'Normal':False})
    data['Wind'] = data['Wind'].map({'Strong':True, 'Weak':False})
    data['PlayTennis'] = data['PlayTennis'].map({'Yes':True, 'No':False})
    #重排欄位
    data = data.reindex(columns=['Humidity', 'Wind', 'Overcast', 'Rain', 'Sunny', 'Cool', 'Hot', 'Mild', 'PlayTennis'])
    return data

def entropy(data:pd.DataFrame, attribute:str):
    total = len(data)
    values = set(data[attribute])
    entropy = 0
    for value in values:
        pi = (data[attribute] == value).sum()/total
        entropy += pi*np.log2(pi)*-1
    return entropy


def conditional_entropy(data:pd.DataFrame, attribute:str):
    #計算第一層以attribute進行分割後，'PlayTennis'的entropy
    data_len = len(data)
    values = set(data[attribute])
    conditional_entropy_value = 0
    for value in values:
        #將data依attribute分類
        attribute_classify = (data[data[attribute] == value])
        classify_entropy = entropy(attribute_classify, 'PlayTennis')
        #分類後，'PlayTennis'的entropy以各邊'PlayTennis'的entropy值*各邊資料佔總資料比例後，相加計算
        conditional_entropy_value += classify_entropy*(len(attribute_classify)/data_len)
    return round(conditional_entropy_value, 3)



def Gain(data:pd.DataFrame, attribute:str):
    data_len = len(data)
    S_entropy = entropy(data, 'PlayTennis')
    values = set(data[attribute])
    Gain = S_entropy
    for value in values:
        #將data依attribute分類
        attribute_classify = (data[data[attribute] == value])
        classify_entropy = entropy(attribute_classify, 'PlayTennis')
        #計算Gain時則改為減去分類後'PlayTennis'的entropy以各邊'PlayTennis'的entropy值*各邊資料佔總資料比例
        Gain -= classify_entropy*(len(attribute_classify)/data_len)

    return round(Gain, 3)


if __name__ == '__main__':
    #讀取資料
    data = read_csv_file("./data.csv")
    data = Transform_to_Discrete(data)
    X = data.drop('PlayTennis', axis=1)
    Y = data['PlayTennis'].astype(str)  #輸入兩個instance的類別，此處為要/不要玩羽毛球
    clf = tree.DecisionTreeClassifier(criterion='entropy') # 創一個decision tree classifier 
    clf = clf.fit(X, Y) # 將training data 以classifier 做學習
    # 設定圖片大小和解析度
    plt.figure(figsize=(15,10))

    # 繪製決策樹，加入更多參數使圖片更容易理解
    tree.plot_tree(clf,
                feature_names=X.columns,     # 使用實際的特徵名稱
                class_names=sorted(set(Y)),  # 使用實際的類別名稱
                filled=True,                 # 填充顏色
                rounded=True,                # 使用圓角
                fontsize=10)                 # 設定字型大小

    # 顯示圖片
    plt.show()

    #計算entropy進行驗證：
    print("PlayTennis_entropy = ", entropy(data, 'PlayTennis'))
    

    min_entropy = None
    max_information_gain = None
    choose_col = None
    for col in data.drop('PlayTennis', axis=1):
        #每次決策應該選擇分類後，PlayTennis的Entropy值最小的（各邊PlayTennis的Entropy*佔比的和）或information gain最大的
        choose_col_entropy = conditional_entropy(data, col)
        choose_col_information_gain = Gain(data, col)
        print(col, "entropy = ", choose_col_entropy, "information gain = ", choose_col_information_gain)
        #在此以entropy進行選擇
        if min_entropy == None or choose_col_entropy < min_entropy:
            min_entropy = choose_col_entropy
            max_information_gain = choose_col_information_gain
            choose_col = col
    #print(data)
    print()
    print("choose", "'" + choose_col + "', ", "entropy = ", min_entropy, "information gain = ", max_information_gain)