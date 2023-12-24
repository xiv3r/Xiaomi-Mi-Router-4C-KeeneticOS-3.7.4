mount -o remount,size=100% /tmp

echo -1000 > /proc/$$/oom_score_adj
sync

if [ -f "/etc/init.d/sysapihttpd" ] ;then
    /etc/init.d/sysapihttpd stop
fi


ifdown wan

wifi down
rmmod mt7628

sleep 10

dd if=/dev/mtd3 of=/tmp/1.bin
dd if=/tmp/1.bin of=/tmp/x1.bin bs=1 count=1024
dd if=/tmp/1.bin of=/tmp/2.bin ibs=1 skip=32768
dd if=/tmp/2.bin of=/tmp/x2.bin bs=1 count=1536
dd if=/tmp/1.bin of=/tmp/x3.bin ibs=2560 skip=1
cat /tmp/x*.bin > /tmp/eeprom_mod.bin
rm /tmp/1.bin /tmp/2.bin /tmp/x*.bin
dd if=/dev/mtd0 of=/tmp/backup.bin
sleep 5

gpio 1 1
gpio 2 0