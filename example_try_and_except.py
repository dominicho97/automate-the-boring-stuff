#def div42by(divideBy) :
#    try:
 #      return 42/ divideBy
  #  except ZeroDivisionError:
       # print('Error, you tried to divide by 0')
#print(div42by(2))
#print(div42by(12))
#print(div42by(0))
#print(div42by(1))

#You can not divide by 0 so you get an error.
       #Use try and except to pass the error.


print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
            print('that is a lot of cats')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')


#In the code above the input allowed to also enter words.
    #using try and except you can negate the error from entering words.
