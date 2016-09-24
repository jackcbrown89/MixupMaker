from pydub import AudioSegment
from pydub import effects


def segmentAud(track, track2):
    song = AudioSegment.from_mp3("%s.mp3" % track)
    song2 = AudioSegment.from_mp3("%s.mp3" % track2)
    trans = AudioSegment.from_mp3("spacewhoosh.mp3")
    song = song[:-10000]
    songfade = song.fade_out(2000)

    song2fade = song2.fade_in(2000)
    ftrack = songfade + trans + song2fade

    ftrack.export("mashup.mp3", format="mp3")

segmentAud("Big City Life", "440HZ")