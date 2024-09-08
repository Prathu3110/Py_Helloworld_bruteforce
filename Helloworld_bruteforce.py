import string,random,time

letters = string.ascii_letters
result = "HelloWorld"

output = ""

for letter in result:
    while True:
        randoml = random.choice(letters)
        print(output + randoml, end='\r')  
        if randoml == letter:
            output += randoml
            break
        time.sleep(0.01)

print("\nCompleted:", output)
