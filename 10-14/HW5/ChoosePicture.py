import tkinter as tk
from tkinter import filedialog
from PIL import Image
import io

def ChoosePicture():
    root = tk.Tk()
    root.withdraw()

    #打開文件選擇對話框並設置文件類型為圖片
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )

    #檢查用戶是否選擇了文件
    if file_path:
        print(f"Selected file: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return 0

def ReadPictureToBinary(FilePath):
    #輸入圖片路徑，回傳圖片的binary
    im = Image.open(FilePath)
    image_bytes = io.BytesIO()
    FileName = FilePath.split("/")[-1]
    FileFormat = FileName.split(".")[-1]
    FileFormat = FileFormat.upper().replace("JPG", "JPEG")
    print("FileFormat = ", FileFormat)
    im.save(image_bytes, format=FileFormat)
    return image_bytes.getvalue()

def BinaryToPicture(image_bytes):
    pil_img = Image.open(io.BytesIO(image_bytes))
    #依設定的bitmap大小而定
    pil_img = pil_img.resize((100,100))
    image_data = io.BytesIO()
    pil_img.save(image_data, format="PNG")
    image_data.seek(0)
    return image_data