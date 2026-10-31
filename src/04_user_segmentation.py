import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "clean_user_behavior.csv")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

# 2. 绘图配置
plt.close("all")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 3. 读取全量清洗数据
df = pd.read_csv(DATA_PATH)

# 4. 过滤出“购买”行为，并按用户分组统计购买次数
# 注意：这里只筛选 buy，天然就排除了 buy_cnt = 0 的纯浏览用户
buy_users = df[df["behavior"] == "buy"].groupby("user_id").size()

# 5. 绘制分布直方图
plt.figure(figsize=(10, 5))
# 设置 bins，x 轴从 1 开始（因为买过东西的至少是 1 次）
# edgecolor="white" 让柱子之间有白边，更好看
plt.hist(buy_users, bins=range(1, buy_users.max() + 2), alpha=0.8, color="#4472C4", edgecolor="white")

plt.title("真实购买用户的购买次数分布（长尾效应）")
plt.xlabel("购买次数")
plt.ylabel("用户人数")
plt.xticks(range(1, buy_users.max() + 1))
plt.grid(axis='y', alpha=0.3)

# 6. 保存图表
save_path = os.path.join(FIGURES_DIR, "04_user_purchase_distribution.png")
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"用户购买分布图已成功保存至: {save_path}")

plt.show()
