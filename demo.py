from pyecharts.charts import *
from pyecharts.globals import ThemeType
from pyecharts.options import *

f = open("D:/1960-2019全球GDP数据.csv", "r", encoding="ANSI")
data_all = f.readlines()
f.close()
data_all.pop(0)  # 删除第一条无关的数据
# print(data_all)
data_dict = {}
for line in data_all:
    line = line.split(",")
    year = line[0]
    country = line[1]
    GDP = float(line[2])
    try:
        data_dict[year].append([country, GDP])
    except:
        data_dict[year] = []
        data_dict[year].append([country, GDP])
# print(data_dict)
timeline1 = Timeline({"theme": ThemeType.CHALK})
for year1 in data_dict:
    data_dict[year1].sort(key=lambda ele: ele[1], reverse=True)
    top8 = data_dict[year1][:8]

    # print(top8)
    data_country = []
    data_gdp = []
    for cou in top8:
        data_country.append(cou[0])
        data_gdp.append(cou[1])
    # print(data_country)
    # 创建每一年的柱状图
    bar = Bar()
    bar.add_xaxis(data_country)


    # bar.add_yaxis(f"{year1}全球前8GDP国家", data_gdp)
    # bar.add_yaxis(f"{year1}全球前8GDP国家", data_gdp, label_opts=LabelOpts(position="top"))

    bar.add_yaxis("GDP", data_gdp, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(is_show=True, title=f"{year1}全球前八GDP国家")
    )
    # 添加时间线
    timeline1.add(bar, f"{year1}")

# 配置时间线
timeline1.add_schema(
    is_loop_play=True,
    is_auto_play=True,
    is_timeline_show=True,
    play_interval=500
)
timeline1.render("1960-2014全球前八GDP国家.html")
