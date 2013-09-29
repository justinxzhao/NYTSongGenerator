NYTSongGenerator / Tuning the Times
================

Generate a song and lyrics from New York Times published articles! Authored by Lisa Li, Michael Saltzman, Justin Zhao

# About
* Python Flask Framework
* Homemade rhyming dictionaries were built with the help of cmudict (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
* User specifies a topic and a background song and the New York Times Semantic API (http://developer.nytimes.com/docs) returns a list of all the most recent/relevant articles.
* Titles from the first 10 pages of these files are used to generate the lyrics for the song.
* The lyrics can be read by a robotic voice (http://tts-api.com/) that has been autotuned (http://www.sonicapi.com/)
* Rhyming Scheme of all lyrics is AABBCCDDEE, etc, though this functionality might be extended in the future

Hacked for Hack NY 2013
