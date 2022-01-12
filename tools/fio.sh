# /bin/bash
# 没有安装stress
if ! [ -x "$(command -v fio)" ]; then
  sudo apt-get install fio
  echo "fio安装成功！"
else
  echo "fio已经安装！"
fi

echo ' '
echo "[ sudo fio -filename=/dev/sde -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=2G\
-numjobs=10 -runtime=10 -group_reporting -name=mytest ]"
sudo fio -filename=/dev/sde -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=2G\
-numjobs=10 -runtime=5 -group_reporting -name=mytest


