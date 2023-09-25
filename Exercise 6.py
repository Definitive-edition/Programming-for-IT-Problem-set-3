def computepay(hoursworked, payrate):
    #Variables
    totalpay = 0
    regularhours = 0
    overtimehours = 0
    regulartimelimit = 40
    regularpay = 0
    overtimepay = 0
    time_half = 1.5
    
    
    #If statement
    if hoursworked > regulartimelimit:
        regularhours = regulartimelimit
        overtimehours = hoursworked - Regulartimelimit
        
    else:
        regularhours = hoursworked
        overtimehours = 0
        
    regular = regularhours * payrate
    overtimepay = overtimehours * payrate * time_half
    
    totalpay = regularpay + overtimepay
    return totalpay
#Calling the function
print (computepay(52, 20))
    