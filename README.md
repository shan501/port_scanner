# port_scanner

This script will scan a ip address and let you know what port is open on that machine


## Target Machine
Specify the ip address that you want to scan 

```
ip='192.168.183.131'

```
## Port Scan Function

This is a function that we will use to determine if a specific port is open on a ip address

```
def portscan(port):
    try :
        s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((ip,port))
        return True 
    except:
        return False

```

It returns true if it successully connected to that port and false if it dont


## Open and Unopen Ports

Stores open and unopen ports in a list 

```
port_list=[]
no_port_list=[]

```

## Function to scan all the ports 

This function will iterate through 1-100 and scan each of these port 

```
for port in range(100):
    if (portscan(port)):
        print ('The port ' , port , 'is open on ',ip)
        port_list.append(port)
    else : 
        print ('The port ', port , 'is close on ',ip)
        no_port_list.append(port)

```
## Return Output 
Finally return all the ports that are open and all the ports that are closed

```
print('The following ports are open ',port_list , 'on ', ip)
print('The following ports are close ',no_port_list , 'on ',ip)
```



