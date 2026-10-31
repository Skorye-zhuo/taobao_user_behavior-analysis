import pandas as pd
import matplotlib.pyplot as plt
import os

plt.close("all")
# 解决中文字体显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 读取数据
file_path = "clean_user_behavior.csv" # 建议后续改为 '../data/clean_user_behavior.csv'
df = pd.read_csv(file_path)

# 2. 动态计算各阶段数据（消除硬编码）
stage = ["浏览(pv)", "加购(cart)", "收藏(fav)", "购买(buy)"]
nums = [
    len(df[df["behavior"] == "pv"]),
    len(df[df["behavior"] == "cart"]),
    len(df[df["behavior"] == "fav"]),
    len(df[df["behavior"] == "buy"])
]

# 3. 绘图
plt.figure(figsize=(10, 6))
bars = plt.bar(stage, nums, color=["#4472C4", "#5B9BD5", "#70AD47", "#ED7D31"])

# 对数坐标：解决 PV 与 Buy 之间巨大的量级差异
plt.yscale("log")   
plt.title("电商用户转化漏斗图（对数坐标）")
plt.ylabel("行为次数（对数）")
plt.ylim(bottom=1000, top=max(nums) * 2) # 修复了你原本的缩进bug，移出循环

# 在柱子上标出具体数值
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, 
             int(yval), ha='center', va='bottom', fontsize=11)

# 4. 保存图表（关键：工程化必须留痕）
if not os.path.exists("../figures"):
    os.makedirs("../figures")
plt.savefig("../figures/funnel_log_scale.png", dpi=300, bbox_inches='tight')

# 5. 展示
plt.show()


