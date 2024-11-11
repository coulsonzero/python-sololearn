import pyautogui as pg
import time
from aip import AipOcr       # baidu-ocr
import re


def sleep(t):
    time.sleep(t)



class shoptitans:
    def __init__(self):
        # baidu-ocr
        self.APP_ID = '36397243'
        self.API_KEY = 'm3TDgRKKZuXRdqqocK7yXA6l'
        self.SECRET_KEY = '3yZyZGPkGihvAYYUsyLALZ7Sv9WCNxVa'

    def image_read(self):
        def get_file_content(filepath):
            with open(filepath, "rb") as fp:
                return fp.read()

        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        res_image = client.basicGeneral(get_file_content('assets/full_screen.png'))
        # price = res_image['words_result'][0]['words']
        # price = price.replace('+', '').replace('-', '').replace(',', '').replace("'", '').replace('.', '').replace('○', '')
        # return int(price)
        return res_image


if __name__ == '__main__':
    # sleep(1)

    # pg.screenshot('screen.png')
    # st = shoptitans()
    # res = st.image_read()

    # print(res)

    t = {
        'words_result': [
            {'words': '71'},
            {'words': '588/4.098'},
            {'words': '330.18M'},
            {'words': 'C1,944⊕'},
            {'words': 'Wanderer Lv,39 wants to buy'},
            {'words': 'Monsoon Heart'},
            {'words': '○1,750,000'},
            {'words': '480☑'},
            {'words': '+1.145'},
            {'words': 'Suggest'},
            {'words': '■■■'},
            {'words': 'Discount'},
            {'words': '2,545'},
            {'words': 'Small talk'},
            {'words': 'Surcharge'},
            {'words': '3'},
            {'words': '427'},
            {'words': 'Refuse'},
            {'words': 'Sell'},
            {'words': 'Wait'},
            {'words': '激活Vindows'},
            {'words': '转到"设置"以激活Vindows,'}
        ],
        'words_result_num': 22,
        'log_id': 1681624525666239894
    }

    s = str(t)
    surcharge_energy = list(filter(lambda x: x != ',', re.compile("[0-9|,|.]+", re.S).findall(s[s.find('Surcharge'):s.find('Refuse')])))[-1]
    print(surcharge_energy)

    # price = [e for e in re.compile("[○]?([0-9|,]+)", re.S).findall(s[s.find('buy'):s.find('Suggest')]) if e != ',']
    # energy = re.compile("[0-9|,|.]+/[0-9|,|.]+", re.S).findall(s)[0].split('/')
    # surcharge_energy = \
    # list(filter(lambda x: x != ',', re.compile("[0-9|,|.]+", re.S).findall(s[s.find('Surcharge'):s.find('Refuse')])))[
    #     -1]

    # ans = {
    #     'level': '71',
    #     'energy': '588/4098',
    #     'cur_gold': '330.18M',
    #     'pearls': '1944',
    #     'price': '1,750,000',
    #     'suggest_energy': '180',
    #     'discount_energy': '2040',
    #     'surcharge_energy': '4076',
    #     'sell_energy': '27',
    # }
    #
    # m = {
    #     'energy': res['words_result'][1]['words'],
    #     'price': res['words_result'][7]['words'],
    #     'discount_energy': res['words_result'][9]['words'],
    #     'surcharge_energy': res['words_result'][13]['words']
    # }
    # print(m)





    # s = str(res)
    # l = {
    #     'energy': list(map(int, re.compile("\d+[,]?\d+/\d+[.|,]\d+", re.S).findall(s)[0].replace(".", "").replace(",","").split("/"))),
    #     'price': re.compile("[○|⊙](\d+[,]?\d+[,]?\d+)", re.S).findall(s),
    #     'surcharge_energy':  int(re.compile("[+](\d+[,|.]?\d+)", re.S).findall(s)[0].replace(',', '').replace(".", ''))*2
    # }
    #
    # print(l)





    # 'words': '○9,050,000'
    # 'words': '⊙530,000'
    # '017,000'



