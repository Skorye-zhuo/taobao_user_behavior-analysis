import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 替换成你导出的csv文件名
df = pd.read_csv("buy_count.csv")

plt.figure(figsize=(10,5))
# 直方图：x轴是用户的购买次数
plt.hist(df["buy_cnt"], bins=range(0, df["buy_cnt"].max()+2), alpha=0.7, color="#4472C4")
plt.title("用户购买次数分布直方图")
plt.xlabel("购买次数")
plt.ylabel("用户人数")
plt.xticks(range(0, df["buy_cnt"].max()+1))
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()



