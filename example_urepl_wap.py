import urepl

print('You have entered the urepl boot file thingie')


# Start wireless access point
wap = urepl.wap()
urepl.printdetails()

# wait for the packet from the client to set the outbound ip
reply = urepl.receive()

# Start the urepl sessions
urepl.start()