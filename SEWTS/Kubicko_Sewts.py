import pyads
import time

AMSNETID = "192.168.0.237.1.1"

plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
plc.open()
print(f"Connected?: {plc.is_open}")  # debugging statement, optional
print(f"Local Address? : {plc.get_local_address()}")  # debugging statement, optional

# intern variables
internal_data_1 = 123
internal_data_2 = 321

def read_and_compare_data():
    data_1 = plc.read_by_name("gvl.data_1")
    data_2 = plc.read_by_name("gvl.data_2")

    if data_1 != internal_data_1:
        plc.write_by_name("gvl.data_1", internal_data_1)
    if data_2 != internal_data_2:
        plc.write_by_name("gvl.data_2", internal_data_2)

try:
    while True:
        read_and_compare_data()  # call read funkcion
        time.sleep(0.1)  # wait 100ms

        time.sleep(0.4)  # after 400ms write gvl.bit_0 to true
        plc.write_by_name("gvl.bit_0", True)

except KeyboardInterrupt:
    pass

finally:
    plc.close()
