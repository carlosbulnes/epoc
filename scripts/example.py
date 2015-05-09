# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 

from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

if __name__ == "__main__":
    headset = Emotiv()
    gevent.spawn(headset.setup)
    gevent.sleep(0)
    data = []
    try:
        while True:
            packet = headset.dequeue()
            #print packet.gyro_x, packet.gyro_y
            data.append(packet.sensors['F3']['value'])
            data.append(packet.sensors['FC5']['value'])
            data.append(packet.sensors['AF3']['value'])
            data.append(packet.sensors['F7']['value'])
            data.append(packet.sensors['T7']['value'])
            data.append(packet.sensors['P7']['value'])
            data.append(packet.sensors['O1']['value'])
            data.append(packet.sensors['O2']['value'])
            data.append(packet.sensors['P8']['value'])
            data.append(packet.sensors['T8']['value'])
            data.append(packet.sensors['F8']['value'])
            data.append(packet.sensors['AF4']['value'])
            data.append(packet.sensors['FC6']['value'])
            data.append(packet.sensors['F4']['value'])
            print data
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()