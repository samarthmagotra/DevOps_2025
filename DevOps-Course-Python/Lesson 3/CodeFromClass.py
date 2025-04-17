# Write a programme that gets a name as input and append it to a file called names.txt
for i in range(3):
    name = input(f'Enter the name number {i+1}:')
    with open('name.txt','a') as file:
        file.seek(i)
        file.write(name+'\n')

with open('name.txt','r') as f:
    content = f.read()
    print(content)
    print(type(content))
    lst = content.split()

for i in range(3):
    print('Welcome ' + lst[i])

# Write a programme that reads all of the names from a file called names.txt and greets each name

# Call the first programme three times with different names and run the second program

