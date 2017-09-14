
MAGIC_NUMBER = 0x497E


class Packet:
    def __init__(self,magic,packetType,seqNo,dataLen,data):
        self.magicno = magic
        self.packetType = packetType
        self.seqNo = seqNo
        self.dataLen = dataLen
        self.data = data
        self.constraints()
    '''Checks against rules for Packets'''
    def constraints(self):
        if self.packetType == 0: #DATA
            if self.dataLen > 513 or self.dataLen < 0:
                raise ValueError("Packet value must be between 0 and 512")
            if self.dataLen == 0:
                print("End of File")
        elif self.packetType == 1: #ACKNOWLEDGMENT PACKET
            if self.dataLen != 0:
                print("Drop Packet")
        else:
            raise ValueError("Packet Type must be either Data (0) \n or an Acknoledgment Packet (1)")

    def __str__(self):
        return '---Packet---\nMagicNo: {}\nType: {}\nSequence Number: {}\nData Len: {}\nPayload: {}'.format(self.magicno,
                                                                                           self.packetType,
                                                                                           self.seqNo,
                                                                                           self.dataLen,
                                                                                           self.data)
def main():
    p = Packet(0x497E,0,1,510,"text")
    print(p)
    
main()