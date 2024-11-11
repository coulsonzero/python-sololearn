import math
import time
from functools import wraps  # decorator

import pyautogui as pg
from PIL import ImageGrab    # image save
from aip import AipOcr       # baidu-ocr
import re


APP_ID = '24768609'
API_KEY = 'BNPXUxglAyM8QcG1RRZ9z1RF'
SECRET_KEY = 'b51CqlbZy3TOissI5SSGhdjVCW9Kj24C'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
'''
pip install pyautogui
pip install opencv-python       # if you need the `confidence` option
'''


class Shop_Titans:
    def __init__(self):
        # baidu-ocr

        # screenshot image
        self.img_price    = 'assets/ocr/price.png'
        self.img_screen   = 'assets/ocr/screen.png'
        # suggest
        self.suggest_more = 'assets/sale/suggest_more.png'
        self.suggest_low  = 'assets/sale/t1.png'


        # ---- sale ----- #
        self.price_map: dict = {'surcharge': 1_000_000, 'discount': 300_000}
        self.dpi: int = 2

        self.error_cnt = 0

        # ---- craft ----- #

        # you need to change it !!!
        self.suggest_more_point = (586, 426)     # full screen
        self.wait_guest_point   = (722, 520)     # full screen


    def now(self):
        return time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d


    """
    ocr
    """
    def get_fullscreen(self) -> object:
        def get_file_content(filepath):
            with open(filepath, "rb") as fp:
                return fp.read()
        # ocr
        res_image = client.basicGeneral(get_file_content(self.img_screen))
        return res_image

    def get_fullscreen_info(self, shot=False) -> object:
        # shot
        if shot:
            pg.screenshot(self.img_screen)
        # ocr
        res = self.get_fullscreen()

        # get info
        s = str(res)

        if s.find("error_code") != -1:
            print("[error] cannot connect the ocr api.")
            print(res)
            pg.press('d', interval=0.5)
            if self.error_cnt > 10:
                exit(1)
            self.error_cnt += 1
            return

        try:
            # buy | bug | bu | to:buu
            price = [e for e in re.compile("[○|0]([0-9|,]+)", re.S).findall(s[s.find('wants to'):s.find('Suggest')]) if e != ','][0]
            energy = re.compile("[0-9|,|.]+/[0-9|,|.]+", re.S).findall(s)[0].split('/')
            surcharge_energy = [e for e in re.compile('[-]?([0-9|,]+)', re.S).findall(s[s.find('Suggest'):s.find('Refuse')]) if e != ','][0]
            discount_energy = re.compile('[+]([0-9|,]+)', re.S).findall(s)[0]
        except:
            print("[error] re regx info error!")
            print(res)
            pg.press('d', interval=0.5)
            return

        if discount_energy is not None or int(surcharge_energy) < int(discount_energy.replace(',', '')):
            # surcharge_energy = str(int(discount_energy.replace(',', '')) * 2)
            surcharge_energy = f"{int(discount_energy.replace(',', '')) * 2:,d}"
        # surcharge_energy = list(filter(lambda x: x != ',', re.compile("[-][0-9|,|.]+", re.S).findall(s[s.find('Surcharge'):s.find('Refuse')])))[-1]

        ans = {'price': price, 'energy': energy, 'surcharge_energy': surcharge_energy, 'discount_energy': discount_energy}
        # if not shot: pg.alert(text=ans, button="OK")
        return ans

    def isvalid_fullscreen_info(self, ans: dict) -> bool:
        # if ans is None or ans == []:
        #     return False
        if ans['surcharge_energy'] == '' or ans['price'] == '' or ans['energy'] == []:
            return False
        return True

    def get_info(self, ans: dict) -> dict:
        ans['price'] = int(ans['price'].replace(',', ''))
        ans['energy'] = list(map(lambda x: int(x.replace(',', '').replace('.', '')), ans['energy']))
        ans['surcharge_energy'] = int(ans['surcharge_energy'].replace(',', ''))
        ans['discount_energy'] = int(ans['discount_energy'].replace(',', ''))
        return ans


    def sale(self):
        print("--------- sale --------")
        # ocr info
        ans = self.get_fullscreen_info(shot=True)
        if not self.isvalid_fullscreen_info(ans):
            print("[ERROR] Invalid OCR!")
            return
        print("[{0} sale] {1}".format(self.now(), ans))
        ans = self.get_info(ans)
        price = ans['price']
        energy = ans['energy'][0]
        surcharge_energy = ans['surcharge_energy']
        discount_energy = ans['discount_energy']

        # discount
        if price < self.price_map['discount']:
            pg.press('s', interval=0.3)
            pg.press('e', interval=0.3)
            pg.press('c')
            print("[{0} sale] discount...".format(self.now()))
        # surcharge
        elif price > self.price_map['surcharge']:
            # has enough energy
            if energy > surcharge_energy or energy > 1850:
                # surcharge
                pg.press('f', interval=0.5)
                pg.press('s', interval=0.5)
                pg.press('c', interval=0.5)
                print("[{0} sale] success to surcharge !!!".format(self.now()))
            # tips: maybe can surcharge!
            elif energy > surcharge_energy/2:
                # pass
                pg.press('d', interval=0.5)
                print("[{0} tip] skip over... !!!".format(self.now()))
            # cannot to surcharge
            else:
                print("[error] energy: %d, surcharge_energy: %d".format(energy, surcharge_energy))
                if self.find_suggest_more():
                    self.find_suggest_low()

        # not discount or surcharge(middle)
        else:
            print("[sale] sale directly ")
            pg.press('s', interval=0.5)
            pg.press('c', interval=0.5)


        """
        # small talk
        pg.press('s', interval=0.5)
        fail = pg.locateCenterOnScreen("fail.png", confidence=0.6)
        if fail is None and base_price is not None:
            print(f"[{self.now()} sale] small talk: success")
        else:
            pg.press('z', interval=0.5)
            print(f"[{self.now()} sale] small talk: backfired!")
            return

        '''
        discount
        surcharge(energy enough) | suggest 
        '''
        if base_price < self.price_map["discount"]:
            # discount
            pg.press('e', interval=0.5)
            pg.press('c', interval=0.5)
            self.sale_discount += 1
            print(f"[{self.now()} sale] discount: {self.sale_discount}")
        elif base_price > self.price_map["surcharge"]:
            # surcharge?
            pg.press('f')
            self.image_save()
            surcharge_price = self.image_read()
            time.sleep(1)
            if surcharge_price >= 2 * base_price:
                # surcharge
                pg.press('c', interval=0.5)
                self.sale_surcharge += 1
                print(f"[{self.now()} sale] surcharge: {self.sale_surcharge}")
            else:
                # click suggest more
                suggest_more = pg.locateCenterOnScreen('assets/suggest_more.png', confidence=0.8)
                if suggest_more is None:
                    print("not found suggest more!")
                    pg.press('c')
                    return
                else:
                    x, y = suggest_more
                    pg.moveTo(int(x/self.dpi), int(y/self.dpi))
                    pg.click()
                    print("suggest more")

                # exchange to t1 or t2
                t1 = pg.locateCenterOnScreen('assets/t1.png', confidence=0.5)
                if t1 is None:
                    pg.press('space', interval=1)
                    pg.press('z', interval=1)
                    # print("fail to suggest more t1!")
                    print("suggest: fail!")
                    return
                else:
                    x, y = t1
                    pg.moveTo(int(x/self.dpi), int(y/self.dpi))
                    pg.click()
                    pg.press('s', interval=0.5)
                    pg.press('e', interval=0.5)
                    pg.press('c', interval=0.5)
                    print("suggest: success")

        else:
            # sale
            self.sale_discount += 1
            print(f"[{self.now()} sale] directly: {self.sale_directly}")
            pg.press('c', interval=0.5)
            
        """
    def find_suggest_more(self) -> bool:
        # click suggest more
        suggest_more = pg.locateCenterOnScreen(self.suggest_more, confidence=0.8)
        if suggest_more is None:
            print("[suggest] not found suggest more!")
            pg.press('c', interval=0.5)
            return False
        x, y = suggest_more
        # pg.click(int(x / self.dpi), int(y / self.dpi))
        pg.click(self.suggest_more_point)
        print("[suggest] suggest more success")
        return True

    def find_suggest_low(self):
        # exchange to t1 or t2
        t1 = pg.locateCenterOnScreen(self.suggest_low, confidence=0.5)
        if t1 is None:
            pg.press('space', interval=0.5)
            pg.press('z', interval=0.5)
            print("[suggest] fail to suggest more t1!")
            return
        x, y = t1
        pg.click(int(x / self.dpi), int(y / self.dpi))
        pg.press('s', interval=0.5)
        pg.press('e', interval=0.5)
        pg.press('c', interval=0.5)
        print("[suggest] success to suggest more t1.")

    def main(self):
        try:
            while True:
                self.sale()
        except Exception:
            # -- buy -- ?
            self.buy()
            # -- restock -- ?
            self.restock()
            # -- reconnnect -- ?
            self.reconnect()
            # -- wait -- ?
            self.wait()
            # print("except")
            # time.sleep(2)
            pass





    # -- npc送装备 -- ？
    def buy(self):
        buy = pg.locateCenterOnScreen('assets/buy/buy.png', confidence=0.5)
        # print(buy)  # 948, y=588 Point(x=1883, y=1179)
        if buy is not None:
            pg.press('s', interval=0.5)
            pg.press('c', interval=0.5)
            print(f"[{self.now()} buy] success buy")
        else:
            print("not found the buy.")

    # -- 缺货 -- #
    def restock(self):
        time.sleep(1)

        # 缺货 restock？
        restock = pg.locateCenterOnScreen('assets/restock/restock.png', confidence=0.5)
        if restock is not None:
            x, y = restock
            # pg.click(int(x/self.dpi), int(y/self.dpi))
            pg.press('c', interval=0.5)
            time.sleep(1)

        # market
        market = pg.locateCenterOnScreen('assets/restock/market.png', confidence=0.5)
        if market is not None:
            x, y = market
            pg.click(int(x/self.dpi), int(y/self.dpi))
            time.sleep(1)

        # gold
        gold = pg.locateCenterOnScreen('assets/restock/gold.png', confidence=0.5)
        if gold is not None:
            x, y = gold
            # pg.moveTo(int(x/self.dpi), int(y/self.dpi))
            pg.moveTo(int(x/self.dpi), int(y/self.dpi)+30, interval=1)
            pg.click(clicks=10, interval=1)
            time.sleep(1)

        # sell
        sell = pg.locateCenterOnScreen('assets/restock/sell.png', confidence=0.5)
        if sell is not None:
            # x, y = sell
            # pg.click(int(x/self.dpi), int(y/self.dpi))
            pg.press('c', interval=0.5)
            time.sleep(1)

        
    def wait(self):
        pg.click(self.wait_guest_point)
        fail = pg.locateCenterOnScreen("assets/error/fail.png", confidence=0.6)
        if fail is None:
            print("youu need to wait it for 2s")
            time.sleep(2)
        else:
            print("not need to wait...")



    def reconnect(self):
        reconnect = pg.locateCenterOnScreen('assets/error/reconnect.png', confidence=0.5)
        if reconnect is not None:
            x, y = reconnect
            pg.moveTo(int(x/self.dpi), int(y/self.dpi))
            pg.click()
            print("reconnect...")
            time.sleep(6)

    def get_screen_dpi(self) -> int:
        # dpi default is 2
        time.sleep(2)
        w, h = pg.size()
        img = pg.screenshot('all_screen.png')
        screen_dpi = int(img.size[0] / w)
        print(screen_dpi)
        return screen_dpi

    # def dpi_xy(self, x, y) -> (int, int):
    #     return int(x / self.dpi), int(y / self.dpi)

    def test_ocr(self):
        shop = Shop_Titans()
        print(shop.get_fullscreen_info(False))


if __name__ == '__main__':
    # pg.FAILSAFE = False
    pg.PAUSE = 0.5
    time.sleep(1)


    try:
        shop = Shop_Titans()
        while True:
            shop.main()
    except:
        print("main error")
        pass







