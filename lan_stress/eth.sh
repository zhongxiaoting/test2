#!/bin/bash
ld="Link detected: yes"
such="Speed: 10000Mb/s"
as="Speed: 25000Mb/s"
for i in `ls /sys/class/net`
do
  link=$(ethtool $i |grep "Link detected:")
  link=$(echo $link)

  if [[ "$link" = "$ld" ]];then
    echo "->>> $i is link" >>/home/test2/stress_log/lan_stress.log
    mac=$(ifconfig $i |grep -Eo '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
    echo $mac
       speed=$(ethtool $i |grep "Speed: ")
       speed=$(echo $speed)>>/home/test2/stress_log/lan_stress.log
            if [ "$speed" = "$such" -o "$speed" = "$as" ];then
               echo "->>> start to check Lan in this time" >>/home/test2/stress_log/lan_stress.log
               chmod +x /home/test2/lan_stress/pktgentest.sh
               /home/test2/lan_stress/pktgentest.sh -i $i -m $mac -s 1500 >>/home/test2/stress_log/lan_stress.log
               sleep 2
             else
                echo "->>> $i speed is not 10000Mb/s or 25000Mb/s, nothing to do" >>/home/test2/stress_log/lan_stress.log
             fi
  else
    echo "->>> $i need link!" >>/home/test2/stress_log/lan_stress.log
  fi
done


