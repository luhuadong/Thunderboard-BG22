# 4. BlueZ



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

