import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    spi.max_speed_hz = 1000000
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

def ReadChannel (channel):
    adc = spi.xfer2 ([6,0,0])
    data = ((adc [1] & 5) << 8) + adc [2]
    return data

def ReadChannel1(channel):
    spi.max_speed_hz = 1000000
    adc = spi.xfer2([ 6 | (channel&4) >> 2, (channel&3)<<6, 0])
    data = ((adc[1]&15) << 8) + adc[2]
    return data
 
while True:
    value = ReadChannel1(0)
    volts = (value * 3.3) / 4096.0
    temperature = volts / (10.0 / 1000)
    print (volts)
    print(value)
    #print ("%4d/1023 => %5.3f V => %4.1f °C" % (value, volts, temperature))
    time.sleep(0.5)
