## 安装方式：

下载PythonSmallModule文件夹下的PythonSmallModule-1.0.tar，cd到存放此文件的路径,
pip install PythonSmallModule-1.0.tar

## 说明：

**encryption开头的函数，全部为加密函数**：
包括 ：url编码， base64， MD5

decryption开头的函数，全部为解密函数：
包括 url编码， base64

**decoding开头的函数，全部为字符串解码函数**：
包括： NCR字符串解码，unicode字符串解码


**date开头的函数，全部为时间相关函数**：
包括：
1. 获取指定日期前n天的日期
2. 获取指定日期前n天所有日期列表
3. 获取指定月份总共有多少天
4. 获取指定日期上一周的开始日期和结束日期
5. 获取指定日期上一月的开始日期和结束日期
6. 获取两个日期之间的所有日期,包含开始日期和结束日期

**change开头的函数，全部为转换相关函数**：
包括：
1. datetime类型的日期转换成str类型的日期
2. datetime类型的日期转换成int类型的时间戳 （时间戳精确到秒，即10位数的）
3. str类型的日期转换成datetime类型的日期
4. str类型的日期转换成int类型的时间戳 （时间戳精确到秒，即10位数的）
5. float类型或int类型的时间戳转化成datetime类型的日期
6. float类型或int类型的时间戳转化成str类型的日期








## 自定义代码打包方式，供别人pip安装

：
pycharm里右键 -- new -- Python Packpage，我起名为PythonSmallModule，
然后在新生成的PythonSmallModule文件夹里，新建python-small-module.py文件，里边写入自己的代码。
在PythonSmallModule文件夹同级目录下，新建setup.py文件，内容参照里边去写。
然后，在此处打开命令行
输入 python setup.py build
输入 python setup.py sdist
最后会生成如下图示
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191112175522178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2wxMTU5MDE1ODM4,size_16,color_FFFFFF,t_70)
最后
pip install PythonSmallModule-1.0.tar.gz 
