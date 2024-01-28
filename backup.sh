#!/bin/bash

HOST="localhost"
PORT=11926
PASSWD="19260817"

SAVE_PATH="/home/steam/Steam/steamapps/common/PalServer/Pal/Saved/SaveGames/0"
BACKUP_PATH="/home/steam/Backups"

mkdir -p $BACKUP_PATH

# Save
echo Save| mcrcon --password $PASSWD -p $PORT $HOST

# Backup
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE=$BACKUP_PATH/$DATE.tar.gz

tar -czf $BACKUP_FILE -C $SAVE_PATH .

echo "Backup of $SAVE_PATH completed. Backup file is located at: $BACKUP_FILE"

exit 0
