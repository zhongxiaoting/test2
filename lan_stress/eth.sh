#!/bin/bash
ld="Link detected: yes"
lb=`ethtool enp24s0f0 |grep "Link detected:"`
such="Speed: 10000Mb/s"
as="Speed: 25000Mb/s"
for i in `ls /sys/class/net`
do
link=$(ethtool $i |grep "Link detected:")
link=$(echo $link)

if [[ "$link" = "$ld" ]];then
echo "good"
mac=$(ifconfig $i |grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
echo $mac
   speed=$(ethtool $i |grep "Speed: ")
   speed=$(echo $speed)
        if [ "$speed" = "$such" -o "$speed" = "$as" ];then
           echo "start to check Lan in this time"
           chmod +x /home/test2/lan_stress/pktgentest.sh
           /home/test2/lan_stress/pktgentest.sh -i $i -m $mac -s 1500 &>/home/test2/stress_log/lan_stress.log
           sleep 2
         else
         echo "nothing to do"
         fi
else
echo "need link!"
fi
done


