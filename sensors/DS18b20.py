import os

def get_temperature_from_ds18b20(device_file='/sys/bus/w1/devices/28-012029d48de2/w1_slave')->float:
    assert os.path.exists(device_file)
    tfile = open(device_file)
    text = tfile.read()
    #关闭文件
    tfile.close()
    #用换行符分割字符串成数组，并取第二行
    secondline = text.split("\n")[1]
    #用空格分割字符串成数组，并取最后一个，即t=23000
    temperaturedata = secondline.split(" ")[9]
    #取t=后面的数值，并转换为浮点型
    temperature = float(temperaturedata[2:])
    #转换单位为摄氏度
    temperature = temperature / 1000
    return temperature


if __name__ == '__main__':
    temp = get_temperature_from_ds18b20()
    print('temperature:{} *C'.format(temp))

