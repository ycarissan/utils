# utils
## Slurm interactive job

```
srun -n NPROC --pty bash -i
```

## Screenshots

### Using import Command to Take Desktop Screenshot

```import -window root image1.png```

### Using import Command to Take Selected Area of Screen

```import calc.png```

## Widgets

```
git clone git@github.com:deficient/volume-control.git
git clone git@github.com:deficient/battery-widget.git
```

## backlight

```
git clone git@github.com:ycarissan/brightness.git
```

Allow for modification of the brightness by appropriate users (adapt to your situation) :
```
> cat /etc/tmpfiles.d/brightnessyc.conf 
f /sys/class/backlight/[DISPLAY]/brightness 0664 root users - -
```
REBOOT
Now, the ch_backlight script allows for the modification of the brightness by 1% steps.

## Screen resolution
Query screen names and supported resolutions
```
xrandr -q
```

Set the resolution of your choice:
```
xrandr -d :0 --output eDP-1 --mode 2048x1152
```

## Printer discovery

Allow for mDNS in the firewall.

## CLI Convert a document with libreoffice
```
libreoffice --headless --convert-to pdf toto.odp
```

## Update DNS
```
netconfig update -f
```

## Globalprotect
```
sudo rpm -ivh GlobalProtect_rpm
sudo ln -fTs /opt/paloaltonetworks/globalprotect/gpd.service /etc/systemd/system/gpd.service
-5.1.1.0-17.rpm
systemctl daemon-reload
systemctl enable --now gpd.service
globalprotect connect --portal vpn.univ-amu.fr
```

## Git
Store user/pwd in a git project.
```
git config credential.helper store
```

## Tap to click
From https://cravencode.com/post/essentials/enable-tap-to-click-in-i3wm/
```
sudo mkdir -p /etc/X11/xorg.conf.d && sudo tee <<'EOF' /etc/X11/xorg.conf.d/90-touchpad.conf 1> /dev/null
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

EOF
```

## Update Xresources
```
xrdb -merge ~/.Xresources
```

## Wacom
```
xsetwacom --list devices
xsetwacom set 24 mode relative
```
# Recover
From https://feeding.cloud.geek.nz/posts/recovering-from-unbootable-ubuntu-encrypted-lvm-root-partition/
```
sudo cryptsetup luksOpen /dev/nvme0n1p3 nvme0n1p3_crypt
sudo vgchange -ay
sudo mount /dev/mapper/vgubuntu-root /mnt
sudo mount /dev/nvme0n1p2 /mnt/boot
sudo mount -t proc proc /mnt/proc
sudo mount -o bind /dev /mnt/dev
sudo mount -t sysfs sysfs /mnt/sys
sudo mount --bind /etc/resolv.conf /mnt/etc/resolv.conf
sudo chroot /mnt
```
