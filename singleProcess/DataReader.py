# coding=utf-8

def readData(filename):
    """读取文件数据到内存"""
    lines = fileGen(filename)
    dataSet = []
    for line in lines:
        line_data = [0] * 134
        line_data[0] = int(line[0])
        index_value_list = line[1:].strip().split()
        for block in index_value_list:
            kv = block.strip().split(":")
            key = int(kv[0])
            value = float(kv[1])
            if (key > 133):
                continue
            else:
                line_data[key] = value
        dataSet.append(line_data)
    return dataSet

def fileGen(filename):
    """使用生成器读取文件"""
    file = open(filename, 'r')
    for line in file:
        yield line
    file.close()


if __name__ == '__main__':
    dataSet = readData("train_data_min.txt")
    print(len(dataSet))
    print(str(dataSet))