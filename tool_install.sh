#!/bin/bash
core_num=$(cat /proc/cpuinfo | grep -c processor)-5
core_num=`expr "$core_num" - 5`

cp storcli64 /home

cd /home/tools/fio-3.20
./configure
make -j $core_num
make install

cd /home/tools
rpm -ivf net-snmp-libs-5.7.2-49.el7_9.1.x86_64.rpm
rpm -ivf OpenIPMI-modalias-2.0.27-1.el7.x86_64.rpm OpenIPMI-libs-2.0.27-1.el7.x86_64.rpm OpenIPMI-2.0.27-1.el7.x86_64.rpm
rpm -ivf /home/tools/ipmitool-1.8.18-9.el7_7.x86_64.rpm


rpm -ivf /home/tools/perl-*.x86_64.rpm
#rpm -ivf /home/tools/perl-Compress-Raw-Zlib-2.061-4.el7.x86_64.rpm
#rpm -ivf /home/tools/perl-IO-Compress-2.061-2.el7.noarch.rpm
#rpm -ivf /home/tools/perl-Net-Daemon-0.48-5.el7.noarch.rpm
#rpm -ivf /home/tools/perl-PlRPC-0.2020-14.el7.noarch.rpm
#rpm -ivf /home/tools/perl-DBD-SQLite-1.39-3.el7.x86_64.rpm
#rpm -ivf /home/tools/perl-DBI-1.627-4.el7.x86_64.rpm
rpm -ivf /home/tools/rasdaemon-0.4.1-37.el7.x86_64.rpm


if [ -x "$(command -v ipmitool)" ]; then
  echo "ipmitool install success"
else
  echo "ipmitool install fail"
fi

if [ -x "$(command -v ras-mc-ctl)" ]; then
  echo "rasdaemon install success"
else
  echo "rasdaemon install fail"
fi


if [ -x "$(command -v stress)" ]; then
  echo "stress is already installed"
else
  tar -zxvf /home/tools/stress-1.0.4.tar.gz
  cd /home/tools/stress-1.0.4
  ./configure
  make -j $core_num
  make install
  if [ -x "$(command -v stress)" ]; then
    echo "stress install success"
  else
    echo "stress install fail"
  fi
fi


if [ -x "$(command -v memtester)" ]; then
  echo "memtester is already installed"
else
  tar -zxvf /home/tools/memtester-4.5.1.tar.gz
  cd /home/tools/memtester-4.5.1
  make -j $core_num
  make install
  if [ -x "$(command -v memtester)" ]; then
    echo "memtester install success"
  else
    echo "memtester install fail"
  fi
fi


if [ -x "$(command -v fio)" ]; then
  echo "fio is already installed"
else
  tar -zxvf /home/tools/fio-3.20.tar.gz
  cd /home/tools/fio-3.20
  make -j $core_num
  make install
  if [ -x "$(command -v fio)" ]; then
    echo "fio install success"
  else
    echo "fio install fail"
  fi
fi









