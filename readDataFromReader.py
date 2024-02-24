from PN5180 import PN5180

reader = PN5180(debug=True)
reader._send([0x04, 0x13])  # READ_REGISTER RX_STATUS
result = reader._read(4)  # Read 4 bytes
print(result)