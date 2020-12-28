# Thunderboard-BG22
Funpack 第四期 EFR32BG22 Thunderboard 蓝牙开发板



Thunderboard BG22 开发套件是 Silicon Labs 提供的一个小型原型平台，适用于电池供电的蓝牙应用。上面搭载的 EFR32BG22 蓝牙低功耗 5.2 SoC 可提供低功耗蓝牙、网状网络和误差一米以内的测向精度。



本期任务

- 通过蓝牙读取开发板上的温度传感器数值；
- 当温度超过一定门槛后，再通过蓝牙控制开发板上的 LED 灯点亮以作报警。



![](./images/Thunderboard_EFR32BG22_Hardware_Layout.png)

**开发套件特性**

- Thunderboard 标准尺寸大小 4.5x3cm
- EFR32BG22 无线 Gecko SoC
  - 支持蓝牙 5.2，支持测向和 LE 编码 PHY
  - ARM Cortex-M33 内核，76.8MHz 的工作频率，512kB 闪存和 32kB RAM
  - 板载 38.4MHz 晶体
  - 板载 32.768 晶体
  - 2.4GHz 匹配网络和贴片天线

- 板载调试
  - 板载 Jlink 调试器，一路虚拟串口
  - USB Micro 连接器
  - Mini Simplicity 调试连接插座

- 板载可控的电源控制电路，实现传感器的超低功耗
- 一路用户按键和 LED
- 传感器
  - 相对湿度和温度传感器 Si7021
  - UV 和环境光传感器 Si1133
  - 霍尔效应传感器 Si7210
  - 6 轴惯性传感器 Invensense ICM-20648
- 8Mbit SPI Flash
- 20pin 2.54mm 通孔接口，用于 GPIO 访问和与外部硬件的连接
- 数据包跟踪接口 (PTI)
- USB 或纽扣电池供电
- 开源 Andriod 和 IOS demo 应用程序
- 软件开发平台 Simplicity Studio

