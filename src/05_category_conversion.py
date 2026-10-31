import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# 1. 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "clean_user_behavior.csv")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

# 2. 绘图配置
plt.close("all")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 3. 读取数据
df = pd.read_csv(DATA_PATH)

# 4. 统计每个品类下 pv 和 buy 的数量
view_data = df[df["behavior"] == "pv"].groupby("category_id").size()
buy_data = df[df["behavior"] == "buy"].groupby("category_id").size()

# 合并并填充缺失值
cate_df = pd.DataFrame({"pv": view_data, "buy": buy_data}).fillna(0)
cate_df["convert_rate"] = cate_df["buy"] / cate_df["pv"]

# 过滤掉 pv 为 0 的异常品类
cate_df = cate_df[cate_df["pv"] > 0]

# 取出转化率最高 TOP15
cate_top = cate_df.sort_values("convert_rate", ascending=False).head(15)
print("各品类转化率 TOP15 提取完毕！")

# 5. 绘图
plt.figure(figsize=(12, 6))
# 加了 edgecolor 让柱子有白边更好看
plt.bar(cate_top.index.astype(str), cate_top["convert_rate"], color="#5588cc", edgecolor="white")

plt.title("各商品品类【浏览→购买】转化率 TOP15")
plt.xlabel("品类 ID")
plt.ylabel("转化率")
plt.grid(axis='y', alpha=0.3)
plt.xticks(rotation=45)

# Y 轴显示百分比
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))

# 6. 保存图表（关键！）
save_path = os.path.join(FIGURES_DIR, "05_category_conversion.png")
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"品类转化率图已成功保存至: {save_path}")

plt.show()
