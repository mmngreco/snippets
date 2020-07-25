Some commands

```bash
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo lsmod | grep -i blue  # check driver used ?
sudo lspci | grep -i blue

sudo hciconfig
sudo hciconfig hci0 up  # try to enable
sudo hcitool dev  # check devices
sudo rmmod btusb
sudo modprobe btusb

sudo dmesg | grep -i blue
sudo rfkill list

bluetoothctl
# enter on [bluetooth]# prompt
power on
scan on
quit
```

I've enabled generic bluetooth drivers:

```
sudo rmmod btusb
sudo modprobe btusb
lsmod
```

Some Libraries

```
sudo apt install bluedevil
sudo apt install bluez
sudo apt install bluez-utils-compat
sudo apt install blueman
blueman-manager
sudo apt insatll rtbth-dkms
```

Ref: https://superuser.com/questions/1310775/bluetooth-adapter-not-detected-on-linux

```bash
sudo apt install --reinstall -y \
    bluetooth \
    bluez \
    bluez-firmware \
    bluez-hcidump \
    bluez-cups \
    bluez-tools \
    pulseaudio-module-bluetooth
sudo apt-get --purge --reinstall install pulseaudio
# check you don't have: autospawn = now
sudo vim /etc/pulse/client.conf
sudo pactl unload-module module-bluetooth-discover
sudo pactl load-module module-bluetooth-discover
sudo service bluetooth force-reload
sudo service bluetooth restart
```
