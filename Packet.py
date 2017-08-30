
MAGIC_NUMBER = 0x497E


class Packet:
    def __init__(self,magic,packet_type,seqno,dataLen,data):
        self.magicno = magic
        self.packet_type = packet_type
        self.seqno = seqno
        self.dataLen = dataLen
        self.data = data
    def constraints():
        print("Enterign")
        if self.seqno != 0:
            print("Error 1")
def main():
    print("asdadsa")
    magic = MAGIC_NUMBER
    packet_type = "dataPacket"
    seqno = 2
    dataLen = 512
    data = " " * dataLen 
    x = Packet(4,3,2,1,1)
    x.constraints()