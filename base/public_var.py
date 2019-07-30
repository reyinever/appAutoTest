import os
# 项目的路径
pro_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(pro_path)
# 数据文件目录
data_path=os.path.join(pro_path,"data")
# print(data_path)

#截图目录
screenshot_path=os.path.join(pro_path,"screenshot")