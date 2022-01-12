# /bin/bash
# 没有安装stress
if ! [ -x "$(command -v smartctl)" ]; then
  sudo apt-get install smartmontools
  echo "smartctl安装成功！"
else
  echo "smartctl已经安装！"
fi

echo ' '
echo "[ sudo smartctl --all /dev/sdd ]"
sudo smartctl --all /dev/sdd

