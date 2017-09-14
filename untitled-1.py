'''Both communicate with each other using packets of
a certain size and sending these through the channel'''
import socket
import sys
from Packet import *
import select
import random

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
    #in channel, data in of sender
    
    c_sout = int(sys.argv[2])
    check_length(c_sout, "Csender output")
    #in channel, data out of sender
    
    c_rin = int(sys.argv[3])  
    check_length(c_rin, "Creceiver input")
    #in channel, data in of receiver
    
    c_rout = int(sys.argv[4])  
    check_length(c_rout, "Creceiver output")
    #in channel, data out of receiver
    
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

c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss = get_options()

#create a socket
#check the error
try:
    Csin = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    Csout = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    Crin = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    Crout = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    Sin = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    Rin = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    print("Socket created successfull.")
except socket.error as msg:
    print('Failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit(1)

'''Bind localhost'''
try:
    Csin.bind(('localhost', c_sin))
    Csout.bind(('localhost', c_sout))
    Crin.bind(('localhost', c_rin))
    Crout.bind(('localhost', c_rout))
    print("Bind success.")
except socket.error as msg:
    print('Bind failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

'''Connect'''
try:
    Csout.connect(('localhost', s_in))
    Crout.connect(('localhost', r_in))
    print("Connect success.")
except socket.error as msg:
    print('Connect failed: Error Code is ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

'''Enter a infinite loop'''

while True:
    in_put, out_put, excep = select.select([Csin, Crin], [], [], 0.1)
    #input data
    for s in in_put:
        if s == Csin:
            # receive data
            data, address = Csin.recvfrom(512)
            # convert string to packet instance
            packet = loads(data)
            #use packet data
            if packet.magic != "0x497E" or random.random() < loss:
                #drop
                continue
            else:
                try:
                    Crout.send(dumps(packet))
                except:
                    print("Channel cannot send packet to receiver.")
                    sys.exit(1)
        if s == Crin:
            # receive data
            data, address = Crin.recvfrom(512)
            # convert string to packet instance
            packet = loads(data)
            #use packet data
            if packet.magic != "0x497E" or random.random() < loss:
                continue
            else:
                try:
                    Csout.send(dumps(packet))
                except:
                    print("Channel cannot send packet to sender.")
                    sys.exit(1)