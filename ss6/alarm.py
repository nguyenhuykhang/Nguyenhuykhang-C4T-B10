import datetime
import pyglet
datetime.datetime.now()


print('bay gio la {}'.format(datetime.datetime.now().strftime("%H.%M")))
alarmclock = input('Gio ban muon hen:')

while True:
    currenthour = datetime.datetime.now().strftime("%H.%M")

    if alarmclock == currenthour:

         

        music = pyglet.resource.media('crowd-cheering.mp3')
        music.play()

        pyglet.app.run()