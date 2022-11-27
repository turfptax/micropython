import urepl

print('You have entered the urepl boot file thingie')

wap = urepl.wap()

# wait for the packet from the client to set the outbound ip
reply = urepl.receive()

# Start the urepl sessions
urepl.start()