
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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
    knn_model = KNeighborsClassifier(n_neighbors=n_neighbors)
    class_labels = list(set(y_train))[:-1]
    for label in range(0, len(class_labels)):
        class_labels[label] += 0.5
    
    y_train_class = np.digitize(y_train, bins=class_labels)  # 自定義區間 
    knn_model.fit(X_train, y_train_class) 
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
    KNNmodel = trainKNN(X_train, y_train, 5) # 以最近的5個點vote
    correct = 0
    for test in range(0, len(X_test)):
        prediction = predict(KNNmodel, X_test[test])
        if classify_prediction(prediction, label_names) == label_names[y_test[test]]:
            correct += 1

    print("accuracy =", correct/len(X_test))

def caculation_knn(X_train, y_train, test_data, k):
    distance = np.linalg.norm(X_train - test_data, axis=1) #計算資料案例與新案例的距離list
    k_nearest_indices = np.argsort(distance)[:k] #選前k個最小的index

    # label = y_train[k_nearest_indices]
    # 進行投票
    classes = list(set(y_train))
    a_list = []
    for i in classes:
        a_list.append(int(0))

    for label in y_train[k_nearest_indices]:
        a_list[label] += 1
    
    max_index = 0
    max_value = a_list[0]
    for a in range(0, len(a_list)):
        if a_list[a] > max_value:
            max_value = a_list[a]
            max_index = a

    #print(a_list)
    #print(max_index)
    #means = np.sum(y_train[k_nearest_indices])/k


    return [max_index]


if __name__ == '__main__':
    flower = ReadCSV()
    X_train, X_test, y_train, y_test, label_names = preProcessing(flower)
    KNNmodel = trainKNN(X_train, y_train, 3) # 結果有三種 => 分三群
    correct_caculation = 0
    correct_knn = 0
    print("計算KNN預測", "scikit_learn預測", "真實標籤")
    for test in range(0, len(X_test)):
        prediction_caculation = caculation_knn( X_train, y_train, X_test[test], 5)
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


    # 新的測資
    new_data = [4.6,3.4,1.4,0.2]
    prediction_caculation = caculation_knn( X_train, y_train, new_data, 5)
    prediction_knn = predict(KNNmodel, new_data)
    print("計算KNN預測 accuracy", classify_prediction(prediction_caculation, label_names))
    print("scikit_learn預測", classify_prediction(prediction_knn, label_names))

