while(True):
    print("Press q to quit")
    a  = input("Enter a No. :")
    if a == 'q' :
        break
    else:
        try:
            a=int(a)
            if a > 6:
                print("The no. Entered Is Greater Than 6")
            else:
                print("The no. Entered Is Smaller Than 6")

                # it wont chrash the program it willl continue to go on
                #and ofcourse there are may dif errors
        except Exception as e :
            print(f"Please Enter a 'Number' Not '{a}'.")


print('Thanks For Playing This Game')
