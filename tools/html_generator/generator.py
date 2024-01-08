import os

def generate_html_with_images(image_directory, output_html_file):
    image_files = os.listdir(image_directory)
    image_files = [file for file in image_files if file.endswith('.png')]

    html_content = "<html><head><title>Image Gallery</title></head><body>"

    for image_file in image_files:
        image_src = f"http://localhost:8081/photos/{image_file}"
        html_content += f"<img src='{image_src}' alt='{image_file}' /><br>"

    html_content += "</body></html>"

    with open(output_html_file, "w") as file:
        file.write(html_content)

# 画像が保存されているディレクトリとHTMLファイルの出力パス
image_directory = "../../loading-static-page/assets/photos"
output_html_file = "../../loading-static-page/assets/html/index.html"

generate_html_with_images(image_directory, output_html_file)
