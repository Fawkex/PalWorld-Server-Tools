#!/bin/python

from mcrcon import MCRcon
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AutoShutdown')
logger.setLevel(logging.INFO)

server_host = '127.0.0.1'
server_port = 11926
password = '19260817'

# 检查间隔（秒）
check_interval = 60
# 多少次检查没人就自动关服务器
timeout = 15

def shutdown():
    with MCRcon(server_host, password, server_port) as client:
        client.connect()
        _ = client.command('Shutdown 1')

def get_player_count():
     with MCRcon(server_host, password, server_port) as client:
        client.connect()
        players = client.command('ShowPlayers')
        players_count = len(players.split('\n'))-2
        return players_count


def main():
    players_counts = [ 1 for _ in range (timeout) ]
    while True:
        try:
            players_count = get_player_count()
            players_counts.append(players_count)
            logger.info(f'Players Count: {players_count}')
        except Exception as e:
            logger.error("Get Player Count: Unable to connect to server.")
        if not any(players_counts[-timeout:]):
            logger.info(f"Shutting down as server is empty in last {timeout} checks.")
            try:
                shutdown()
            except Exception as e:
                logger.error('Shutdown: Unable to connect to server.')
            logger.info("Shutdown commenced.")
        time.sleep(check_interval)
        
if __name__ == '__main__':
    main()
