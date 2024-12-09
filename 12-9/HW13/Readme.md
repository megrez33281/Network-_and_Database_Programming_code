
## Packages
```
pip3 install torch torchvision torchaudio
```



## YoloV5
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```
* 需在yolov5資料夾中心新增dataset.yaml
    路徑不可有中文
    ```
    path: C:\Users\apple\Downloads
    train: train
    val: val

    # classes
    names:
    0: ruler
    1: utility knife

    ```
* train
    ```
    python train.py --img 640 --batch 10 --epochs 100 --data dataset.yaml --weights yolov5s.pt
    ```

## labelImg
可下載Release的zip檔案
```
https://github.com/HumanSignal/labelImg
```

下載Code(需要使用anconda)
```
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
```

## 我的dataset
'''
https://drive.google.com/file/d/1q0pLRwchThLObxb5AVcEyVRNzpRR1bJ-/view?usp=drive_link
'''




