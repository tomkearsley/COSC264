import socket
import Packet
import os
PACKET_COUNT = 0
MAX_PACKET = 512
MAGIC_NUMBER = 0x497E
class Sender:
    def __init__(self,port_in,port_out,file):
        self.in_address = ('localhost',port_in)
        self.out_address = ('localhost',port_out)
        self.port_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Goes to 
        self.port_out.bind(self.out_address)
        packet_buffer = []
        open_file = open(file,'rb')
        self.create_packet(open_file,packet_buffer)
        self.displayPacketData(packet_buffer)
        
        


    def create_packet(self,open_file,packet_buffer):       
        size = 80000 #10 Kb
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
    
    def displayPacketData(self,packet_buffer):
        for i in range(0,(len(packet_buffer))):
            packet = packet_buffer[i]
            print(getattr(packet,'data'))
    
    

     

        




def main():
    file = "test.txt"
    S = Sender(1024,2048,file)

        
    
    




main()
        