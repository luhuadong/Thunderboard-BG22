# 5. BluePy



[bluepy](https://github.com/IanHarvey/bluepy) 是一个开源项目，提供了 Python API 接口对低功耗蓝牙设备进行访问。目前只支持 Linux 系统（包括树莓派）。

## 安装

bluepy 支持 Python 2.7 和 Python 3.x

To install the current released version, on most Debian-based systems:

```
$ sudo apt-get install python-pip libglib2.0-dev
$ sudo pip install bluepy
```

On Fedora do:

```
$ sudo dnf install python-pip glib2-devel
```

For Python 3, you may need to use `pip3`:

```
$ sudo apt-get install python3-pip libglib2.0-dev
$ sudo pip3 install bluepy
```

*If this fails* you should install from source.

```
$ sudo apt-get install git build-essential libglib2.0-dev
$ git clone https://github.com/IanHarvey/bluepy.git
$ cd bluepy
$ python setup.py build
$ sudo python setup.py install
```

I would recommend having command-line tools from BlueZ available for debugging. There are instructions for building BlueZ on the Raspberry Pi at http://www.elinux.org/RPi_Bluetooth_LE.


