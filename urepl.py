# Simple urepl like module
# takes care of connecting to wifi or creating your own
# written for the Rapsberry Pi Pico W


import socket
import network
import time

global connection_type
global ssid
global password

global server_ip
global client_ip
global port
global timeout

try:
    import frint
    frint.frint('hi from frint inside of urepl')
except:
    print('failed to use frint in urepl')


# Default Network to connect using wificonnect()
# Change these settings or use the built in functions
connection_type = 'Not Connected'
ssid = 'OpenMuscle'
password = '3141592653'
port = 3145
server_ip = '0.0.0.0'
client_ip = '192.168.1.32'
timeout = 15


def wificonnect(ssid=ssid,password=password):
    print('Use: like urepl.wificonnect(SSID,Password)')
    print('otherwise uses default global ssid,password')
    print('returns wlan object from network')
    global server_ip
    global connection_type
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect(ssid,password)
    while not wlan.isconnected():
        pass
    server_ip = wlan.ifconfig()[0]
    print('Wifi Connected!!')
    print(f'SSID: {ssid}')
    print('Local Ip Address, Subnet Mask, Default Gateway, Listening on...')
    print(wlan.ifconfig())
    connection_type = 'Wireless Client'
    return wlan

def wap(pico_ssid = "PicoW",pico_pass = "picopico"):
    global server_ip
    print('Use: like urepl.wap(SSID,Password)')
    print('otherwise uses default Picow,picopico')
    print('returns network wap object')
    #Create a network and WAP Wireless Access Point
    wap = network.WLAN(network.AP_IF)
    wap.config(essid=pico_ssid,password=pico_pass)
    wap.active(False) #rare instances keep this on
    wap.active(True)
    while wap.active == False:
        pass
    print('Wireless Access Point (WAP) Created!!')
    print(f'SSID: {pico_ssid}')
    print(f'PASSWORD: {pico_pass}')
    print('Local Ip Address, Subnet Mask, Default Gateway, Listening on...')
    server_ip = wap.ifconfig()[0]
    print(wap.ifconfig())
    return wap

def send(data):
    global client_ip
    global port
    d = b''
    d += data
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    destination = (client_ip,port)
    print(s)
    s.sendto(d,destination)
    s.close

# Akin to input() on normal python
# Will open a UDP socket and wait for a packet
# Will keep code from running 
def receive():
    data = 'print("oopsydaisy")'
    global client_ip
    global port
    global server_ip
    global timeout
    print('Use like urepl.receive(server_ip,port)')
    r = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.bind((server_ip,port))
    r.settimeout(15)
    print(f'waiting to receive on {server_ip}:{port}')
    try:
        data,addr = r.recvfrom(1024)
        client_ip = addr[0]
    except:
        print('timeout exceeded or recvfrom err')
        r.close()
    r.close()
    return data

def printdetails():
    global ssid
    global server_ip
    global password
    global client_ip
    global port
    global timeout
    global connection_type
    print(f'connection_type: {connection_type}')
    print(f'ssid: {ssid}')
    print(f'server_ip: {server_ip}')
    print(f'client_ip: {client_ip}')
    print(f'port: {port}')
    print(f'timeout: {timeout}')
    
def set_client_ip(client):
    global client_ip
    client_ip = client
    print(f'You set the client_ip to: {client_ip}')
    printdetails()

def set_port(p):
    global port
    port = p
    print(f'You set the port to: {port}')
    printdetails()

def set_timeout(t):
    global timeout
    timeout = t
    print(f'You set the timeout to: {timeout}')
    printdetails()

def start():
    end_session = False
    while not end_session:
        reply = receive()
        frint.frint(exec(reply))
        send(bytes(str(frint.getram()),'utf-8'))
        if reply == b'stop':
            end_session = True
    

print('--urepl--')