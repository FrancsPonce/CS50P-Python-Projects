def main():


    #Working input
    time_input=input("What time is it? ")
    time_convert= convert(time_input)
    time_round= round(time_convert,1)
    #print (time_round)


    #Workin Lists
    list_breakfast= [7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8]
    list_lunch= [12.0, 12.1,12.2,12.3,12.4,12.5,12.6,12.7,12.8,12.9,13]
    list_dinner= [18.0, 18.1,18.2,18.3,18.4,18.5,18.6,18.7,18.8,18.9,19]


    #If functions
    if time_round in list_breakfast:
        print ("breakfast time")
    elif time_round in list_lunch:
        print("lunch time")
    elif time_round in list_dinner:
        print("dinner time")
    else:
        print("Dont eat nothing :3")



def convert(time):
    hours, minutes = time.split(":")
    hours= int(hours)
    minutes= int(minutes)
    minutes_convert= (minutes/60)
    time_convert= hours+minutes_convert
    #print (time_convert)
    return time_convert



if __name__ == "__main__":
    main()
