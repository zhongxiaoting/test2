#!/bin/bash
rmmod pktgen
sleep 5
modprobe pktgen

# chmod +x lan_while.sh
# timeout 2m ./lan_while.sh &
ld="Link detected: yes"
one_sd="Speed: 1000Mb/s"
ten_sd="Speed: 10000Mb/s"
tf_sd="Speed: 25000Mb/s"
enp0="enp24s0f0"
for i in `ls /sys/class/net`
do
  link=$(ethtool $i |grep "Link detected:")
  link=$(echo $link)

  if [[ "$link" = "$ld" ]];then
    echo "->>> $i is link"
    mac=$(ifconfig $i |grep -Eo '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
#    echo $mac
       speed=$(ethtool $i |grep "Speed: ")
       echo "->>> $i is $speed"
       speed=$(echo $speed)
            if [ "$speed" = "$ten_sd" -o "$speed" = "$tf_sd" -o "$speed" = "$one_sd" ];then
                # echo "->>> start to check Lan in this time"
                if "$i"="$enp0";then
                    echo "aaa"
                fi

                sleep 2
            else
                echo "->>> $i speed is not 10000Mb/s or 25000Mb/s, nothing to do"
            fi
  else
    echo "->>> $i need link!"
  fi
done


