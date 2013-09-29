import urllib2
from bs4 import BeautifulSoup

def generateAudio(lyrics):
    '''Takes in the lyrics. Returns a URL to the autotuned mp3 (no backing).'''

    s = lyrics.replace (" ", "+")


    tts_url = "http://tts-api.com/tts.mp3?q=%s&return_url=1" % s
    tts = urllib2.urlopen(tts_url)
    
    soup = BeautifulSoup(tts)
    input_file = soup.get_text()

    access_id = "78908f19-88ab-4e11-ab95-ac47aecd8458"

    midi_pitches = "58-58-58-58-58-58-57-57-53-57-55-53-58-57-57-53-57-55-" \
        "53-58-57-57-53-53-57-55-55-53-57-55-53-58-53-53-53-57-55-55-53-58-..."


    sonic_url = "https://api.sonicapi.com/process/elastiqueTune" \
        "?access_id=%s" \
        "&input_file=%s" \
        "&tempo_factor=0.7" \
        "&pitchcorrection_percent=90" \
        "&pitchdrift_percent=80" \
        "&midi_pitches=%s" % (access_id, input_file, midi_pitches) 

    #print sonic_url
    '''
    req2 = urllib2.Request(sonic_url)
    response = urllib2.urlopen(req2)
    mp3 = response.read()
    #print len(mp3)
    '''
    
    return sonic_url

if __name__=='__main__':
    lyrics = "This+won't+work+if+there+are+spaces+in+the+url+you+provide."
    lyrics2 = "I came in like a wrecking ball. I never hit so hard in love. All I wanted was to break your walls. All you ever did was wreck me. Yeah, you, you wreck me."

    generateAudio(lyrics2)
    
