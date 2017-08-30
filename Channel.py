MINIMUM_PORT = 1024
MAXIMUM_PORT = 64000

import Reciever
import Sender
def main():
    #c_sin,c_sout,c_rin,c_rout = input("Enter the Four Port Numbers for Channel: ").split()
    i = 0
    c_sin,c_sout,c_rin,c_rout = 0,0,0,0
    channel_ports = [0,0,0,0] #Binds ports to correct sockets Order is SENDER IN , SENDER OUT, RECIEVER IN , RECIEVER OUT
    print("Please enter the port numbers for the channel in this order:\n  Sender IN , Sender OUT, Reciever IN, Reciever OUT")
    while(i < 4):
        port = int(input("Enter a channel port number: "))
        if(MINIMUM_PORT < port < MAXIMUM_PORT):
            channel_ports[i] = port
            i+= 1
        else:
            port = int(input("Port number must lie between 1024 and 64,000: "))
            if(MINIMUM_PORT < port < MAXIMUM_PORT):
                channel_ports[i] = port
                i+= 1
    s_in = int(input("Please enter the S_IN port number: "))
    r_in = int(input("Please enter the R_IN port number: "))
    loss = float(input("Please enter packet loss rate between 0 and 1: "))
    if(loss > 0 or loss < 1):
        loss = float(input("Please enter packet loss between 0 and 1: "))
    
def connect(c_sin,c_sout,c_rin,c_rout):
    sender = Sender(c_out,c_sin)
    reciever = Receiver(c_rout,c_rin)
    
    

main()
    