x = "There are %d type of people."%10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s."%(binary,do_not) #字符串包含字符串1

print x
print y

print "I said: %r."%x                                     #字符串包含字符串2
print "I also said: '%s'."%y                              #字符串包含字符串3

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"         #字符串包含字符串4
print joke_evaluation % hilarious

w = "This is the left sade of..."
e = "a string with a right side."
print w+e
