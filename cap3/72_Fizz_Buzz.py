#The first numbers in the Fizz-Buzz game
Num = 100

#For loop :
#The starting player begins by saying one, and then play passes to the player to the left.
#Each subsequent player is responsible for the next integer in sequence before play passes to the following player. 
#On a player’s turn they must either say their number or one of following substitutions:
# • If the player’s number is divisible by 3 then the player says fizz instead of their number.
# • If the player’s number is divisible by 5 then the player says buzz instead of their number.
#A player must say both fizz and buzz for numbers that are divisible by both 3 and 5.
for i in range(1,Num+1,1):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("Fizz-Buzz")
    else:
        print(i)