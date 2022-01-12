# /bin/bash
# 没有安装stress
if ! [ -x "$(command -v stress)" ]; then
  sudo apt-get install stress
  echo "stress安装成功！"
else
  echo "stress已经安装！"
fi

