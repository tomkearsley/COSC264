import Packet
import channel
import reciever
import sender


def main():
    #c_sin, c_sout, c_rin, c_rout, s_in, r_in, loss
    port1 = 10290 
    port2 = 10250
    port3 = 10260
    port4 = 10270
    port5 = 10280
    port6 = 10300
    port7 = 10310
    port8 = 10320
    loss = 0 
    
    c = Channel(port3, port4, port6, port5, port1, port7, loss)
    s = sender(port1, port2, port3, 'test.txt')
    r = reciever(port7, port8, port6,'outputfile.txt')
    #port_sin,port_sout,c_sin,raw_file
  