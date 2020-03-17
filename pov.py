import cv2
import os
import math
from PIL import Image
 
#配列設定
#Frame = 5 #抽出フレーム数指定
NUMPIXELS = 32 #LEDの数
Div = 200 #１周の分割数
 
#色閾値
#colTh = 64
 # Gifファイルを読み込む
# 参考 https://www.tech-tech.xyz/gif-divide.html

gif_file_name = "magic.gif"
im = Image.open(gif_file_name)
print(im.is_animated)

print(im.n_frames)
Frame=im.n_frames
#Frame = 10 #抽出フレーム数指定
gif = cv2.VideoCapture(gif_file_name)

 
#ファイル作成
file = open('graphics.h', 'w')
file.write('#define Frame ' + str(Frame) + '\n')
file.write('#define NUMPIXELS ' + str(NUMPIXELS) + '\n')
file.write('#define Div ' + str(Div) + '\n' + '\n')
#file.write('#define Frame ' + str(Frame) + '\n' + '\n')
 
 
file.write('const uint32_t pic [Frame][Div][NUMPIXELS] = {' + '\n')
 

 
 
#画像変換関数
def polarConv(pic, i):
    imgOrgin = cv2.imread(pic) #画像データ読み込み
    
    h, w, _ = imgOrgin.shape #画像サイズ取得
 
    #画像縮小
    imgRedu = cv2.resize(imgOrgin,(math.floor((NUMPIXELS * 2 -1)/h *w), NUMPIXELS * 2 -1))
    #cv2.imwrite(str(i) + '-resize.jpg',imgRedu)
 
    #縮小画像中心座標
    h2, w2, _ = imgRedu.shape
    wC = math.floor(w2 / 2)
    hC = math.floor(h2 / 2)
 
    #極座標変換画像準備
    imgPolar = Image.new('RGB', (NUMPIXELS, Div))
 
 
    #極座標変換
    file.write('\t{\n')
    for j in range(0, Div):
        file.write('\t\t{')
        for i in range(0, hC+1):
            #座標色取得
            #参考：http://peaceandhilightandpython.hatenablog.com/entry/2016/01/03/151320
            rP = int(imgRedu[hC + math.ceil(i * math.cos(2*math.pi/Div*j)),
                         wC - math.ceil(i * math.sin(2*math.pi/Div*j)), 2])
                     
            gP = int(imgRedu[hC + math.ceil(i * math.cos(2*math.pi/Div*j)),
                         wC - math.ceil(i * math.sin(2*math.pi/Div*j)), 1])
                     
            bP = int(imgRedu[hC + math.ceil(i * math.cos(2*math.pi/Div*j)),
                         wC - math.ceil(i * math.sin(2*math.pi/Div*j)), 0])
            
            file.write('0x%02X%02X%02X' % (rP,gP,bP))
            
            if i == hC:
                file.write('},\n')
            else:
                file.write(', ')
                
            imgPolar.putpixel((i,j), (rP, gP, bP))
                     
    file.write('\t},\n\n')
 
 
# スクリーンキャプチャを保存するディレクトリを生成
dir_name = "screen_caps"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
 

    
    
for i in range(Frame):
    is_success, frame = gif.read()
    
    # 画像ファイルに書き出す
    img_name = str(i) + ".png"
    img_path = os.path.join(dir_name, img_name)
    
    cv2.imwrite(img_path, frame)
    #変換
    polarConv(img_path, i)
    
 
 
file.write('};' + '\n' + '\n')
file.close()
