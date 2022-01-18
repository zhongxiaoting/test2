#!/bin/bash
ld="Link detected: yes"
such="Speed: 10000Mb/s"
as="Speed: 25000Mb/s"
for i in `ls /sys/class/net`
do
  link=$(ethtool $i |grep "Link detected:")
  link=$(echo $link)

  if [[ "$link" = "$ld" ]];then
    echo "->>> $i is link"
    mac=$(ifconfig $i |grep -Eo '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
#    echo $mac
       speed=$(ethtool $i |grep "Speed: ")
       echo $speed
       speed=$(echo $speed)
            if [ "$speed" = "$such" -o "$speed" = "$as" ];then
               echo "->>> start to check Lan in this time"
               chmod +x /home/test2/lan_stress/pktgentest.sh
               timeout 24h /home/test2/lan_stress/pktgentest.sh -i $i -m $mac -s 1500 -n 0
               sleep 2
             else
                echo "->>> $i speed is not 10000Mb/s or 25000Mb/s, nothing to do"
             fi
  else
    echo "->>> $i need link!"
  fi
done


