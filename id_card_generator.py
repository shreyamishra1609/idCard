import random
import os
import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont

import pandas as pd
import mysql.connector as sql

mycon= sql.connect(host= "localhost",user="root", passwd="hacker", database="idcard")
if mycon.is_connected():
    
    info=pd.read_sql("select * from idcardd;",mycon)
    print(info)

    rollnum=input("enter the roll no:")
    name="select Name from idcardd where Roll='%s';" %(rollnum,)
    df1=pd.read_sql(name,mycon[0])

    classStud="select Class from idcardd where Roll='%s';" %(rollnum,)
    df2=pd.read_sql(classStud,mycon)

    section="select Section from idcardd where Roll='%s';" %(rollnum,)
    df3=pd.read_sql(section,mycon)

    house="select House from idcardd where Roll='%s';" %(rollnum,)
    df4=pd.read_sql(house,mycon)

    address="select Address from idcardd where Roll='%s';" %(rollnum,)
    df5=pd.read_sql(address,mycon)

    contact="select Contact from idcardd where Roll='%s';" %(rollnum,)
    df6=pd.read_sql(contact,mycon)

    transport="select Transport from idcardd where Roll='%s';" %(rollnum,)
    df7=pd.read_sql(transport,mycon)

    print(df1)
    print(df2)
    print(df3)
    print(df4)
    print(df5)
    print(df6)
    print(df7)
   

else:
    print("error")




image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

os.system("Title: ID CARD Generator by Grasp Coding")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (50, 50)
#message = input('\nEnter Your School Name: ')
message ="Dehradun Public School"
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
#message = input('Enter Your Full Name: ')
message= df1
message = str('Name: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 350)
#message = input('Enter Your Gender: ')
message = df2
message = str('Gender: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (400, 350)
#message = int(input('Enter Your Age: '))
message = df3
message = str('Age: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 450)
#message = input('Enter Your Date Of Birth: ')
#message = int(input('Enter Your Age: '))
message = df4
message = str('Date of Birth: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
#message = input('Enter Your Blood Group: ')
message = df5
message = str('Blood Group: ' + str(message))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 650)
#message = int(input('Enter Your Mobile Number: '))
message = df6
message = str('Mobile Number: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 750)
#message = input('Enter Your Address: ')
message = df7
message = str('Address: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')

img = qrcode.make(str(company) + str(idno))  # this info. is added in QR code, also add other things
img.save(str(idno) + '.bmp')

til = Image.open(name + '.png')
im = Image.open(str(idno) + '.bmp')  # 25x25
til.paste(im, (650, 350))
til.save(name + '.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
input('\n\nPress any key to Close program...')
