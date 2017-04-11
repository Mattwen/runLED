from flask import Flask, render_template, request, flash
import datetime
import RPi.GPIO as GPIO
from flask_socketio import SocketIO
app = Flask(__name__)
from PIL import Image, ImageDraw, ImageFont

import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix

from forms import TextEntryForm

# new matrix for 2 panels daisy chained
matrix = Adafruit_RGBmatrix(16, 2)
app.secret_key = 'gngrger4t34t34terfgsdsd234'

# New image for 64 x 16 display canvas
image = Image.new("1", (64, 16))
image = image.convert("RGBA")
draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
font = ImageFont.truetype("slkscr.ttf", 8)

# mattpi.com/message/
@app.route("/message/", methods=['GET', 'POST'])
def message():
    form = TextEntryForm(request.form)

    if request.method == 'POST' and form.validate():

        # Text Display
        print 'success'
        word=request.form['word']

        # Color Display RGB
        r = int(request.form['r'])
        g = int(request.form['g'])
        b = int(request.form['b'])

        matrix.Clear()

        # init so it repaints on new post
        image = Image.new("1", (64, 16))
        image = image.convert("RGBA")
        draw = ImageDraw.Draw(image)

        # If the text is longer than 12 characters - make two lines
        if len(word) >= 12:

            # word can also be a sentence, split text into two secontion
            word = word.split()
            firstpart, secondpart = word[:len(word)/2], word[len(word)/2:]

            # set second and first part
            firstpart = ' '.join(firstpart)
            secondpart = ' '.join(secondpart)

            # Draw both parts
            draw.text((0, 0, 0, 0), firstpart, font=font, fill=(r,g,b,255))
            draw.text((0, 8, 0, 0), secondpart, font=font, fill=(r,g,b,255))

        # Draw the image normally
        else:
            draw.text((0, 0, 0, 0), word, font=font, fill=(r,g,b,255))

        # Set the image
        matrix.SetImage(image.im.id, 0, 0)
    else:
       print 'failure'
    # Return the same view
    return render_template('text.html', form=form)

# Remove these later
@app.route("/orange/") # mattpi.com/orange/
def drawOrange():

    matrix.Fill(0xff751a)
    return render_template('control.html')

@app.route("/blue/") # mattpi.com/blue/
def drawBlue():

   matrix.Fill(0x3399ff)
   return render_template('control.html')

@app.route("/red/") # mattpi.com/red/
def drawRed():

   matrix.Fill(0xFF0000)
   return render_template('control.html')

@app.route("/green/")
def drawGreen():

   matrix.Fill(0x009900)
   return render_template('control.html')

@app.route("/")
def drawControl():
   return render_template('control.html')

@app.route("/pi/")
def drawTable():
   return render_template('pi.html')

@app.route("/stop/")
def stopRun():
   matrix.Clear()
   return render_template('control.html')

# Runs on port 5000 - shitty temporary flask server - replace with nginx
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
