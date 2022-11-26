print('starting PR2040 pico W')

import urepl

# Setup as wireless access point
wap = urepl.wap()

# print the network details
urepl.printdetails()

# setup to receive a packet and also get the senders address
reply = urepl.receive()

# Now that we have the senders address send something back
text = b'This is the return message'
urepl.send(text)

# start a repl loop will continue until receive 'stop' from client
urepl.start()

