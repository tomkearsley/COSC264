'''Both communicate with each other using packets of
    a certain size and sending these through the channel'''
import socket
import sys
import Packet
import select
import random
import pickle

localhost = '127.0.0.1'
#First is the port number
def check_length(port, port_desc):
    """check whether port number is in range"""
    if 1024 < port < 64000:
        True
    else:
        print(port_desc + " port number not in range 1024~64000")
        sys.exit(1)

def get_options():
    #port number
    """get variables from command_line"""
    c_sin = int(sys.argv[1])
    check_length(c_sin, "Csender input")
    #in channel,data in of sender
    
    c_sout = int(sys.argv[2])
    check_length(c_sout, "Csender output")
    #in channel,data out of sender
    
    c_rin = int(sys.argv[3])
    check_length(c_rin, "Creceiver input")
    #in channel,data in of receiver
    
    c_rout = int(sys.argv[4])
    check_length(c_rout, "Creceiver output")
    #in channel,data out of receiver
    
    s_in = int(sys.argv[5])
    check_length(s_in, "sender input")
    #data input in sender
    
    r_in = int(sys.argv[6])
    check_length(r_in, "receiver input")
    #data input in receiver
    
    loss = float(sys.argv[7])
    if loss < 0 or loss >= 1:
        print("packet loss rate is not in range")
        sys.exit(1)
    return c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss

<<<<<<< HEAD
def non_terminal(c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss):
    return c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss

#c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss = nonterminal()
c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss = get_options()
=======
>>>>>>> origin/master

#c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss = get_options()

def channel(c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss):
    #next step, we need to create a socket
    #we can create error check every step to make function more perfect
    try:
        Csin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Csin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        Csout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Csout.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        Crin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Crin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        Crout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Crout.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        print("Socket created successfull.")
    except socket.error as msg:
        print('Failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit(1)
    
    '''Bind 127.0.0.1'''
    try:
        Csin.bind((localhost, c_sin))
        Csout.bind((localhost, c_sout))
        Crin.bind((localhost, c_rin))
        Crout.bind((localhost, c_rout))
        print("Bind success.")
    except socket.error as msg:
        print('Bind failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    
    '''Connect'''
    
    try:
        Csin.listen(5)
        Csin_connect, Csin_connect_addre = Csin.accept()
        Csout.connect((localhost, s_in))
        
        Crin.listen(5)
        Crin_connect, Crin_connect_addre = Crin.accept()
        Crout.connect((localhost, r_in))
        print("Connect success.")
    except socket.error as msg:
        print('Connect failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    
    '''Enter a infinite loop'''
    
    final_packet = False
    while True:
        in_put, out_put, excep = select.select([Csin_connect, Crin_connect], [], [], 1)
        error = False
        #data input
        for s in in_put:
            if s == Csin_connect:
                # receive data
                packet_fwd = Csin_connect.recv(1024)
                # convert string to packet instance
                packet_error = pickle.loads(packet_fwd)
                #use data from the packet
                if packet_error.magic != "0x497E" or random.random() < loss:
                    #drop
                    continue
                if packet_error.seqNo == 0:
                    final_packet = True
                    print("Reveived the final packet.")
                if random.uniform(0, 1) < 0.1:
                    print("bit error")
                    #unpickle, change, pickle
                    
                    packet_error.dataLen += random.randint(1, 10)
                    
                    #pickle it up again
                    packet_stream = pickle.dumps(packet_error)
                    packet_buffer = []
                    packet_buffer.append(packet_stream)
                    error = True
                    Crout.send(packet_buffer[0])
                
                #Send to receiver
                if not error:
                    Crout.send(packet_fwd)
        
            if s == Crin_connect:
                # receive data
                packet_fwd = Crin_connect.recv(1024)
                # convert string to packet instance
                packet_error = pickle.loads(packet_fwd)
                #use data from the packet
                if packet_error.magic != "0x497E" or random.random() < loss:
                    #drop
                    continue
                if packet_error.seqNo == 0:
                    final_packet = True
                    print("Reveived the final packet.")
                if random.uniform(0, 1) < 0.1:
                    print("bit error")
                    #unpickle, change, pickle
                    
                    packet_error.dataLen += random.randint(1, 10)
                    
                    #pickle it up again
                    packet_stream = pickle.dumps(packet_error)
                    packet_buffer = []
                    packet_buffer.append(packet_stream)
                    error = True
                    Csout.send(packet_buffer[0])
                if not error:
                    Csout.send(packet_fwd)
                    if final_packet == True:
                        break



    Csin.close()
    Csout.close()
    Crin.close()
    Crout.close()


<<<<<<< HEAD
        if s == Crin_connect:
            # receive data
            packet_fwd = Crin_connect.recv(1024)
            # convert string to packet instance
            packet = pickle.loads(packet_fwd)
            #use data from the packet
            if packet.magic != "0x497E" or random.random() < loss:
                #drop
                continue
            if packet.seqNo == 0:
                final_packet = True
                print("Reveived the final packet.")              
            if random.uniform(0, 1) < 0.1:
                print("bit error")
                #unpickle, change, pickle
                
                packet.dataLen += random.randint(1, 10)
                                 
                #pickle it up again
                packet_stream = pickle.dumps(unpickle_error)
                packet_buffer = []
                packet_buffer.append(packet_stream)
                error = True
                Csout.send(packet_buffer[0])
                if final_packet == True:
                    break
                             
            #Send to receiver
            if not error:
                Csout.send(packet_fwd)
                if final_packet == True:
                    break
                
Csin.close()
Csout.close()
Crin.close()
Crout.close()



=======
channel(8000, 8001, 8002, 8003, 8004, 8005, 0)
>>>>>>> origin/master
