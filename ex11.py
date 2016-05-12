print "How old are you?",
age = raw_input()
print u'\033[31m'
print "How tall are you?",
height = raw_input()
print u'\033[31m'
print "How much do you weigh?",
weight = raw_input()
print u'\033[31m'


print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)