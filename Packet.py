
MAGIC_NUMBER = 0x497E


class Packet:
    def __init__(self,magic,packet_type,seqno,dataLen,data):
        self.magicno = magic
        self.packet_type = packet_type
        self.seqno = seqno
        self.dataLen = dataLen
        self.data = data
        
    '''Checks against rules for Packets'''
    def constraints(self):
        if self.magicno != MAGIC_NUMBER:
            raise ValueError("Magic Number mismatch")
        if self.packet_type == 0: #DATA
            if self.dataLen > 512 or self.dataLen < 0:
                raise ValueError("Packet value must be between 0 and 512")
            if self.dataLen == 0:
                print("End of File")
        elif self.packet_type == 1: #ACKNOWLEDGMENT PACKET
            if self.dataLen != 0:
                print("Drop Packet")
        else:
            raise ValueError("Packet Type must be either Data (0) \n or an Acknoledgment Packet (1)")
    
def main():
    magic = MAGIC_NUMBER
    packet_type = 0
    seqno = 2
    dataLen = 1
    data = [0] * dataLen 
    x = Packet(magic,packet_type,seqno,dataLen,data)
    x.constraints()
    
    
main()