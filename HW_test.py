import time
# 下面的函数导入是为了观察作图，后期可以去掉
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt


def compute_everyday_cputype_num(cpu_types, Times):
    '''
    将sdk数据包里面的数据保存到二维数组，每一行表示那天的各个虚拟机的种类及个数
    第一个数据位表示天数，方便后面按需提取
    '''

    vir_typenum = []  # 二维数组存放虚拟机信息

    # 五个循环前的先行变量初始化
    vir_typenum = []  # 二维数组存放虚拟机信息
    month = Times[0][0]
    i = 0
    day_count = Times[i][1]
    cpu_num = [day_count, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0]  # 每天各个虚拟机的个数,第一位表示天数

    # 循环存储的开始
    while(i < len(cpu_types)):
        if (Times[i][0] == month) and (month <= 12):
            if day_count != Times[i][1]:
                vir_typenum.append(cpu_num)
                day_count = Times[i][1]
                cpu_num = [day_count, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0]  # 每天各个虚拟机的个数
            else:
                if cpu_types[i] == "flavor1":
                    cpu_num[1] = cpu_num[1] + 1
                elif cpu_types[i] == "flavor2":
                    cpu_num[2] = cpu_num[2] + 1
                elif cpu_types[i] == "flavor3":
                    cpu_num[3] = cpu_num[3] + 1
                elif cpu_types[i] == "flavor4":
                    cpu_num[4] = cpu_num[4] + 1
                elif cpu_types[i] == "flavor5":
                    cpu_num[5] = cpu_num[5] + 1
                elif cpu_types[i] == "flavor6":
                    cpu_num[6] = cpu_num[6] + 1
                elif cpu_types[i] == "flavor7":
                    cpu_num[7] = cpu_num[7] + 1
                elif cpu_types[i] == "flavor8":
                    cpu_num[8] = cpu_num[8] + 1
                elif cpu_types[i] == "flavor9":
                    cpu_num[9] = cpu_num[9] + 1
                elif cpu_types[i] == "flavor10":
                    cpu_num[10] = cpu_num[10] + 1
                elif cpu_types[i] == "flavor11":
                    cpu_num[11] = cpu_num[11] + 1
                elif cpu_types[i] == "flavor12":
                    cpu_num[12] = cpu_num[12] + 1
                elif cpu_types[i] == "flavor13":
                    cpu_num[13] = cpu_num[13] + 1
                elif cpu_types[i] == "flavor14":
                    cpu_num[14] = cpu_num[14] + 1
                elif cpu_types[i]=="flavor15":
                    cpu_num[15] = cpu_num[15] + 1
                else:
                    pass
                i = i + 1
        else:
            month = month + 1
    return vir_typenum



def graph_analyse(type_data):
    '''
    将之前收集到的二维数组以虚拟机为单位画成折线图，观察规律
    '''

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    for type in range(1, 16):
        data = []

        for i in range(0, len(type_data)):
            data.append(type_data[i][type - 1])

        y = [i for i in range(0, len(type_data))]

        plt.figure()
        plt.plot(y, data)
        plt.title("第" + str(type) + "种虚拟机类型随时间的分布情况")
        plt.xlabel("具体的某一天")
        plt.ylabel("虚拟机的个数")
        plt.savefig(
            r"C:\Users\lyy18291855970\Desktop\预测的图像信息\Figure_" + str(type) + "png")


def gather_data_to_week(datasets):
    '''
    将数据以一个月四周来进行分割，方便预测,但是万一要预测的数据集跨度超过两个周就会遇到难题，所以不适用
    '''
    i = 0
    n = 0
    print(len(datasets))
    new_dataset = []
    weekdataset = []
    while(i < len(datasets)):
        try:
            while(True):
                if(datasets[i][0] <= 7):
                    if(n == 0):
                        #if weekdataset:#判断是否有第四个循环产生的weekdataset数据集没有加入
                          #  new_dataset.append(weekdataset)
                        weekdataset = datasets[i][1:]#当小循环里面的n为0就表示第一次循环，此时需要初始化weekdataset
                    else:
                        weekdataset = list(
                            map(lambda x: x[0] + x[1], zip(datasets[i][1:], weekdataset)))
                    n = n + 1
                    i = i + 1
                else:
                    n=0
                    new_dataset.append(weekdataset)
                    break 

            while(True):
                if(7 < datasets[i][0] <= 15):
                    if(n==0):
                        weekdataset=datasets[i][1:]
                    else:
                        weekdataset = list(
                            map(lambda x: x[0] + x[1], zip(datasets[i][1:], weekdataset)))
                    n = n + 1
                    i = i + 1
                else:
                    n=0
                    new_dataset.append(weekdataset)
                    break 
           

            while(True):
                if(15 < datasets[i][0] <= 22):
               
                    if(n == 0):
                        weekdataset = datasets[i][1:]
                    else:
                        weekdataset = list(
                            map(lambda x: x[0] + x[1], zip(datasets[i][1:], weekdataset)))
                    n = n + 1
                    i = i + 1
                else:
                    n=0
                    new_dataset.append(weekdataset)
                    break 
            

            while(True):
                if(22 < datasets[i][0] <= 31):

                    if(n == 0):
                        weekdataset = datasets[i][1:]
                    else:
                        weekdataset = list(
                            map(lambda x: x[0] + x[1], zip(datasets[i][1:], weekdataset)))
                    n = n + 1
                    i = i + 1
                else:
                    n=0
                    new_dataset.append(weekdataset)
                    break 

        except Exception:
            break

    return new_dataset


if __name__ == "__main__":

    # 初始化一些变量
    cpu_types = []  # 存放cpu类型
    times = []  # 存放时间，数据形式为“%Y-%m-%d”
    array = []  # 系统给出存放初始数组
    vir_typenum = []  # 二维数组存放虚拟机信息

    # 文件读入
    with open('all.txt', 'r') as lines:
        for line in lines:
            array.append(line)

    # 数据重组
    for i in range(0, len(array)):

        deal_array = array[i].split()
        cpu_types.append(deal_array[1])
        b = time.mktime(time.strptime(deal_array[2], "%Y-%m-%d"))
        ti = time.localtime(b)
        times.append([ti[1], ti[2]])
    vir_typenum = compute_everyday_cputype_num(cpu_types, times)
    #dataset = gather_data_to_week(vir_typenum)
    print(vir_typenum[len(vir_typenum)])





'''展示数据的老代码
    data=[]
    for i in range(0,len(dataset)):
        data.append(dataset[i][0])
    y=[i for i in range(0,len(dataset))]
    plt.figure()  
    plt.plot(y,data)
    plt.show()

'''