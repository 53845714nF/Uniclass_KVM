#!/usr/bin/python
"""
This Module switch on UDP-TA2-4K KVM Switch.
"""

from usb.core import find
from usb.util import get_string


def main():
    """
    The Main Function that switch the input of the UDP-TA2-4K KVM.
    """
    payload_1_2 = bytearray([1, 1, 0, 0, 0, 0, 0, 0])
    payload_2_1 = bytearray([1, 0, 0, 0, 0, 0, 0, 0])

    dev = find(idVendor=0x10d5, idProduct=0x55a2)

    if dev is None:
        raise ValueError('KVM-Switch not connected!')
    else:
        print('KVM-Switch found.')

    serial_number = get_string(dev, dev.iSerialNumber)

    if (serial_number.encode('utf-8')) == b'02\xc2\x92':
        try:
            dev.write(2, payload_1_2.decode('utf-8'))
        except:
            pass
        print("switched from 1 to 2")

    if (serial_number.encode('utf-8')) == b'12\xc2\xb2':
        dev.write(2, payload_2_1.decode('utf-8'))
        print("switched from 2 to 1")


if __name__ == "__main__":
    main()
