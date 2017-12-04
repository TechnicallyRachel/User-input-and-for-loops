a = int(input("Type in the value of your first car: "))
b = int(input("Type in the value of your current car: "))
if a < b:
    print "Niiiiiiice dude, I bet that was a heck of an upgrade!"
    #print "{} is less than {}".format(a, b)
elif a == b:
    print "Hang in there, one day you'll get a helicopter!"
    #print "{} is equal to {}".format(a, b)
else:
    print "I'm sorry for your loss, man."
    #print "{} is greater that {}".format(a, b)

c = int(input("Type in the value of your dream car: "))

if c < b:
    print "What are you waiting for broseph? Drive your dream!"
elif c == b:
    print "Eh, keep an eye out, you can totally find a good deal for your trade-in!"
else:
    print "A man's reach must exceed his grasp, dude. One day you'll drive your dream, Top Gear!"
    
