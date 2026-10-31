
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