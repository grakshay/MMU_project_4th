#import statements
from spy_details import spy_name, spy_age, spy_salutation, spy_rating
from start_chat import start_chat
print ("let's get started")
question = "do you want to continue as" + spy_salutation + " " + spy_name + " (Y/N) "
existing = raw_input(question)
#validating user input
if existing  == 'Y' or existing == 'y' :
    start_chat(spy_name,spy_age,spy_rating)
    #logic here
elif existing  == 'N' or existing == 'n' :
    #new users code here
    spy_name = raw_input("type your name here ")
    if len(spy_name) > 0:
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_salutation = raw_input("what should we call you ")
        spy_age = raw_input("what is your age  ")
        print type(spy_age)
        spy_age = float(int(spy_age))
        print type(spy_age)
        spy_name = spy_salutation + ' ' + spy_name
        print 'welcome ' + spy_name + " glad to have you back with us"
        print "alright " + spy_name + " i'd like to know more about you before we proceed further"
    else:
        print "invalid name....please try again"


else :
    print ("wrong choice....try again")

