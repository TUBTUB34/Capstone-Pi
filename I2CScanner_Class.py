import smbus2

class I2CScanner:
    def __init__(self, bus_number=1):
        self.bus = smbus2.SMBus(bus_number)

    def scan(self):
        devices = []
        for address in range(0x03, 0x78):  # I2C addresses range from 0x03 to 0x77
            try:
                self.bus.write_byte(address, 0)
                devices.append(hex(address))
            except OSError:
                pass
        #devices = ['0x8', '0x9', '0xa']:
            
        if not devices:
            return None
        return devices

    def close(self):
        self.bus.close()
        
    def GetData(self, address, what):
        if (what == 'voltage'):
            message = 'V'
        elif (what == 'current'):
            message = 'C'
        elif (what == 'power'):
            message = 'P'
        data = message.encode('utf-8')
        self.bus.write_i2c_block_data(address, 0, list(data))
        return self.bus.read_byte(address)
