import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("clean_user_behavior.csv")

# 每个品类下，pv、buy数量
view_data = df[df["behavior"] == "pv"].groupby("category_id").size()
buy_data = df[df["behavior"] == "buy"].groupby("category_id").size()

cate_df = pd.DataFrame({"pv": view_data, "buy": buy_data}).fillna(0)
cate_df["浏览转购买转化率"] = cate_df["buy"] / cate_df["pv"]
cate_df = cate_df[cate_df["pv"] > 0]
# 取出转化率最高TOP15
cate_top = cate_df.sort_values("浏览转购买转化率", ascending=False).head(15)
print("各品类转化率TOP15：")
print(cate_top)

# 绘图
plt.figure(figsize=(12,6))
plt.bar(cate_top.index.astype(str), cate_top["浏览转购买转化率"], color="#5588cc")
plt.title("各商品品类【浏览→购买】转化率TOP15")
plt.xlabel("品类ID")
plt.ylabel("转化率")
plt.grid(axis='y', alpha=0.3)
plt.xticks(rotation=45)
# 新增：Y轴显示百分比
from matplotlib.ticker import PercentFormatter
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.tight_layout()
plt.show()
