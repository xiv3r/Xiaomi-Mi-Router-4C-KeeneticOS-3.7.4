echo 432545


gpio 3 1
gpio 2 0

mount -o remount,size=100% /tmp

echo -1000 > /proc/$$/oom_score_adj
sync

if [ -f "/etc/init.d/sysapihttpd" ] ;then
    /etc/init.d/sysapihttpd stop
fi

wifi down
rmmod mt7628
rmmod mt7613

ifdown wan
sleep 3