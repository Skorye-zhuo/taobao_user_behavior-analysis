import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. 路径配置
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

# 4. 分别计算每小时的 PV 和 Buy（不需要去读中间那个 hour_trend.csv）
pv_data = df[df["behavior"] == "pv"].groupby("hour").size()
buy_data = df[df["behavior"] == "buy"].groupby("hour").size()

# 5. 开始画图（双 Y 轴）
fig, ax1 = plt.subplots(figsize=(12, 6))

# 左轴：浏览量 PV
ax1.plot(pv_data.index, pv_data.values, marker='o', color='#2E86AB', linewidth=2, label="浏览量pv")
ax1.set_xlabel("小时")
ax1.set_ylabel("浏览量 PV", color='#2E86AB')
ax1.tick_params(axis='y', labelcolor='#2E86AB')
ax1.set_xticks(range(0, 24))
ax1.grid(alpha=0.3)

# 右轴：购买量 Buy
ax2 = ax1.twinx()  # 关键：共享 X 轴，创建第二个 Y 轴
ax2.plot(buy_data.index, buy_data.values, marker='s', color='#F24236', linewidth=2, label="购买量buy")
ax2.set_ylabel("购买量 Buy", color='#F24236')
ax2.tick_params(axis='y', labelcolor='#F24236')

# 找出活跃最高峰并标注
max_hour = pv_data.idxmax()
max_count = pv_data.max()
ax1.annotate(f'PV峰值：{max_hour}点\n{max_count}次',
              xy=(max_hour, max_count),
              xytext=(max_hour + 1, max_count * 0.8),
              arrowprops=dict(arrowstyle='->', color='gray'),
              fontsize=11,
              color='#2E86AB')

plt.title("一天24小时：浏览量 vs 购买量趋势 (双Y轴)")
fig.legend(loc="upper right", bbox_to_anchor=(0.9, 0.9))

# 6. 保存并展示
save_path = os.path.join(FIGURES_DIR, "02_hourly_trend.png") # 用英文命名
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"图表已成功保存至: {save_path}")

plt.show()
