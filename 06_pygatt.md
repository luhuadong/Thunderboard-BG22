# 6. pygatt

[pygatt](https://github.com/peplin/pygatt) 是一个用于读写蓝牙设备的 GATT 描述符的 Python 模块，可用于任何符合标准 GATT 描述符行为的设备，例如健身追踪器、传感器等等。

pygatt 支持两种不同后端并提供了 Pythonic API：

- BlueZ (requires Linux), using the `gatttool` command-line utility.
- Bluegiga's BGAPI, compatible with USB adapters like the BLED112.

我们在 Linux 上进行测试，因此选择使用 gatttool 后端即可。

## 安装

```shell
$ pip install pygatt
```



## API

```python
Help on method char_write_handle in module pygatt.backends.gatttool.device:

char_write_handle(handle, *args, **kwargs) method of pygatt.backends.gatttool.device.GATTToolBLEDevice instance
    Writes a value to a given characteristic handle. This can be used to
    write to the characteristic config handle for a primary characteristic.
    
    hande -- the handle to write to.
    value -- a bytearray to write to the characteristic.
    wait_for_response -- wait for response after writing.
    
    Example:
        my_ble_device.char_write_handle(42, bytearray([0x00, 0xFF]))
```



```python
Help on method char_read_handle in module pygatt.backends.gatttool.device:

char_read_handle(handle, *args, **kwargs) method of pygatt.backends.gatttool.device.GATTToolBLEDevice instance
    Reads a Characteristic by handle.
    
    handle -- handle of Characteristic to read.
    
    Returns a bytearray containing the characteristic value on success.
    
    Example:
        my_ble_device.char_read_handle(5)
```





