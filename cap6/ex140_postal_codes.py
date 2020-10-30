code = input("Enter a postal code: ").upper()

lis = list(code)

dic = {'Newfoundland':'A','Nova Scotia':'B','Prince Edward Island':'C','New Brunswick':'E',\
    'Quebec':['G','H','J'],'Ontario':['K','L','M','N','P'],'Manitoba':'R','Saskatchewan':'S',\
    'Alberta':'T','British Columbia':'V','Nunavut':'X','Northwest Territories':'X','Yukon':'Y'}

if len(code)<=6:
    if lis[0]=='D' or lis[0]=='F' or lis[0]=='I' or\
        lis[0]=='O' or lis[0]=='Q' or lis[0]=='U' or\
            lis[0]=='W' or lis[0]=='Z' or lis[0].isdigit or lis[1].isdigit()==False:
        print("Error message: That is not a right postal code")
    else:
        if lis[0] == 'X':
            result = 'Nunavut or Northwest'
        else:
            for d in dic:
                if lis[0]==dic[d]:
                    result = d
        if lis[1] == 0:
            address = 'rural'
        else:
            address = 'urban'

        print("The postal code",code,"is for a(an)",address,"address in",result)
else:
    print('This is not a right postal code!')


