# 이미지 다루기(처리)
'''
PIL 라이브러리 이용
설치: pip install pillow
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont

im = Image.open('original.jpg')
print(im.format)
print(im.size)
print(im.mode)

output = 'output.jpg'

im.save(output) # 파일 저장
temp = Image.open(output)
temp.show()

# 썸네일 생성
im = Image.open('original.jpg')
size = (64,64)

im.thumbnail(size)
im.save(output)

temp = Image.open(output)