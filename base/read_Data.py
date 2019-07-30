import yaml,os
from base.public_var import data_path


def read_data(file_name):
    """
    :param file_name: data目录下的文件名，只写文件即可
    :return:
    """
    try:
        file_path=os.path.join(data_path,file_name)
        # print(file_path)
        with open(file_path,'r',encoding='utf-8')as f:
            return yaml.load(f)
    except Exception as e:
        print("读数据异常：",e)


if __name__ == '__main__':
    print(read_data("phone_login.yaml"))