import os
import pandas as pd

# 1. 获取项目根目录绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. 定义各个目录的路径
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_FULL_PATH = os.path.join(DATA_DIR, "UserBehavior.csv")       # 完整原始数据
RAW_SMALL_PATH = os.path.join(DATA_DIR, "small_UserBehavior.csv") # 切割后的数据
CLEAN_DATA_PATH = os.path.join(DATA_DIR, "clean_user_behavior.csv") # 最终清洗数据

# 3. 自动检查并创建文件夹
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ================= 步骤一：切割数据 =================
if not os.path.exists(RAW_SMALL_PATH):
    print(f"未找到 {RAW_SMALL_PATH}，准备切割...")
    try:
        max_rows = 100000
        count = 0
        with open(RAW_FULL_PATH, encoding="utf-8") as fr, open(RAW_SMALL_PATH, "w", encoding="utf-8") as fw:
            for line in fr:
                fw.write(line)
                count += 1
                if count >= max_rows:
                    break
        print(f"切割完成，已提取前 {max_rows} 行，保存为 small_UserBehavior.csv")
    except FileNotFoundError:
        print(f"【报错】找不到完整的原始数据，请确认它是否在 {RAW_FULL_PATH}")
        exit() # 找不到原始数据就退出，没必要往下跑

# ================= 步骤二：读取并清洗 =================
print("\n开始进行数据清洗...")
try:
    df = pd.read_csv(RAW_SMALL_PATH)
    
    # 重命名列（如果你下载的原始数据没有表头，就需要这行；如果有表头，这行会报错，注意看情况）
    df.columns = ["user_id", "item_id", "category_id", "behavior", "timestamp"]

    # 时间戳转日期时间
    df["time"] = pd.to_datetime(df["timestamp"], unit="s")
    
    # 提取小时
    df["hour"] = df["time"].dt.hour
    
    # 过滤异常时间（保留 2017-11-25 到 2017-12-03 的数据）
    start_time = pd.to_datetime("2017-11-25")
    end_time = pd.to_datetime("2017-12-03")
    df = df[(df["time"] >= start_time) & (df["time"] < end_time)]
    
    # 查看清洗后结果
    print("\n清理完成，查看前五行数据: ")
    print(df.head())
    
    print("\n各类行为统计: ")
    print(df["behavior"].value_counts())
    
    # 保存清洗好的数据
    df.to_csv(CLEAN_DATA_PATH, index=False, encoding="utf-8")
    print(f"\n清洗完毕，文件已保存至: {CLEAN_DATA_PATH}")

except Exception as e:
    print(f"清洗过程中发生错误: {e}")
