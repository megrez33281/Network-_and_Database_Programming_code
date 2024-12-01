
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np



def ReadCSV():
    file_path = './HW12/flower.csv'
    df = pd.read_csv(file_path)
    return df.copy()

def preProcessing(flower):
    # X為Feature，Y為Label
    X = flower.drop("species", axis=1)
    X = X.values

    # 將label換成數字
    
    label_names = list(set(flower["species"].values))
    for label in range(0, len(label_names)):
        flower[flower['species'] == label_names[label]] = label

    Y = flower["species"]
    Y = Y.values
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=12345)
    return X_train, X_test, y_train, y_test, label_names

def trainKNN(X_train, y_train, n_neighbors):
    knn_model = KNeighborsRegressor(n_neighbors=n_neighbors) 
    knn_model.fit(X_train, y_train) 
    return knn_model

def predict(KNNmodel, data_point):
    prediction = KNNmodel.predict([data_point])
    return prediction

def classify_prediction(prediction, label_names):
    prediction = round(prediction[0])
    return label_names[prediction]

def testKNNmodel():
    flower = ReadCSV()
    X_train, X_test, y_train, y_test, label_names = preProcessing(flower)
    KNNmodel = trainKNN(X_train, y_train, 3) # 結果有三種 => 分三群
    correct = 0
    for test in range(0, len(X_test)):
        prediction = predict(KNNmodel, X_test[test])
        if classify_prediction(prediction, label_names) == label_names[y_test[test]]:
            correct += 1

    print("accuracy =", correct/len(X_test))

def caculation_knn(X_train, y_train, test_data, k):
    distance = np.linalg.norm(X_train - test_data, axis=1) #計算資料案例與新案例的距離list
    k_nearest_indices = np.argsort(distance)[:k] #選前k個最小的index
    means = np.sum(y_train[k_nearest_indices])/k


    return [means]


if __name__ == '__main__':
    flower = ReadCSV()
    X_train, X_test, y_train, y_test, label_names = preProcessing(flower)
    KNNmodel = trainKNN(X_train, y_train, 3) # 結果有三種 => 分三群
    correct_caculation = 0
    correct_knn = 0
    print("計算KNN預測", "scikit_learn預測", "真實標籤")
    for test in range(0, len(X_test)):
        prediction_caculation = caculation_knn( X_train, y_train, X_test[test], 3)
        prediction_knn = predict(KNNmodel, X_test[test])
        caculation_classify = classify_prediction(prediction_caculation, label_names)
        knn_classify = classify_prediction(prediction_knn, label_names)
        true_classify = label_names[y_test[test]]
        print(caculation_classify, knn_classify, true_classify)
        if caculation_classify == true_classify:
            correct_caculation += 1
        if knn_classify == true_classify:
            correct_knn += 1
        

    print("計算KNN預測 accuracy =", correct_caculation/len(X_test))
    print("scikit_learn預測 accuracy =", correct_knn/len(X_test))

