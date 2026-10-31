import pandas as pd
df = pd.read_csv("clean_user_behavior.csv")
#统计各个行为的数量
pv_count = len(df[df["behavior"] == "pv"])
cart_count = len(df[df["behavior"] == "cart"])
fav_count = len(df[df["behavior"] == "fav"])
buy_count = len(df[df["behavior"] == "buy"])
print("=====电商行为漏洞=====")
print(f"浏览 pv: {pv_count}")
print(f"浏览 cart: {cart_count}")
print(f"浏览 fav: {fav_count}")
print(f"浏览 buy: {buy_count}")
print("\n=====转化率=====")
print(f"浏览->加购转化率: {cart_count/pv_count:.2%}")
print(f"浏览->收藏转化率: {fav_count/pv_count:.2%}")
print(f"浏览->购买转化率: {buy_count/pv_count:.2%}")
print(f"加购->购买转化率: {buy_count/cart_count:.2%}")

import matplotlib.pyplot as plt
plt.close("all")
#设置中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
#数据
stage = ["浏览","加购","收藏","购买"]
nums = [77817,4720,2294,1820]


plt.figure(figsize=(10,6))
plt.bar(stage,nums,color=["#4472C4","#5B9BD5","#70AD47","#ED7D31"])
plt.yscale("log")   # 关键改动
plt.title("电商用户转化漏斗图（对数坐标）")
plt.ylabel("行为次数（对数）")
#柱上标数字
for i,value in enumerate(nums):
    plt.text(i,
             value,
             str(value),
             ha="center",
             va="bottom",
             fontsize=11
             )
    plt.ylim(bottom=1000,top=max(nums)*2)
    plt.show()
