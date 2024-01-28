#!/bin/bash

# 检查是否存在包含"PalServer-Linux-Test"字段的进程
if pgrep -f "PalServer-Linux-Test" > /dev/null; then
  echo "A process containing 'PalServer-Linux-Test' is already running."
else
  echo "PalServer not running. Starting PalServer,"

  # 创建一个新的detached（分离）的screen会话
  if screen -ls | grep -q "[^0-9]*pal[^0-9]*"; then
    echo "A screen session named 'pal' already exists."
    screen -D pal
  else
    echo "Screen not running. Starting a new detached screen session."
    
    screen -dmS pal
  fi
  
  # 在后台screen会话中执行命令
  screen -S pal -X stuff "
    cd ~/Steam/steamapps/common/PalServer
    ./PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS
    ^M
  "

  echo "PalServer started in background screen session."
fi

exit 0
