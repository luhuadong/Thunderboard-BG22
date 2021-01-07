# Append. Notes



Hello，大家好，我是 Rudy。欢迎来到得捷电子和硬禾学堂联合推出的 Funpack 第四期。本期的主角是来自 Silicon Labs 的 ThunderBoard。



## 硬件平台

![](./images/Thunderboard_EFR32BG22_Hardware_Layout.png)

Thunderboard BG22 是一款来自 Silicon Labs（也就是芯科科技）的蓝牙开发套件。核心 SoC EFR32BG22 是其推出的第二代蓝牙芯片，相对于之前的系列 BG22 的功耗更低，非常适用于电池供电且需要定位功能的极低功耗的物联网应用场景。

Thunderboard BG22 虽然体积小、成本低，但功能齐全。搭载了丰富且实用的传感器，包括温湿度传感器、UV 指数和环境光传感器、霍尔效应传感器、6轴惯性传感器，此外，还有两个带有 PDM 输出的数字麦克风，以及一个通过 Micro USB 接口就可以连接使用的内置调试器。

针对物联网开发人员面临的诸多挑战，Silicon Labs 为开发者提供了 Simplicity Studio 5 集成开发环境，帮助用户针对性能、功耗、尺寸、多协议共存和安全性等方面进行优化，同时组件化、图形化的配置方式，也帮助用户提高代码复用，缩短开发周期。

低功耗蓝牙的应用，除了常见的蓝牙耳机、音箱、鼠标、键盘等设备，还将在运动健身设备、便携式医疗设备、智能家居、楼宇自动化、工业自动化等领域发挥重要作用。



在运动和健身的数据追踪方面发挥着重要作用，在追踪蓝牙资产标签和信标位置方面发挥关键作用。

- 资产标签和信标
- 消费电子遥控器
- 便携式医疗设备
- 蓝牙网状网络低功耗节点
- 运动、健身和保健设备
- 互联家居
- 楼宇自动化和安全

> Silicon Labs（芯科科技）是一家致力于建立更智能、更互联世界的领先芯片、软件和解决方案供应商。



## 开发环境

Simplicity Studio

最近发布的 Simplicity Studio 5 是其集成开发环境（IDE）的一次重大升级。新版 Simplicity Studio 可以通过具有 Web 风格的集中式用户界面为各种无线协议提供一致的访问和开发体验。



## 设计思路

本期的任务是：

- 通过蓝牙读取开发板上的温度传感器数据；
- 当温度超过一定门槛后，再通过蓝牙控制开发板上的 LED 灯点亮以作报警。

在实现该功能之前，我们先来快速了解一下蓝牙协议栈。简单来说，BLE 蓝牙协议栈主要分为 PHY层，也就是物理层，它的作用是控制无线电的频段、调制和解调方式等等。在此之上是 LL 链路层、HCI 接口层，这一部分也被称为 Controller。

再往上是 GAP层、L2CAP 逻辑链路控制和适配协议、SMP 安全管理协议、ATT 属性协议 以及 GATT 通用属性协议层。这一部分也称为 Host 层，是蓝牙协议栈的关键部分。

再往上就是各种 Profile 应用了。对于 Thunderboard 这种单芯片方案来说，实际上 Controller、Host 和 Profiles 都是在 BG22 这片 SoC 上实现的。对于蓝牙应用开发者来说，通常只需要关注 GATT 层和各种 Profile 即可。

Profile 里面会包含一些 Service，比如电池服务、传感器数据服务等等。

我们可以把各种 Profile 比喻为不同的柜子，不同的柜子有不同的功能，存放不同的东西，柜子里面也可以包含其他柜子，也就是 Include，柜子里面存放的物品就是 Characteristic 也就是特征值，不同的物品自然会有不同的属性和内容，这就是它对应的 properties 和 value。

我们在 Simplicity Studio 中打开 Thunderboard 的工程，看到默认配置好的一些 Service。对于本次任务，我们只需要关注 Automation IO 和 Environment Sensing 服务即可。

打开对应的配置，我们就可以看到 LED 和 温度传感器 对应的 UUID 和 属性。了解了这些，我们就可以开始做实验啦。



## 实验介绍

我们登录到一台支持蓝牙功能的 Linux 系统，并预先安装了 BlueZ 蓝牙协议栈。

现在，我们来检查一下系统上的蓝牙设备

```shell
hciconfig
```

搜索附近的 BLE 设备

```shell
sudo hcitool lescan
```

可以看到 Thunderboard #27036 开发板对应的地址是 60:A4:23:C9:69:9C

接下来使用 gatttool 进入交互模式：

```shell
gatttool -b 60:A4:23:C9:69:9C -I
```

连接设备

```
connect
```

查看设备提供的服务

```
primary
```

查看设备提供的特征

```
characteristics
```

可以看到所有特性的句柄和属性值，以及该特征  value 对应的句柄 和 uuid ；根据属性和 uuid，我们就不难发现 LED 和 温度传感器所对应的特征值了。

接下来我们可以通过 uuid 或 handle 来找到对应的特征值并进行读写操作了。

比如打开 LED 灯

```shell
char-write-req 0x0022 01
```

关闭 LED 灯

```shell
char-write-req 0x0022 00
```

读取当前温度

```shell
char-read-hnd 0x0045
```

到这里，其实我们已经实现了蓝牙的读写操作了。

为了完成本次任务，我基于 pygatt 写了一段代码，整体流程是这样的：

首先 Thunderboard 启动后进行广播，然后应用程序搜索到该设备并进行连接，接着通过 uuid 找到温度传感器对应的特征值，读取数据并进行转换，再和预设的温度阈值进行比较，如果温度高于 25 摄氏度，则修改 LED 的特征值，点亮 LED 灯；否则关闭 LED 灯。

```sequence
ThunderBoard->ThunderBoard: 初始化
Application->ThunderBoard: 蓝牙连接
ThunderBoard->Application: 传感器数据
Application->ThunderBoard: 控制LED
```





## 效果演示





## 参考资料

- [Silicon Labs以Simplicity Studio 5簡化IoT開發](https://www.silabs.com/community/chinese-blog.entry.html/2020/09/11/silicon_labs_simplicitystudio5iot-OOQk)
- [Silicon Labs以Simplicity Studio 5简化物联网开发](https://www.21ic.com/article/871760.html)