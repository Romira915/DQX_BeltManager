from PIL import Image
import sys
import pyocr
import pyocr.builders
import cv2
import BeltScreenshots as bs

def BelttoString(path):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    # 原稿画像の読み込み
    img_org = Image.open(path)
    img_rgb = img_org.convert("RGB")
    pixels = img_rgb.load()

    # 原稿画像加工（黒っぽい色以外は白=255,255,255にする）
    c_max = 190
    for j in range(img_rgb.size[1]):
        for i in range(img_rgb.size[0]):

            if (pixels[i, j][0] > c_max and pixels[i, j][1] > c_max and
                    pixels[i, j][0] > c_max):
                pixels[i, j] = (0, 0, 0)
    c_max = 0
    for j in range(img_rgb.size[1]):
        for i in range(img_rgb.size[0]):
            if (pixels[i, j][0] > c_max or pixels[i, j][1] > c_max or
                    pixels[i, j][0] > c_max):
                pixels[i, j] = (255, 255, 255)

    res = tool.image_to_string(img_rgb, lang="jpn",
                            builder=pyocr.builders.TextBuilder(tesseract_layout=6))

    res = res.replace("\n\n","\n")
    print(res)
    return res

    # img = cv2.imread("conv.png")
    # cv2.imshow("img", img)
    # cv2.waitKey()
