import urllib2

def DL(URL, name):
    rawData = urllib2.urlopen(URL)
    reading = rawData.read()
    f = open('%s.mp3'%name, 'w+')
    f.write(reading)
    f.close()

    return reading


DL("http://sbist.yt-downloader.org/download.php?id=eb68c3a9a6449e70f57814fd853d0981", "audio2")
print('done')