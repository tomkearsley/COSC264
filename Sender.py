import socket
import Packet
import os
import sys
PACKET_COUNT = 0
MAX_PACKET = 512
MAGIC_NUMBER = 0x497E
TIME_OUT = 1
IP = '127.0.0.1'
def sender(port_sin,port_sout,c_sin,file):
    '''Creating Sockets'''
    port_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''Binding sockets to Addresses'''
    port_in.bind((IP,port_sin))
    port_out.bind((IP,port_sout))
    
    packet_buffer = [] # All Packets to be transmitted
    
    
    '''Listening'''
    port_out.listen(1)
    
    # connect() sout
    #port_out.connect((IP, c_sin))  # set to default receiver to port_num of Csin
    
    
    
    # check if supplied filename exits and is readable else exit sender 
    '''
    if not (os.path.isfile(PATH) and os.access(PATH, os.R_OK)):
        exit(-1)'''
        
    sender_next = 0 #local integer variable set to 0
    exit_flag = False # exit Flag 
    
    while True:
        with open(file, 'rb') as file:
            local_buffer = file.read(MAX_PACKET)  
        
        packet_size = sys.getsizeof(local_buffer)
        if packet_size > 0:
            #Packet = (magic,type,seqno,dataLen,data)
            packet = Packet.Packet(MAGIC_NUMBER,0,sender_next,packet_size,local_buffer)
            packet_buffer.append(packet)
        else:
            packet = Packet.Packet(MAGIC_NUMBER,0,sender_next,0,0)
            packet_buffer.append(packet)
            exit_flag = True
        inner_loop = True
        while inner_loop:
            count = 0
            port_out.send(packet) #sends packet
            
            socket_list = [port_in, sys.stdin]
            read_sock, write_sock, error_sock, _ = select.select(
                socket_list, [], [],
                TIMEOUT)            
            if exit_flag:
                print('Total Packets Sent:', sent_packet_count)
                file_name.close()
                sock_sin.close()
                sock_sout.close()
            else:
                inner = False            
        


        
        




'''
    def create_packet(self,open_file,packet_buffer):       
        remainder = size - ((len(packet_buffer) + 1 )* MAX_PACKET)
        while remainder > MAX_PACKET:
            open_file.seek(remainder)
            local_buffer = open_file.read(MAX_PACKET)       
            magic = MAGIC_NUMBER
            packet_type = 0
            seqno = 2        
            packet = Packet.Packet(magic,packet_type,seqno,MAX_PACKET,local_buffer)
            packet_buffer.append(packet)
            remainder = size - ((len(packet_buffer) + 1 )* MAX_PACKET)
        open_file.seek(remainder)
        local_buffer = open_file.read(remainder)
        magic = MAGIC_NUMBER
        packet_type = 0
        seqno = 2        
        packet = Packet.Packet(magic,packet_type,seqno,remainder,local_buffer)
        packet_buffer.append(packet)
        
        return packet_buffer
    '''
def displayPacketData(self,packet_buffer):
    for i in range(0,(len(packet_buffer))):
        packet = packet_buffer[i]
        print(getattr(packet,'data'))
    
    

     

        




def main():
    file = 'test.txt'
    s = sender(1026,1028,1030,file)

        
    
    




main()
        