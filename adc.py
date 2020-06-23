from mcp3208 import MCP3208
import time

adc = MCP3208()

while True:
        #for i in range(4):
                #print('ADC[{}]: {:.2f}'.format(i, adc.read(i)))
    print(adc.read(0))
    data=adc.read(0)
    volts = (data * 3.3) / float (4096)
    print(volts)

    time.sleep(0.5)
