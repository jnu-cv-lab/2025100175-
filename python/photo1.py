import cv2
import numpy as np
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, 'test.jpg')

if os.path.exists(img_path):
    
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    
    if img is not None:
        print("✅ 原图读取成功！")
        print(f"   原图尺寸: {img.shape}") 

        
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        print("✅ 灰度图转换完成！")
        print(f"   灰度图尺寸: {gray_img.shape}")  

        
        gray_path = os.path.join(current_dir, 'gray_test.jpg')
        cv2.imwrite(gray_path, gray_img)
        print(f"✅ 图片已保存至: {gray_path}")

        
        cv2.imshow('Original Image', img)
        cv2.imshow('Gray Image', gray_img)
        print("\n👀 图片已显示，按任意键退出...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("❌ 读取失败：文件存在，但无法解码。")
else:
    print("❌ 错误：文件不存在。")