# {'words_result': [{'words': '710'}, {'words': '588/4.098'}, {'words': 'J330.18M'}, {'words': '21,944⊕'}, {'words': 'Barbarian Lv.37 wants to buy'}, {'words': '/Excalibu四'}, {'words': '○5,250,000'}, {'words': '9'}, {'words': '453'}, {'words': '+1,405'}, {'words': 'Suggest'}, {'words': 'Discount'}, {'words': '80'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': '3'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': '激活Vindows'}, {'words': '转到设置"以激活Windows。.'}], 'words_result_num': 22, 'log_id': 1681621773851829156}
# {'words_result': [{'words': '71'}, {'words': '588/4.098'}, {'words': '330.18M'}, {'words': 'C1,944⊕'}, {'words': 'Wanderer Lv,39 wants to buy'}, {'words': 'Monsoon Heart'}, {'words': '○1,750,000'}, {'words': '480☑'}, {'words': '+1.145'}, {'words': 'Suggest'}, {'words': '■■■'}, {'words': 'Discount'}, {'words': '2,545'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': '3'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': '激活Vindows'}, {'words': '转到"设置"以激活Vindows,'}], 'words_result_num': 22, 'log_id': 1681624525666239894}

# {'words_result': [{'words': '7列'}, {'words': '348/4.098'}, {'words': '330.18M'}, {'words': '1,944⊕'}, {'words': 'Soldier Lv.36 wants to buy.'}, {'words': '⑨'}, {'words': 'Star-Spangled Plate'}, {'words': '○530,000'}, {'words': '2'}, {'words': '335'}, {'words': '+450'}, {'words': 'Suggest'}, {'words': 'Discount'}, {'words': '904'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': 'X'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': '激活Vindows'}, {'words': '转到设置"以激活Windows'}], 'words_result_num': 23, 'log_id': 1681627763765465005}
# {'words_result': [{'words': '71'}, {'words': '348/4.098'}, {'words': '330.18M'}, {'words': '1,944⊕'}, {'words': 'Soldier Lv.36 wants to buy.'}, {'words': '⑨'}, {'words': 'Star-Spangled Plate'}, {'words': '⊙530,000'}, {'words': '335'}, {'words': '+450'}, {'words': 'Suggest'}, {'words': 'Discount'}, {'words': '904'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': 'X'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': 'C空'}, {'words': '激活Vindows'}, {'words': '转到设置"以激活Windows'}], 'words_result_num': 23, 'log_id': 1681629100577675894}
# {'words_result': [{'words': '348/4.098'}, {'words': '330.18M'}, {'words': 'C>1,944⊕门'}, {'words': 'Musketeer Lv.37 wants to buy'}, {'words': 'Djinn Pyre'}, {'words': '○9,050,000'}, {'words': '317'}, {'words': '+2,040'}, {'words': 'Suggest'}, {'words': 'Discount'}, {'words': 'O'}, {'words': '以'}, {'words': '-4.076'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': '0'}, {'words': 'X'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': '激活Vindows'}, {'words': '转到设置"以激活Windows。'}], 'words_result_num': 23, 'log_id': 1681632664832266531}
# {'words_result': [{'words': '71'}, {'words': '548/4,098'}, {'words': '330.18M'}, {'words': '>1,944⊕'}, {'words': 'Musketeer Lv.37 wants to buy'}, {'words': '⑤'}, {'words': 'XL Magic Potion'}, {'words': '○17,000'}, {'words': '325'}, {'words': '+85'}, {'words': 'Suggest'}, {'words': '■■'}, {'words': 'Discount'}, {'words': '☑.八'}, {'words': '190'}, {'words': 'Small talk'}, {'words': 'Surcharge'}, {'words': 'X'}, {'words': '427'}, {'words': 'Refuse'}, {'words': 'Sell'}, {'words': 'Wait'}, {'words': '激活Vindows'}, {'words': '转到"设置"以激活Vindows。'}], 'words_result_num': 24, 'log_id': 1681627460435602663}

