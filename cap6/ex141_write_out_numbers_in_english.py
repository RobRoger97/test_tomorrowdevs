dic = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
        10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16: "sixteen", 
        17:"seventeen",18:"eighteen",19: "nineteen",}
dic2 = {20:"twenty", 30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90: "ninety"}

def en_num(n):
    if n>=0 and n<=999:
        if n<20:
            return dic[n]
        if n<100:
            if n%10==0:
                return dic2[n]
            else:
                return dic2[(n//10)*10]+' '+dic[n%10]
        if n<=999:
            if n%100==0:
                return dic[n//100]+' '+'hundred'
            else:
                return dic[n//100]+' '+'hundred'+' '+en_num(n%100)
    else:
        return "This number is out of range"

def main():
    integer = int(input("Enter an integer: "))
    print("The English word of that number is: \n", en_num(integer))

main()