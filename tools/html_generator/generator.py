import os

num_images = 100  # 生成する画像の数
html_content = "<html><head><title>Test Page</title></head><body>"

for i in range(num_images):
    img_url = f"https://picsum.photos/200/300?random={i}"  # ダミー画像URL
    html_content += f"<img src='{img_url}' alt='Dummy Image {i}' />"

html_content += "</body></html>"

# 目的のディレクトリ
output_directory = "../../loading-static-page/http1.1/html"
output_file = os.path.join(output_directory, "complex.html")

# ディレクトリが存在するか確認し、存在しない場合は作成
os.makedirs(output_directory, exist_ok=True)

# HTMLファイルを指定したディレクトリに生成
with open(output_file, "w") as file:
    file.write(html_content)
