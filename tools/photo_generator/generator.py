from PIL import Image
import os

num_images = 100
output_directory = "../../loading-static-page/assets/photos"

# 出力ディレクトリの作成
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# ダミー画像の生成と保存
for i in range(num_images):
    image = Image.new('RGB', (200, 300), (i * 2 % 255, i * 3 % 255, i * 5 % 255))
    image.save(os.path.join(output_directory, f'image_{i}.png'))
