import socket
import pickle
import select

IP = '127.0.0.1'
MAGIC_NO = 0x497E
DATA_PACKET = 0
ACK_PACKET = 1

def receiver(port_rin, port_rout, port_cin, file_name):
    '''check ports for validity'''
    for port in [port_rin, port_rout, port_cin]:
        if not check_port_nums(port):
            return -1
    
    '''create sockets'''
    sock_rin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_rout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    '''bind sockets'''
    sock_rin.bind((IP, port_rin))
    sock_rout.bind((IP, port_rout))
    
    '''connect rout socket to cin socket'''
    sock_rout.connect((IP, port_cin))
    
    file = open(file_name, 'a')
    
    expected = 0
    
    sock_rin.listen(5)
    sock_cin, _ = sock_rin.accept()
    
    message_recived = False
    while not message_recived:
        ready = select.select([sock_cin], [], [])       # waits until data is ready to receive, blocking call
        if ready[0]:                                    # there is an addr to recevie from
            packet = rin_addr.recv(1024)
            packet = pickel.loads(packet)
            if packet.magicno != MAGIC_NO:
                continue
            if packet.packetType != DATA_PACKET:
                continue
            if packet.seqno != expected:
                ack_packet = Packet(MAGIC_NO, ACK_PACKET, packet.seqno, 0, None)
                sock_rout.send(pickle.dumps(ack_packet))
                continue
            else:
                ack_packet = Packet(MAGIC_NO, ACK_PACKET, packet.seqno, 0, None)
                sock_rout.send(pickle.dumps(ack_packet))
                expected += 1
                if packet.dataLen > 0:
                    file.write(pickle.loads(packet.data))
                else:
                    file.close()
                    break






def check_port_nums(port):
    '''checks port number for validity'''
    if port <= 64000 and port >= 1024:
        return True
    else:
        return False

receiver(8005, 12333, 8002, "wow.txt")
