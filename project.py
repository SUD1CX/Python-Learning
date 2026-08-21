# price=1000000
# x=input('Do you have a good cedit? (yes/no): ')
# x=x.lower()
# has_good_creddit=x
# if has_good_creddit=='yes':
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# income=input('Do you have a good income? (yes/no): ')
# income=income.lower()
# if income=='yes' and has_good_creddit=='yes':
#     print('You are eligible for a loan!')
# else:
#     print('Sorry, you are inelegible for a loan.')
# print(f'Down Payment: ${down_payment}')
# print('''Thank you!
# Coustomer Support''')



# temperature=input('What is the temperature today? ')
# x=int(temperature)
# if x>30:
#     print("It's a hot day.")
# elif x<10:
#     print("It's cold today.")
# else:
#     print("It's neither hot or cold.")



# name=input('Enter your name: ')
# x=len(name)
# if x<3:
#     print('Name must be atleast 3 characters long.')
# elif x>50:
#     print('Name can be a maximum of 50 characters.')
# else:
#     print('Name looks Good!')



# import random
# guess_number=random.randint(0,100)
# i=1
# while i<=3:
#     x=int(input('Guess the number: '))
#     i=i+1
#     if guess_number==x:
#         print('Congratulations! You guessed the correct number.')
#         print('Game Over')
#         break
#     else:
#         print('Wrong number.')
# if i==4:
#     print('''Sorry,you failed,
#    Game Over''')
#     print(f'The correct number was {guess_number}')



# command=""
# started=False
# while command != "/quit":
#     command=input("->").lower()
#     if command=="/start":
#         if started:
#             print('Car has already stared.')
#         else:
#             started=True
#             print('Car started...')
#     elif command=="/stop":
#         if not started:
#             print('The car has already stopped')
#         else:
#             started=False
#             print('Car stopped')
#     elif command=="/help":
#         print("Type '/start' to start the car\nType '/stop' to stop the car\nType'/quit' to quit the game")
#     elif command=="/quit":
#         print('Game exited sucessfully.')
#         break
#     else:
#         print('Invalid Command')




# price= [10,20,30]
# total=0
# for item in price:
#     total+=item
# print(f'Total price: {total}')



# numbers=[5,2,5,2,2]
# for cross in numbers:
#     print('X'*cross)

# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     output=""
#     for count in range(x_count):
#         output+='X'
#     print(output)



# list=[5,7,22,5, 25, 18, 52,75,69,96,7,1,8]
# max=list[0]
# for greatest_number in list:
#     if max<greatest_number:
#         max=greatest_number
# print(max)



# numbers=[2, 2, 4, 6, 3, 4, 6, 1]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)



# phone=input('Phone Number: ')
# digit_mappings={
#     "0" : "Zero",
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five",
#     "6" : "Six",
#     "7" : "Seven",
#     "8" : "Eight",
#     "9" : "Nine",
# }
# output=""
# for ch in phone:
#     print(ch)
#     output+=digit_mappings.get(ch, "!") + (" ")
# print(output)
    #! Here the phone number is a string so phython can itrate over each character from the string seperately



    # message=input('->')
# words=message.split(' ')
# emoji={
#     ":)" : "🙂",
#     ":(" : "🙁",
#     ":/" : "😕",
#     ":D" : "😀",
#     ":<" : "😡",
#     ":>" : "😊",
#     ">_<" : "🥰",
#     ";_;" : "😫"
# }
# output=""
# for word in words:
#     output+=emoji.get(word, word) + (' ')
# print(output)


# try:
#     age=int(input('Age:'))
#     income=20000
#     risk=income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be zero')
# except ValueError:
#     print('Invalid Value')



class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
point1=Point(10, 20)
print(point1.x)
    #! A class is a reusable template or blueprint used to build objects, which are distinct instances encapsulating both data (attributes) and behaviors (methods).
    