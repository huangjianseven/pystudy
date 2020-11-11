score = input("Enter your score:")



try:
    score = float(score)

    if(score>1 or score<0):
    	# print("Please input correctly(0~1.0)!")
    	exit()


    if score >= 0.9:
    	grade = 'A'
    elif score >= 0.8:
    	grade = 'B'
    elif score >= 0.7:
    	grade = 'C'
    elif score >= 0.6:
    	grade = 'D'
    elif score < 0.6:
    	grade = 'F'
    print(grade)


except:
	print("Please input correctly(0~1.0)!")
    

    
