

"""
运行代码-->> "render.html"-->>> 浏览器


from pyecharts import ...    #pip install pyecharts==0.1.9.4/0.1.9.7

... = ...(Title, subTitle)
attr = [..., ...]
#attr = [..., ...]
v1 = [..., ...]
#v2 = [..., ...]
....add('...', attr, v1, is_...=True)
#....add('...', attr, v2, is_...=True)
....show_config()
....render()



Bar           >>> 条形图/柱状图/堆状图
Pie           >>> 饼图/比例图/玫瑰图
Line, Grid    >>> 折线图
EffectScatter >>> 散点图
Line          >>> 面积图
Pie,Timeline  >>> 时间表
Liquid        >>> 水球图
WordCloud     >>> 词云
Gauge         >>> 仪表盘图
"""


# encoding: utf-8
import time
from pyecharts import Bar       #pip install pyecharts==0.1.9.4


v1 = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v2 = [5, 20, 36, 10, 75, 90]
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", v1, v2, is_more_utils=True)
bar.show_config()
bar.render()
