# ble_scan_connect.py:
from bluepy.btle import *
from bluepy.btle import *
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n = 0
addr = []
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print (" %s = %s" % (desc, value))

number = input('Enter your device number: ')
print ('Device', number)
num = int(number)
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num], 'random')
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#



try:
    service_uuid = 0xfff0
    SERVICE_UUID = UUID(service_uuid)

    print("service uuid = 0x%x"%service_uuid)


    testService = dev.getServiceByUUID(SERVICE_UUID)


    for descriptor in dev.getDescriptors(testService.hndStart,testService.hndEnd):
        if (descriptor.uuid==0x2902):
            print("Before write:",descriptor.read())
            h = descriptor.handle
            print("h =",h)
            dev.writeCharacteristic(h,b'\x02\x00')
            print("After write:",descriptor.read())
            print("readCharacteristic =",dev.readCharacteristic(descriptor.handle))


    
finally:
    dev.disconnect()


'''
des = dev.getDescriptors(uuid = UUID(0x2902))[0]
if (des.supportsRead()):
    print(des.read())
des.write(0x0002)
'''