# 4. BlueZ

> 测试：THUNDERBOARD #27036 `60:A4:23:C9:69:9C`



## bluetoothctl

**使用bluetoothctl连接到蓝牙设备**

启动 bluetoothctl 交互式命令

```shell
bluetoothctl show
```

打开蓝牙适配器

```shell
agent KeyboardOnly
default-agent
power on
```

扫描

```shell
scan on
```



```shell
[Thunderboard #27036]# info
Device 60:A4:23:C9:69:9C
	Name: Thunderboard #00000
	Alias: Thunderboard #00000
	Paired: no
	Trusted: no
	Blocked: no
	Connected: yes
	LegacyPairing: no
	UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
	UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
	UUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)
	UUID: Battery Service           (0000180f-0000-1000-8000-00805f9b34fb)
	UUID: Automation IO             (00001815-0000-1000-8000-00805f9b34fb)
	UUID: Environmental Sensing     (0000181a-0000-1000-8000-00805f9b34fb)
	UUID: Vendor specific           (1d14d6ee-fd63-4fa1-bfa4-8f47b42119f0)
	UUID: Vendor specific           (a4e649f4-4be5-11e5-885d-feff819cdc9f)
	UUID: Vendor specific           (ec61a454-ed00-a5e8-b8f9-de9ec026ec51)
	UUID: Vendor specific           (f598dbc5-2f00-4ec5-9936-b3d1aa4f957f)
	RSSI: -56

```



## hciconfig

使用 `hciconfig` 命令可以查看当前能够识别的蓝牙设备，该命令类似 `ifconfig` 查看网卡设备。可以控制蓝牙设备的开启与关闭，在默认情况下，蓝牙设备在插入 host 时是不会自动开启的，所以我们在调试之前要先开启设备。

```shell
$ hciconfig 
hci0:	Type: BR/EDR  Bus: USB
	BD Address: 74:E5:F9:FF:B0:CB  ACL MTU: 1021:4  SCO MTU: 96:6
	UP RUNNING PSCAN ISCAN 
	RX bytes:56591727 acl:245 sco:0 events:8083009 errors:0
	TX bytes:700294981 acl:8080058 sco:0 commands:2632 errors:0
```

会输出以上内容，我们可以看到蓝牙设备的编号为 `hci0`，这是 host 分配给设备的 ID，我们用来启动或关闭设备也是需要该 ID 来控制。

开启与关闭设备：

```shell
#设备打开
sudo hciconfig hci0 up
#设备关闭
sudo hciconfig hci0 down
```



## hcitool

在打开蓝牙设备以后，就可以使用 hcitool 工具集对蓝牙进行控制，工具集参数分为两部分，一为正常的蓝牙设备调试，二为低功耗即 BLE 设备， 工具参数如下：



搜索 BLE 设备：

```shell
$ sudo hcitool lescan
LE Scan ...
6B:FB:CD:E4:6E:FB (unknown)
6B:FB:CD:E4:6E:FB (unknown)
60:A4:23:C9:69:9C Thunderboard #27036
60:A4:23:C9:69:9C (unknown)
50:76:0F:FA:95:10 (unknown)
50:76:0F:FA:95:10 (unknown)
F8:31:68:A0:8C:06 SMI-M1
F8:31:68:A0:8C:06 (unknown)
```





## gattool

使用 interactive 方式连接设备：

```shell
gatttool -b 60:A4:23:C9:69:9C -I
```

查看帮助：

```shell
[60:A4:23:C9:69:9C][LE]> help
help                                           Show this help
exit                                           Exit interactive mode
quit                                           Exit interactive mode
connect         [address [address type]]       Connect to a remote device
disconnect                                     Disconnect from a remote device
primary         [UUID]                         Primary Service Discovery
included        [start hnd [end hnd]]          Find Included Services
characteristics [start hnd [end hnd [UUID]]]   Characteristics Discovery
char-desc       [start hnd] [end hnd]          Characteristics Descriptor Discovery
char-read-hnd   <handle>                       Characteristics Value/Descriptor Read by handle
char-read-uuid  <UUID> [start hnd] [end hnd]   Characteristics Value/Descriptor Read by UUID
char-write-req  <handle> <new value>           Characteristic Value Write (Write Request)
char-write-cmd  <handle> <new value>           Characteristic Value Write (No response)
sec-level       [low | medium | high]          Set security level. Default: low
mtu             <value>                        Exchange MTU for GATT/ATT
```

连接：

```shell
[60:A4:23:C9:69:9C][LE]> connect
Attempting to connect to 60:A4:23:C9:69:9C
Connection successful
```

查看设备提供的服务：

```shell
[60:A4:23:C9:69:9C][LE]> primary
attr handle: 0x0001, end grp handle: 0x0008 uuid: 00001801-0000-1000-8000-00805f9b34fb
attr handle: 0x0009, end grp handle: 0x000d uuid: 00001800-0000-1000-8000-00805f9b34fb
attr handle: 0x000e, end grp handle: 0x001a uuid: 0000180a-0000-1000-8000-00805f9b34fb
attr handle: 0x001b, end grp handle: 0x0024 uuid: 00001815-0000-1000-8000-00805f9b34fb
attr handle: 0x0025, end grp handle: 0x0028 uuid: 0000180f-0000-1000-8000-00805f9b34fb
attr handle: 0x0029, end grp handle: 0x002b uuid: ec61a454-ed00-a5e8-b8f9-de9ec026ec51
attr handle: 0x002c, end grp handle: 0x0034 uuid: f598dbc5-2f00-4ec5-9936-b3d1aa4f957f
attr handle: 0x0035, end grp handle: 0x003e uuid: a4e649f4-4be5-11e5-885d-feff819cdc9f
attr handle: 0x003f, end grp handle: 0x0047 uuid: 0000181a-0000-1000-8000-00805f9b34fb
attr handle: 0x0048, end grp handle: 0xffff uuid: 1d14d6ee-fd63-4fa1-bfa4-8f47b42119f0
```

