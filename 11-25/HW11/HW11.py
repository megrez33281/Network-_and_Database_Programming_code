import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import random
import numpy as np


def MakeData():
    features, true_labels = make_blobs(
        n_samples=400,
        centers=4,
        cluster_std=2.75,
        random_state=42
    )

    return features, true_labels

def Normalization(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features

def GetKmeans(features):
    kmeans = KMeans(
        init='random',
        n_clusters=4,
        n_init=10,
        max_iter=300,
        random_state=42
    )
    kmeans.fit(features)
    return kmeans

def draw_pic(x_datas, y_datas, labels1, title1, labels2, title2):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].scatter(x_datas, y_datas, c=labels1, s=100)
    axes[0].set_title(title1)

    axes[1].scatter(x_datas, y_datas, c=labels2, s=100)
    axes[1].set_title(title2)

    plt.tight_layout()
    plt.show()

def sameCenter(MatrixA, MatrixB):
    if len(MatrixA) != len(MatrixB):
        return False

    for element in range(0, len(MatrixA)):
        if list(MatrixA[element]) != list(MatrixB[element]):
            return False
    return True

def Kmeans(scaled_features, clusters, Max_iteration):
    #隨機選取初始中心
    centers = random.sample(list(scaled_features), clusters)
    NewCenters = []
    labels = []
    iteration = 0
    while True:
        #分配label
        feature_clusters = []
        NewCenters = []
        labels = []
        for cluster in range(clusters):
            feature_clusters.append([])

        for scaled_feature in scaled_features:
            min_distance = None
            label = None
            #計算每個點距離最小的中心點
            for center in range(0, len(centers)):
                d = np.array([centers[center] - scaled_feature])
                distance = np.sqrt(np.square(d).sum(axis=1))
                if min_distance == None or distance < min_distance:
                    min_distance = distance
                    label = center
            labels.append(label)
            feature_clusters[label].append(scaled_feature)

        for feature_cluster in feature_clusters:
            Center = np.mean(np.array(feature_cluster), axis=0)
            NewCenters.append(Center)
        iteration += 1
        if sameCenter(NewCenters, centers) or iteration > Max_iteration:
            break
        centers = NewCenters
   
    return labels, NewCenters

if __name__ == '__main__':
    
    features, true_labels = MakeData()
    scaled_features = Normalization(features)
    kmeans = GetKmeans(scaled_features)
    

    labels, centers = Kmeans(scaled_features, 4, 300)
    print("Centers Get From sklearn.cluster")
    for element in kmeans.cluster_centers_:
        print(element)
    print()
    print("Centers Get From calculation")
    for element in centers:
        print(element)

    #畫出利用sklearn.cluster的分群
    draw_pic(scaled_features[:,0], scaled_features[:,1], kmeans.labels_, 'Kmeans from sklearn.cluster', labels, "Kmeans from calculation")

    #畫出利用