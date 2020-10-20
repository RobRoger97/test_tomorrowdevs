or_price  = [ 4,95 , 9,95 , 14,95 , 19,95 , 24,95 ]
for  x  in  or_price :
    discount  =  round( x * 60 / 100 , 2 )
    new_price  =  round( x - discount , 2 )
    print("%5.2f    %5.2f    %5.2f"%(x , discount , new_price))