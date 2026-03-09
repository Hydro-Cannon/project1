import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

try:
    print('Starting...')
    while True:
        raw_data, addr = s.recvfrom(65536)
        print(f'addr: {addr}')
        print(f'data: {raw_data}')
except KeyboardInterrupt:
    print('\nShutting Down...')

finally:
    s.close()
