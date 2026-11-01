import os
import pandas as pd
import matplotlib.pyplot as plt

# ================= 1. 全局配置 =================
# 解决图表中文乱码和负号显示问题（画图必备）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 动态获取项目根目录 (为了后续读写文件不报错)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼接绝对路径（读取路径 & 保存路径）
csv_path = os.path.join(BASE_DIR, "data", "WITH__PV__Buy.csv")
save_path = os.path.join(BASE_DIR, "figures", "06_high_traffic_low_conv.png")

# ================= 2. 读取数据 =================
# 加上防御性判断：万一文件没找到，给出友好提示，而不是一堆红字报错
if not os.path.exists(csv_path):
    print(f"❌ 报错：找不到数据文件，请检查路径：{csv_path}")
    exit()

df = pd.read_csv(csv_path)

# ================= 3. 准备画图 =================
plt.figure(figsize=(10, 6))

# 使用 range 生成 x 坐标，使两根柱子上下错开
x = range(len(df))

# ================= 4. 绘制双柱状图 =================
# 注意：把 item_id 转成字符串格式，防止 Y 轴数字过长导致重叠
y_labels = df['item_id'].astype(str).tolist()

plt.barh(x, df['pv_cnt'], height=0.4, label='浏览量 (PV)', color='skyblue')
# 使用列表推导式对 x 坐标做偏移，让两根柱子并排显示
plt.barh([i + 0.4 for i in x], df['buy_cnt'], height=0.4, label='购买量 (Buy)', color='salmon')

# ================= 5. 美化图表 =================
# 重新设置 Y 轴刻度，让两根柱子的中心点对齐标签
plt.yticks([i + 0.2 for i in x], y_labels)

plt.xlabel('数量', fontsize=12)
plt.title('高流量低转化 Top10 商品', fontsize=14, fontweight='bold')
plt.legend(loc='lower right')  # 图例放右下角，防止遮挡数据

# 让排名第一的商品排在最上面（符合人类阅读习惯）
plt.gca().invert_yaxis()

plt.tight_layout() # 自动调整边距，防止标签被截断

# ================= 6. 保存并展示 =================
# 确保 figures 文件夹存在，如果没有就自动创建
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, dpi=300) # dpi=300 保证图片高清
print(f"✅ 图片已成功保存至：{save_path}")

plt.show()