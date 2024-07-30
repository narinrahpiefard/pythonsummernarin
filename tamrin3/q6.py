numbers=input("enter 5 numbers: ").split(",")
number_list=list(map(int,numbers))
number_sum=sum(number_list)
if number_sum%2==0:
    number2=eval(input("enter your new number: "))
    print(number_sum+number2)
else:
    print(numbers[0],numbers[1],numbers[3],numbers[4])