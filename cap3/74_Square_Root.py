#Read a number, x, entered by the user
x = int(input("Entered a number: "))

#Initialize
guess = x/2
print("Approximation:",guess)
error = abs((guess**2)-x)
print("Absolute error:",error)

#While loop:
#The quality of the approximation depends on how you define “good enough”. In the author’s solution, 
#guess was considered good enough when the absolute value of the difference between guess ∗ guess and x 
#was less than or equal to 10−12.
while error>(10**(-12)):
    guess=(guess+(x/guess))/2
    error=abs((guess**2)-x)
    print("Approximation:",guess)
    print("Absolute error:",error)
