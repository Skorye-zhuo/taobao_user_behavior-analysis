import pandas as pd
import matplotlib.pyplot as plt

plt.close("all") # 清空旧画布，避免多出一堆图

# 中文设置
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取我们之前处理好的数据表
df = pd.read_csv("clean_user_behavior.csv")

# 按小时分组，统计每个小时的行为总次数
hour_count = df.groupby("hour").size()

plt.figure(figsize=(10, 5))
# 画折线，marker='o' 每个数据点画圆圈标记
plt.plot(hour_count.index, hour_count.values, marker='o', color='#2E86AB', linewidth=2)

plt.title("用户24小时活跃时段分布")
plt.xlabel("一天中的小时")
plt.ylabel("操作次数")
plt.xticks(range(0,24)) # x轴显示0~24全部小时
plt.grid(alpha=0.3) # 淡淡的网格，方便看数值

# 找出活跃最高的小时和数量
max_hour = hour_count.idxmax()
max_count = hour_count.max()
print(f"用户活跃最高峰：{max_hour}点，总操作次数：{max_count}")
#========== 在图上标注最高峰 ==========
plt.annotate(f'峰值：{max_hour}点\n{max_count}次',
              xy=(max_hour, max_count),          # 箭头指向峰值点
              xytext=(max_hour+1, max_count*0.9),# 文字放在哪个位置
              arrowprops=dict(arrowstyle='->', color='red'),
              fontsize=11,
              color='red'
              )
plt.show()
