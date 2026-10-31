import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. 路径配置（绝对路径，跟 01 和 02 保持高度一致）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "clean_user_behavior.csv")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

if not os.path.exists(FIGURES_DIR):
    os.makedirs(FIGURES_DIR)

# 2. 绘图配置
plt.close("all")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 3. 读取数据
df = pd.read_csv(DATA_PATH)

# 4. 动态计算各阶段数据
stage = ["浏览(pv)", "加购(cart)", "收藏(fav)", "购买(buy)"]
nums = [
    len(df[df["behavior"] == "pv"]),
    len(df[df["behavior"] == "cart"]),
    len(df[df["behavior"] == "fav"]),
    len(df[df["behavior"] == "buy"])
]

# 5. 计算相对第一步（浏览）的转化率
rates = [num / nums[0] for num in nums]

# 6. 绘图
plt.figure(figsize=(10, 6))
bars = plt.bar(stage, nums, color=["#4472C4", "#5B9BD5", "#70AD47", "#ED7D31"])

# 对数坐标
plt.yscale("log")   
plt.title("电商用户转化漏斗图（对数坐标）")
plt.ylabel("行为次数（对数）")
plt.ylim(bottom=1000, top=max(nums) * 2) 

# 7. 在柱子上标出具体数值 和 转化率
for bar, num, rate in zip(bars, nums, rates):
    yval = bar.get_height()
    # 拼接字符串：类似 "1820\n(2.34%)"
    display_text = f"{num}\n({rate:.2%})"
    plt.text(bar.get_x() + bar.get_width()/2, yval, 
             display_text, 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# 8. 保存图表（改个规范的名字）
save_path = os.path.join(FIGURES_DIR, "03_funnel_analysis.png")
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"漏斗图已成功保存至: {save_path}")

# 9. 展示
plt.show()
