from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '24768609'
API_KEY = 'BNPXUxglAyM8QcG1RRZ9z1RF'
SECRET_KEY = 'b51CqlbZy3TOissI5SSGhdjVCW9Kj24C'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


# 调用通用文字识别（标准版）
res_image = client.basicGeneral(get_file_content('../assets/ocr/price.png'))
print(res_image)
print(res_image['words_result'][0]['words'])

# {'words_result': [{'words': '9,050,000'}], 'words_result_num': 1, 'log_id': 1681329640863021256}
# 9,050,000