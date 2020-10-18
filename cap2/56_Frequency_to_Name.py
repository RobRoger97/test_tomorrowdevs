#Read the frequency of some radiation from the user
frequency = float(input("Enter a frequency of a some radiation: "))

#Categories according to its frequency
if frequency<3e9:
    name = "Radio Wavs"
elif frequency>=3e9 and frequency<3e12:
    name = "Microwaves"
elif frequency>=3e12 and frequency<4.3e14:
    name = "Infrared Light"
elif frequency>=4.3e14 and frequency<7.5e14:
    name = "Visible Light"
elif frequency>=7.5e14 and frequency<3e17:
    name = "Ultraviolet Light"
elif frequency>=3e17 and frequency<3e19:
    name = "X-Rays"
elif frequency>=3e19:
    name = "Gamma Rays"

#Display the result
print ("The appropriate name of that frequency %d is %s" %(frequency,name))