'''
<p class="price">
    <span class="pricedetail">
        "¥"
        <strong>698.00</strong>
    </span>
    <span class="postalicon">
    包邮
    </span>
</p>
<span class="title" title="双面羊绒大衣女毛呢外套100%羊毛双面绒">双面羊绒大衣女毛呢外套100%羊毛双面绒</span>
<p class="shopName">
    <span class="shopNick">zhaoxiaofangxj</span>
    <span class="payNum">190人付款</span>
</p>

output：
价格：¥698.00
标题：双面羊绒大衣女毛呢外套100%羊毛双面绒
店铺：zhaoxiaofangxj
付款：190人付款
'''



import re


html = """
<p class="price">
    <span class="pricedetail">
        "¥"
        <strong>698.00</strong>
    </span>
    <span class="postalicon">
    包邮
    </span>
</p>
<span class="title" title="双面羊绒大衣女毛呢外套100%羊毛双面绒">双面羊绒大衣女毛呢外套100%羊毛双面绒</span>
<p class="shopName">
    <span class="shopNick">zhaoxiaofangxj</span>
    <span class="payNum">190人付款</span>
</p>
"""


"""
价格：¥698.00
标题：双面羊绒大衣女毛呢外套100%羊毛双面绒
店铺：zhaoxiaofangxj
付款：190人付款
"""


regex = """
<p class="price">
    <span class="pricedetail">
        "(.*?)"
        <strong>(.*?)</strong>
    </span>
    .*?
</p>
<span class="title" title="(.*?)">.*?</span>
<p class="shopName">
    <span class="shopNick">(.*?)</span>
    <span class="payNum">(.*?)</span>
</p>
"""
pattern = re.compile(regex, re.S)
r_list = pattern.findall(html)
print(r_list)
text = r_list[0]
for i in r_list:
    print('商品:', i[2])
    print(f'价格: {i[0]}{i[1]}')
    print('店铺:',i[3])
    print('付款:',i[4])
