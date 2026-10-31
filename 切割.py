input_file = r"UserBehavior.csv"
output_file = r"small_UserBehavior.csv"
max_rows=100000
count = 0
with open(input_file, encoding="utf-8") as fr, open(output_file, "w",encoding="utf-8") as fw:
     for line in fr:
         fw.write(line)
         count = count + 1
         if count >= max_rows:
             break
print("切割完成，已提取前{max_rows}行，保存为small_UserBehavior.csv")