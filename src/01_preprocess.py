import pandas as pd

df = pd.read_csv("small_UserBehavior.csv")
df.columns=["user_id","item_id","category_id","behavior","timestamp"]

#时间截转成日期时间
df["time"] = pd.to_datetime(df["timestamp"],unit="s")
#提取小时，后面分析用户活跃时间段用
df["hour"] = df["time"].dt.hour
#过滤掉异常时间（时间范围2017-11-25~2017-12-03）
start_time = pd.to_datetime("2017-11-25")
end_time = pd.to_datetime("2017-12-03")
df = df[(df["time"]>=start_time) & (df["time"]<end_time)]
#查看数据清理后的前五行
print("清理完成，查看前五行数据: ")
print(df.head())
#查看四种行为分别有多少数量
print("\n各类行为统计: ")
print(df["behavior"].value_counts())
#保存清洗好的数据，sql,绘图都用这个
df.to_csv("clean_user_behavior.csv",index=False,encoding="utf-8")
print("\n清洗完毕，已保存 clean_user_behavior.csv")
