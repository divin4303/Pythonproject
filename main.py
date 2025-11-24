import time

import mysql.connector
import TON
import TOF
import TP

db = mysql.connector.connect(host="172.20.45.150",
                             user="root",
                             password="Oct@2019")

ton = TON.TON(PT=2.0)  # 2-second TON timer
tof = TOF.TOF(PT=3.0)
tp  = TP.TP(PT=1.0)

while True:
    input_signal = read_gpio_pin()  # your function for Raspberry Pi

    print("TON:", ton.update(input_signal))
    print("TOF:", tof.update(input_signal))
    print("TP :", tp.update(input_signal))

    time.sleep(0.01)  # 10 ms scan cycle

