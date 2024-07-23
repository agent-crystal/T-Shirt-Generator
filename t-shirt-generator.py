from PIL import Image, ImageDraw,ImageFont
import random

shirtpic = Image.open('whiteshirt.png')
shirt = ImageDraw.Draw(shirtpic)

quotes = [
    " Yeehaw ",
    "Sunny Side up",
    "Never Gonna Give \n You Up",
    "Monday Blues ",
    "Out of this \n World",
    "May the force \n be with you"
]

pictures = [
     Image.open('img1.png'),
     Image.open('img2.png'),
     Image.open('img3.png'),
     Image.open('img4.png'),
     Image.open('img5.png'),
]

rand_quote = random.choice(list(quotes))
rand_picture = random.choice(list(pictures))

font = ImageFont.truetype('arial.ttf', size=42)

shirtpic.paste(rand_picture,(300,425))
shirt.text((380,250),rand_quote, fill=(0, 0, 0),font=font)

shirtpic.show()
shirtpic.save('output_image.png')
print("Image saved as 'output_image.png'.")
