#!/bin/bash
#rmmod pktgen
#sleep 5
#modprobe pktgen


ld="Link detected: yes"
one_sd="Speed: 1000Mb/s"
ten_sd="Speed: 10000Mb/s"
tf_sd="Speed: 25000Mb/s"
e24f0="enp24s0f0"
e24f1="enp24s0f1"
e59f0="enp59s0f0"
e59f1="enp59s0f1"

ip=1
count=0
j=0

i=0
declare -a array_mac
for enp in `ls /sys/class/net`
do
  if [ "$enp" = "$e24f0" -o "$enp" = "$e24f1" -o "$enp" = "$e59f0" -o "$enp" = "$e59f1" ];then
  mac=$(ifconfig $enp |grep -Eo '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}')
  #echo $mac
  array_mac[$i]=$mac
  i=$(($i+1))
  fi
done
echo ${array_mac[*]}



for i in `ls /sys/class/net`
do
  link=$(ethtool $i |grep "Link detected:")
  link=$(echo $link)

  if [[ "$link" = "$ld" ]];then
    echo "->>> $i is link"
    
#    echo $mac
       speed=$(ethtool $i |grep "Speed: ")
       echo "->>> $i:$speed"
       speed=$(echo $speed)
            if [ "$speed" = "$ten_sd" -o "$speed" = "$tf_sd" -o "$speed" = "$one_sd" ];then
                # echo "->>> start to check Lan in this time"
                if [ "$i" = "$e24f0" -o "$i" = "$e24f1" -o "$i" = "$e59f0" -o "$i" = "$e59f1" ];then
                    echo $i
                    echo rem_device_all >/proc/net/pktgen/kpktgend_$count
                    echo add_device $i > /proc/net/pktgen/kpktgend_$count
                    echo count 10000 > /proc/net/pktgen/$i
                    echo clone_skb 1000 >/proc/net/pktgen/$i
                    echo pkt_size 1500 >/proc/net/pktgen/$i
                    
                    echo dst 10.11.11.$ip >/proc/net/pktgen/$i
                    b=$(($count%2))
                    if [ $b = 0 ];then
                      echo dst_mac ${array_mac[$(($j+1))]} >/proc/net/pktgen/$i
                    else
                      echo dst_mac ${array_mac[$(($j-1))]} >/proc/net/pktgen/$i
                    fi
                    ip=`expr $ip + 1`
                    count=$(($count+1))
                    j=`expr $j + 1`
                fi
                sleep 2

            else
                echo "->>> $i speed is not 10000Mb/s or 25000Mb/s, nothing to do"
            fi
  else
    echo "->>> $i need link!"
  fi
done


