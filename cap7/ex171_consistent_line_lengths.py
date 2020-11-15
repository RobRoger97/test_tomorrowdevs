# Max line 
max_line = 50
File = "C:/Users/Roberta/Desktop/Python/Alice.txt"
# Open the file to read
inf = open(File,'r')
lis = [] # empty list
for line in inf: # read each line of the file
    line = line.strip()
    for word in line.split():
        lis.append(word)# inserts each word into the list
    s=''
    lun = 0
    for l in lis:
        if line == '': # if the line is empty (new paragraph) NON FUNZIONA!
            s+='\n'+l+' '
            lun = len(l)+1
        lun+= len(l)+1
        if lun>max_line : # if the sum of the rows exceeds the maximum
            s+='\n'+l+' '
            lun = len(l)+1
        elif lun <= max_line:
            s+=l+' '
# Close the file
inf.close()
# Display the result
print(s)