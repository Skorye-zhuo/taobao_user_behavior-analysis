import os
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(BASE_DIR, "data", "funnel_data.csv")
save_path = os.path.join(BASE_DIR, "figures", "07_funnel_analysis.png")

df = pd.read_csv(csv_path)

# 提取数据并倒序（为了画漏斗）
steps = ['浏览 (PV)', '加购 (Cart)', '收藏 (Fav)', '购买 (Buy)']
counts = [df['pv_user_cnt'][0], df['cart_user_cnt'][0], df['fav_user_cnt'][0], df['buy_user_cnt'][0]]

plt.figure(figsize=(8, 5))
bars = plt.barh(steps[::-1], counts[::-1], color=['#2ecc71', '#3498db', '#9b59b6', '#e74c3c'])

# 在柱子中间标数字
for bar in bars:
    width = bar.get_width()
    plt.text(width / 2, bar.get_y() + bar.get_height()/2,
             f'{int(width):,}', ha='center', va='center', color='white')

plt.xlabel('用户人数')
plt.title('电商全链路用户转化漏斗') # 我去掉了 bold，防止报红字
plt.tight_layout()

plt.savefig(save_path, dpi=300)
print(f"✅ 漏斗图已保存至: {save_path}")
plt.show()
#以下是完美按照漏斗顺序来的
#WITH user_time_agg AS (
#    SELECT
#        user_id,
#        MIN(IF(behavior='pv', `timestamp`, NULL)) AS pv_time,
#        MIN(IF(behavior='cart', `timestamp`, NULL)) AS cart_time,
#       MIN(IF(behavior='fav', `timestamp`, NULL)) AS fav_time,
#       MIN(IF(behavior='buy', `timestamp`, NULL)) AS buy_time
#   FROM clean_user_behavior
#   GROUP BY user_id
#)
#SELECT
#    -- 条件1：看过
#    SUM(IF(pv_time IS NOT NULL, 1, 0)) AS pv_user,
#    -- 条件2：看过，且加购时间晚于浏览时间
#    SUM(IF(pv_time IS NOT NULL AND cart_time > pv_time, 1, 0)) AS cart_user,
#     -- 条件3：看过且加购，且收藏晚于加购
#    SUM(IF(cart_time > pv_time AND fav_time > cart_time, 1, 0)) AS fav_user,
#    -- 条件4：按顺序走完全程
#    SUM(IF(fav_time > cart_time AND buy_time > fav_time, 1, 0)) AS buy_user
# FROM user_time_agg;