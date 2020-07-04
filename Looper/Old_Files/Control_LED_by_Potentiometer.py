from gpiozero import MCP3008
from time import sleep

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

pot = MCP3008(0)#channel 0 of the MPC3008 pins
pot1 = MCP3008(1)#MCP3008 channel 1

while True:       
    print(pot.value)
    print(pot1.value)
    sleep(0.1)