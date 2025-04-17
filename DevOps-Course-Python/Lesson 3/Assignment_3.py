#1 + 2
if __name__ == '__main__':
    try:
        a = 1 / 0
    except ZeroDivisionError:
        print("Division by zero")


#3. Is the following code legal? - Yes
try:
    x = 1
finally:
    print("finally")

#4
#Except handles all types of exceptions

# 6
# Except IOError - handles I/O (input/output) exceptions
# Except ZeroDivisionError - handles division by zero

#7. Create a text file named “words.txt” programmatically
#8. Write your name into the file
with open('words.txt','w+') as f:
    f.write('Hi,, this is a test\n')
    f.write('My name is Samarth')
    f.close()

#9 Read your file content and print it
with open('words.txt', 'r') as f:
    content = f.read()
    print(content)
    f.close()

#10 Write Hebrew content into your text file and print its content programmatically.
with open("hebrew.txt",'w',encoding='utf-8') as my_file:
    my_file.write("שלום")
    my_file.close()

#12. Create an image from code (png file) Hint: use Pillow
from PIL import Image, ImageDraw, ImageFont

# Step 1: Create a blank image (RGB mode)
width, height = 400, 200
image = Image.new("RGB", (width, height), color="white")

# Step 2: Initialize the drawing context
draw = ImageDraw.Draw(image)

# Step 3: Add shapes and text
# Draw a rectangle
draw.rectangle((50, 50, 350, 150), outline="black", fill="lightblue")

# Add text (you can specify a font path for custom fonts)
font = ImageFont.load_default()
text = "Hello, Pillow!"
#text_width, text_height = draw.textbbox(text, font=font)
text_position = ((width - 20) // 2, (height - 20) // 2)
draw.text(text_position, text, fill="darkblue", font=font)

# Step 4: Save the image as a PNG file
image.save("example_image.png")

print("Image created and saved as example_image.png")

