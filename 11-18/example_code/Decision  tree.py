from sklearn import tree

X = [[0, 0], [1, 1]] # 輸入兩個instance, 個別有兩個attribute
Y = [0, 1] #輸入兩個instance的類別
clf = tree.DecisionTreeClassifier() # 創一個decision tree classifier 
clf = clf.fit(X, Y) # 將training data 以classifier 做學習
tree.plot_tree(clf) #使用jupyter notebook
print (clf.predict([[2., 2.], [0., 0.], [-2., -2.]])) # 以訓練好的decision tree 模型分類三個instance
