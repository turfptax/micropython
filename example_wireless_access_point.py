print('starting PR2040 pico W')

import urepl


def somefunction(data):
    urepl.frint(data)
    return 'you printed to the repl environment standard output'


# Setup as Wireless Access POint
# if you don't specify a password/ssid it will use the defaul in urepl.py
wap = urepl.wap('SSIDname','WIFIpassword')

# print the network details
urepl.printdetails()

# setup to receive a packet and also get the senders address
reply = urepl.receive()

# Now that we have the senders address send something back
text = b'This is the return message'
urepl.send(text)

# start a repl loop will continue until receive 'stop' from client
#urepl.start()

#grab the last urepl.frint printing

#set the port
urepl.set_port(1234)

# Set receive timeout value in seconds
urepl.set_timeout(10)

# Set the client Ip Address manually
urepl.set_client_ip("172.16.1.2")

# send an output the the repl environment
urepl.frint('this is a message for urepl')

# get the last output of the repl environment
print(urepl.getbuff())






