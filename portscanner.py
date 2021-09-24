#! /usr/bin/env python3 
import socket 

#ip address that you want to scan 
ip='192.168.183.131'

#the function that scans the port, returns true if successfully connected and false if not
def portscan(port):
    try :
        s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((ip,port))
        return True 
    except:
        return False 
#store the open and not open ports in a list 
port_list=[]
no_port_list=[]


print ('Starting Port Scan....')

#specif the port numbers you want to scan 
for port in range(100):
    if (portscan(port)):
        print ('The port ' , port , 'is open on ',ip)
        port_list.append(port)
    else : 
        print ('The port ', port , 'is close on ',ip)
        no_port_list.append(port)

print('The following ports are open ',port_list , 'on ', ip)
print('The following ports are close ',no_port_list , 'on ',ip)




