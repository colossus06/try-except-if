print("This is a simple number checker program")
answer = input("Enter an number: ")
try:
    ianswer= int(answer)
except:
    ianswer = -1
if ianswer > 0:
    print("Yes this is a number: ", ianswer)
else:
    print("Nope, this is not a number: ", answer)


#converting user input

'''
input is always string you  should convert it 
to int. using type conversion

input=int(input("Enter a number: "))

'''