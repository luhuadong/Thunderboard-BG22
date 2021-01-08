# Thunderboard-BG22
Funpack 第四期「EFR32BG22 Thunderboard 蓝牙开发板」说明文档



## 自我介绍

大家好，我是 卢华东 Rudy，业余时间喜欢折腾一些开源软件和硬件，正在努力成为一名真正创客，利用开源和科技的力量做出能促进社会进步的产品。



## 实现功能

本期任务：

- 通过蓝牙读取开发板上的温度传感器数值；
- 当温度超过一定门槛后，再通过蓝牙控制开发板上的 LED 灯点亮以作报警。



针对这次活动和实现的功能，我一共整理了五篇文章：

1. [Thunderboard BG22 蓝牙开发板](https://luhuadong.blog.csdn.net/article/details/112304058)
2. [蓝牙技术 Q&A](https://luhuadong.blog.csdn.net/article/details/112306398)
3. [低功耗蓝牙 BLE 协议架构](https://luhuadong.blog.csdn.net/article/details/112306742)
4. [BlueZ gatttool 操作 Thunderboard 蓝牙开发板](https://luhuadong.blog.csdn.net/article/details/112307074)
5. [使用 pygatt 读取 Thunderboard 温度数值并控制 LED](https://luhuadong.blog.csdn.net/article/details/112307393)

视频和代码链接如下：

- 视频介绍：<https://www.bilibili.com/video/BV1Wf4y1y72k/> 
- 代码仓库：<https://github.com/luhuadong/Thunderboard-BG22>

Thunderboard 的代码位于 demo/soc_thunderboard_brd4184a；应用程序的代码位于 code/pygatt_test.py，一共 27 行代码。

```python
import time
import pygatt

adapter = pygatt.GATTToolBackend()
counter = 30
threshold = 25

try:
    adapter.start()
    device = adapter.connect('60:A4:23:C9:69:9C')

    while counter > 0:
        value = device.char_read("00002a6e-0000-1000-8000-00805f9b34fb")
        temp = (value[1] * 256 + value[0]) / 100
        print("[{:0>2d}] temp: {:.2f} 'C".format(counter, temp))

        if temp > threshold:
            device.char_write_handle(0x0022, bytearray([0x01]))  # LED on
        else:
            device.char_write_handle(0x0022, bytearray([0x00]))  # LED off

        time.sleep(1)
        counter -= 1

finally:
    print("end")
    adapter.stop()
```



## 心得体会

Funpack 第四期活动带来了精致小巧、功能齐全的 Thunderboard BG22 蓝牙开发板。本期任务不多，对于初次接触蓝牙开发的小伙伴来说，难点不在于写多少代码，而在于如何理解蓝牙协议栈及其工作方式。

我在本次实验中，Thunderboard BG22 的固件直接使用 Simplicity Studio 5 的 demo，不需要写一行代码，同时图形化的配置也能让用户更直观地理解蓝牙模型和配置 GATT 服务。应用程序部分，我是直接通过 gatttool 和 pygatt 来完成的，虽然只是很简单的命令行程序，但能帮助我们理解蓝牙模型。

总的来说，通过这次学习，我对 BLE 蓝牙协议栈有了一个大致的了解，也体验到好的开发工具（比如 Simplicity Studio 5）对开发效率的提升。物联网有很大的未来，蓝牙是不可或缺的一种连接方式，还需要不断学习才能掌握蓝牙技术。

最后，再次感谢得捷电子和硬禾学堂，感谢 Funpack 第四期的各位小伙伴！



​                                                                                                                        2021年01月08日





## 资料

- <https://www.silabs.com/wireless/gecko-series-2/efr32bg22>
- <https://www.eetree.cn/doc/detail/2119>