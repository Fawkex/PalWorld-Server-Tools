#!/bin/bash

HOST="localhost"
PORT=11926
PASSWD="19260817"

echo Shutdown 1| mcrcon --password $PASSWD -p $PORT $HOST

exit 0
