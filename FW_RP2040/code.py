import board
import busio
import adafruit_mcp4725


# I2C settings 
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

uart = busio.UART(tx=board.GP4, rx=board.GP5)

# DAC MCP4726A1 adress=0x61
dac_voltage = adafruit_mcp4725.MCP4725(i2c, address=0x61)
# DAC MCP4726A3 adress=0x63
dac_current = adafruit_mcp4725.MCP4725(i2c, address=0x63)

# current DAC parameter for Statron remote control
alpha = 1714
# voltage DAC paramater for Statron remote control
beta = 1546


# Statron voltage remote control
def set_voltage(voltage):
    try:
        if voltage < 30:
            dac_voltage.value = round(voltage * alpha)
        else:
            dac_voltage.value = 0
    except:
        dac_voltage.value = 0

# Statron current remote control
def set_current(current):
    try:
        if current < 30:
            dac_current.value = round(current * beta)
        else:
            dac_current.value = 0
    except:
        dac_current.value = 0

while True:
        data = uart.read(32)

        if data is not None:
        # convert bytearray to string
            data_string = data.decode('UTF-8')
            uart.write(bytes(data, 'UFT-8'))    
            
            
            if data_string == 'set:volt':
                
                set_voltage(20)

