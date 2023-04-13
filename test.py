import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

f_us = open("C:/Learning/Python/美国.txt", "r", encoding="utf-8")
us_data = f_us.read()

f_jp = open("C:/Learning/Python/日本.txt", "r", encoding="utf-8")
jp_data = f_jp.read()

f_in = open("C:/Learning/Python/印度.txt", "r", encoding="utf-8")
in_data = f_in.read()

us_data = us_data[us_data.index("(") + 1:us_data.index(")")]
us_dict = json.loads(us_data)
us_trend_data = us_dict['data'][0]['trend']
us_x_data = us_trend_data['updateDate'][:314]
us_y_data = us_trend_data['list'][0]['data'][:314]

jp_data = jp_data[jp_data.index("(") + 1:jp_data.index(")")]
jp_dict = json.loads(jp_data)
jp_trend_data = jp_dict['data'][0]['trend']
jp_x_data = jp_trend_data['updateDate'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

in_data = in_data[in_data.index("(") + 1:in_data.index(")")]
in_dict = json.loads(in_data)
in_trend_data = in_dict['data'][0]['trend']
in_x_data = in_trend_data['updateDate'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="确诊人数", pos_left="center", pos_bottom="1%")
)

line.render()

f_us.close()
f_jp.close()
f_in.close()
