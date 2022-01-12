#!/bin/bash
core_num=$(cat /proc/cpuinfo | grep -c processor)-5
core_num=`expr "$core_num" - 5`
tar -zxvf /home/stress-1.0.4.tar.gz
cd /home/stress-1.0.4
./configure
make -j $core_num
make install


tar -zxvf /home/memtester-4.5.1.tar.gz
cd /home/memtester-4.5.1
make -j $core_num
make install


tar -zxvf /home/fio-3.20.tar.gz
cd /home/fio-3.20
./configure
make -j $core_num
make install

if ! [ -x "$(command -v stress)" ]; then
  echo "stress未安装成功！重新安装中！"
  rm -rf /home/stress-1.0.4
  tar -zxvf /home/stress-1.0.4.tar.gz
  cd /home/stress-1.0.4
  ./configure
  make -j $core_num
  make install
  if ! [ -x "$(command -v stress)" ]; then
    echo "stress重新安装失败!"
  else
    echo "stress重新安装成功！"
  fi
else
  echo "stress已经安装！"
  if ! [ -x "$(command -v memtester)" ]; then
    echo "memtester未安装成功！重新安装中！"
    rm -rf /home/memtester-4.5.1
    tar -zxvf /home/memtester-4.5.1.tar.gz
    cd /home/memtester-4.5.1
    make -j $core_num
    make install
    if ! [ -x "$(command -v memtester)" ]; then
      echo "memtester重新安装失败!"
    else
      echo "memtester重新安装成功！"
    fi
  else
    echo "memtester已经安装！"
    if ! [ -x "$(command -v fio)" ]; then
      echo "fio未安装成功！重新安装中！"
      rm -rf /home/fio-3.20
      tar -zxvf /home/fio-3.20.tar.gz
      cd /home/fio-3.20
      ./configure
      make -j $core_num
      make install
      if ! [ -x "$(command -v fio)" ]; then
        echo "fio重新安装失败!"
      else
        echo "fio重新安装成功！"
      fi
    else
      echo "fio已经安装！"
      echo "stress、memtester、fio都安装成功！请执行程序"
    fi
  fi
fi








