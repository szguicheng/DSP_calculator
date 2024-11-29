from PIL import Image
import json
import os
def get_image_name():
    with open('src/data/item.json','r') as f:
        data = json.load(f)
    return data


def split_image(image_path, rows, cols):
    # 打开原始图片
    image = Image.open(image_path)
    img_width, img_height = image.size

    # 计算每个子图片的宽度和高度
    tile_width = img_width // cols
    tile_height = img_height // rows
    data = get_image_name()
    i = 0
    # 分割图片并保存子图片
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = (col + 1) * tile_width
            lower = (row + 1) * tile_height
            i+=1
            output_dir = f"{os.path.basename(data[i]["iconPath"])}"
            tile_name = f"{data[i]["iconPath"].split('/')[-1]}.png"
            # 裁剪子图片
            tile = image.crop((left, upper, right, lower))
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            tile_path = f"{output_dir}/{tile_name}.png"
            tile.save(tile_path, "PNG")

# 示例使用
image_path = "resources/Item_pic.webp"
rows = 14  # 分割成4行
cols = 14  # 分割成4列

split_image(image_path, rows, cols)