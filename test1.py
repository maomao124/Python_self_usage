"""
 * Project name(项目名称)：Python_self用法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:28
 * Version(版本): 1.0
 * Description(描述)：
 如果把类比作造房子的图纸，那么类实例化后的对象是真正可以住的房子。根据一张图纸（类），
 我们可以设计出成千上万的房子（类对象），每个房子长相都是类似的（都有相同的类变量和类方法），
 但它们都有各自的主人，那么如何对它们进行区分呢？
当然是通过 self 参数，它就相当于每个房子的门钥匙，可以保证每个房子的主人仅能进入自己的房子
Python 类方法中的 self 参数就相当于 C++ 中的 this 指针。
 """


class Person:
    def __init__(self):
        print("正在执行构造方法")

    # 定义一个study()实例方法
    def study(self):
        print(self, "正在学Python")


class Person1:
    name = ""

    def __init__(self, name):
        self.name = name
        print("正在执行构造方法")

    # 定义一个study()实例方法
    def study(self):
        print(self, "正在学Python")


if __name__ == '__main__':
    zhangsan = Person()
    zhangsan.study()
    lisi = Person()
    lisi.study()

    w = Person1("王五")
    print(w.name)

    w.study()
