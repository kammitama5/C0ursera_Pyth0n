def greet(friend, money):
  if friend and (money > 20):
    print "Hi!"
    money = money - 20
  elif friend:
    print "Hiya"
  else:
    print "I'm mean"
    money = money + 10
  return money
  
  
money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money 
print ""

money = greet(True, money)
print "Money:", money 
print ""