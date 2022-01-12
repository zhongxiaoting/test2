# /bin/bash
# CPU MCE检测工具rasdaemon安装
if ! [ -x "$(`command -v rasdaemon`)" ]
  then
    sudo apt-get install rasdaemon
    if ! [ -x "$(`command -v rasdaemon`)" ]
      then
        echo "rasdaemon安装失败！"
    else
      echo "rasdaemon安装成功！"
    fi
else
  echo "rasdaemon已经安装！"
fi