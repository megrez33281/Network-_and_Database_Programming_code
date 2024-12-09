import cv2
import numpy as np
import torch
import os
import pandas
import warnings

# 忽略所有的 FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)


### 此處模型中使用的尺全長約17.2公分 ###

def loadModel():
    # 載入模型
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./model/best.pt', force_reload=True)
    return model


def predictPicture(model, path, saveName="result.png"):
    # 預測圖片

    # 讀取圖片
    img = cv2.imread(path) # 9.jpg表現最佳，1、4、5、6、7.jpg 次之
    # 使用模型進行預測
    results = model(img)
    # 在圖片上畫出預測結果
    rendered_image = results.render()
    # 儲存結果
    cv2.imwrite(saveName, np.squeeze(rendered_image)) 
    return results.pandas().xyxy[0].head()


def CaculateLength(predict_result:pandas.DataFrame):
    ruler_info = predict_result[predict_result['name'] == "ruler"]
    utility_knife_info = predict_result[predict_result['name'] == "utility knife"]
    
    # 目標為計算物品相對於尺的位置，故只需要x方向的資訊

    # 尺在圖片上的長度
    Ruler_long = ruler_info['xmax'] - ruler_info['xmin']
    Ruler_long = Ruler_long.values[0]

    # 圖片中尺的左側與物件左側的距離
    Utility_knife_start = utility_knife_info['xmin'].values - ruler_info['xmin'].values # 物件的左側與尺的左側之距離(表示物件在尺上的位置)
    Utility_knife_start = Utility_knife_start[0]

    # 尺的全長約17.2公分，計算物件在尺上的真實位置
    ratio = 17.2/Ruler_long
    # 物件在尺上的真實位置
    Utility_Length = round(Utility_knife_start*ratio, 3)
    return Utility_Length



if __name__ == '__main__':
    model = loadModel()
    directory_path = './test/'
    # 讀取directory_path中所有jpg、png的圖檔
    pic_files = [f for f in os.listdir(directory_path) if f.endswith('.jpg') or f.endswith('.png')]
    for pic_file in pic_files:
        print("讀取圖片：", pic_file)
        path = directory_path + pic_file
        file_format = pic_file.split(".")[-1]
        file_name = pic_file.replace(file_format, "")
        predict_result = predictPicture(model, path, './result/'+ 'result-' + file_name + ".png")
        length = CaculateLength(predict_result)
        print("物品位於尺上的", length, "公分處\n\n")

    









