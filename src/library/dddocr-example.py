import ddddocr

ocr = ddddocr.DdddOcr(beta=True)
img = open("price.png", "rb").read()
res = ocr.classification(img)
print(res)