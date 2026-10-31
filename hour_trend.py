import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

plt.close("all")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读你刚从MySQL导出的小时统计csv
df = pd.read_csv("hour_trend.csv")

plt.figure(figsize=(12,6))
# 蓝线：浏览量pv
plt.plot(df["hour"], df["pv_total"], marker='o', color='#2E86AB', linewidth=2, label="浏览量pv")
# 橙线：购买量buy
plt.plot(df["hour"], df["buy_total"], marker='s', color='#F24236', linewidth=2, label="购买量buy")

plt.title("一天24小时：浏览量 vs 购买量趋势")
plt.xlabel("小时")
plt.ylabel("次数")
plt.xticks(range(0,24))
plt.grid(alpha=0.3)
plt.legend() # 显示图例，区分两条线

plt.tight_layout()
plt.show()
