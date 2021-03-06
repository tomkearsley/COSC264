import sys
import time
import pickle
import select
import packet
import socket
PACKET_COUNT = 0
MAX_PACKET = 512
MAGIC_NUMBER = 0x497E
TIME_OUT = 1
IP = '127.0.0.1'




def sender(port_sin,port_sout,c_sin,raw_file):
    
    '''CHECK PORTS FOR IN RIGHT VALUES:'''
    minPort = 1024
    maxPort = 64000
    portList = [port_sin,port_sout,c_sin,"Sender in","Sender out","Channel in"]
    for i in range (0,3):
        if (portList[i] < 1024 or portList[i] > 64000):
            raise Exception("Port {} not in valid range.".format(portList[i+3]))
    
    '''Creating Sockets'''
    sout = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SENDER OUT
    
    
    sin = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SENDER IN
    
    
    '''BINDING SOCKETS'''
    sout.bind((IP, port_sout))
    sin.bind((IP,port_sin))
    
    
    '''Connecting Sender out to Channel in'''
    sout.connect((IP,c_sin))
    
    
    sin.listen(5) # Listen at Max Necessary?
    
    sinConnection, sinAddress = sin.accept()
<<<<<<< HEAD
            
    packetConfirmation = False   
=======
    
    packetConfirmation = False
>>>>>>> origin/master
    packetBuffer = [] # All Packets to be transmitted Packets will be serialized.
    readBytes = 0
    filePos = 0
    flagExit = False
    
    sequenceNo = 1
    
    
    try:
        file = open(raw_file, 'rb')
    except IOError:
        printf("File Could not Be Found!")
        exit()


    while not flagExit:
        file.seek(filePos)
        packet_size = file.read(512)
        if len(packet_size) > 0:
            packet = packet.Packet(MAGIC_NUMBER,0,sequenceNo,len(packet_size),packet_size)
            filePos += 512
        else:
            sequenceNo = 0;
            packet = packet.Packet(MAGIC_NUMBER,0,sequenceNo,0,None)
            exit_flag = True
        
        serializedPacket = pickle.dump(packet) #Serialize packet using Pickle
        packetBuffer.append(serializedPacket)
        while (packetConfirmation == False):
            sout.send(packetBuffer[0]) # Send first packet in buffer.
            
            # Arguments: 1 = list waiting for reading, last = timeout time.
            tripleList = select.select([s_in_connection], [], [], 1)
            # ^ Return Val = Three items List of objects that are ready.
            
            if tripleList[0]:
                recievedPacket = sinConnection.recv(1024)
                recievedPacket = pickle.loads(recievedPacket)
                if getattr(recievedPacket,'seqNo') == sequenceNo:
                    sequenceNo += 1
                    packetBuffer.pop(0)
                    packetConfirmation = True
            else:
                print("Confirmation Packet not received. \nRetransmitting....")





        sin.close()
        sout.close()




def displayPacketData(packet_buffer):
    for i in range(0,(len(packet_buffer))):
        packet = packet_buffer[i]
        print(getattr(packet,'data'))





<<<<<<< HEAD
sender(10290, 10250, 10260, "test.txt")
        
=======
sender(8004, 12315, 8000, "todo.txt")
>>>>>>> origin/master
