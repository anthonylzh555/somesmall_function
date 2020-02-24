from deque_delta import MovingAverage

obj = MovingAverage(3)

while True:
    
    x=input("Please Enter the number：")   ###can be change into other data input
    print("Temperature : ", x)
    
    delta_t = round(obj.next(float(x)),2)
    prob = (delta_t / 5)*100  ### stardard temperature : 5 degree
    #print("Delta T : ", delta_t , "probability : ", prob, " %")
    
    s_curtain = 0
    
    while delta_t != 0 and float(delta_t) >= 0:
        if float(x) > 25:               ### Threshold of the temperature
            if prob > 50 :             ### When the heating rate is over
                
                s_curtain = 1
                print("Delta T : ", delta_t , "probability : ", prob, "%")
                print("Outdoor emperature rising !! ", s_curtain)
                
            elif float(x) > 35:       ### When the temperature is over 35 degree
                
                s_curtain = 1
                prob = 100
                print("Delta T : ", delta_t , "probability : ", prob, "%")
                print("Outdoor temperature is too high ", s_curtain)
                
            else:
                s_curtain = 0
                print("Delta T : ", delta_t , "probability : ", prob, "%")
                print("Sunny day @@ ", s_curtain)
                
        else :
           s_curtain = 0
           print("Delta T : ", delta_t , "probability : ", prob, "%")
           print("It's gonna be OK ", s_curtain)

        break
    else :
        if float(x) > 35:               ### Threshold of the temperature
            
            s_curtain = 1
            prob = 100
            print("Delta T : ", delta_t , "probability : ", prob, "%")
            print("Outdoor temperature is too high ", s_curtain )
                
        else :
           s_curtain = 0
           print("Delta T : ", delta_t , "probability : ", prob, "%")
           print("It's gonna be OK ", s_curtain)


