import time
import pygatt

adapter = pygatt.GATTToolBackend()
counter = 10
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

