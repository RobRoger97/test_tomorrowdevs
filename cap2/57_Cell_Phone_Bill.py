#Data
Max_min=50
Max_SMS=50
Month_price_base=15.00
Cost_Min_Extra=0.25
Cost_SMS_Extra=0.15
Additional_Charge_911=0.44
Percent_Tax_TOT=5/100

#Read sms and minutes from user
mn=int(input("Enter the number of minutes used in the last month: "))
sms=int(input("Enter the number of sms used in the last month: "))

#Loop to find out if the extra fee is there or not
if mn>Max_min or sms>Max_SMS:
    Extra_Fee=True
    minExtra=mn-Max_min
    smsExtra=sms-Max_SMS
else:
    Extra_Fee=False

#loop based on the presence of the extra fee
if Extra_Fee==False:
    Tot_price=Month_price_base+Additional_Charge_911
    print("SUBTotal                 %6.2f" % Tot_price)
    tax=Tot_price*(Percent_Tax_TOT)
    Tot_price=Tot_price+tax
    print("BASE FEE                 %6.2f" % Month_price_base)
    print("ADDITIONAL CHARGE 911V   %6.2f" % Additional_Charge_911)
    print("TAX 5 percent            %6.2f" % tax)
    print("Total                    %6.2f" % Tot_price)
elif Extra_Fee==True:
    Extra_price_Min=minExtra*Cost_Min_Extra
    if Extra_price_Min<=0:
        Extra_price_Min=0
        minExtra=0
    Extra_price_SMS=smsExtra*Cost_SMS_Extra
    if Extra_price_SMS<=0:
        Extra_price_SMS=0
        smsExtra=0
    Tot_price = Month_price_base + Additional_Charge_911 + Extra_price_Min + Extra_price_SMS
    tax = Tot_price * (Percent_Tax_TOT)
    print("SUBTotal              %6.2f" % Tot_price)
    Tot_price = Tot_price + tax
    print("BASE FEE              %6.2f" % Month_price_base)
    print("EXTRA MINUTES         %6.2f" % Extra_price_Min, "WHERE EXTRA MINUTES ARE %3d" % minExtra, "(Cost/min)",Cost_Min_Extra)
    print("EXTRA SMS             %6.2f" % Extra_price_SMS, "WHERE EXTRA SMS ARE     %3d" % smsExtra, "(Cost/sms)",Cost_SMS_Extra)
    print("ADDITIONAL CHARGE 911 %6.2f" % Additional_Charge_911)
    print("TAX 5 percent         %6.2f" % tax)
    print("Total                 %6.2f" % Tot_price)