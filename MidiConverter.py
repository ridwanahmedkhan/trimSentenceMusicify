#Import the library
from midiutil.MidiFile import MIDIFile
import os

class MidiConverter:
	
	def stringToMidiConverter(self, musicString):  
		#musicString = 'Mind Music Machine Lab'
		countChars = len(musicString)

		print "The lenght of the musicString is %d" % (countChars)

		musicMIDI = MIDIFile(countChars)
		duration = 1
		volume = 100
		track = 0
		time = 0


		for ch in musicString:	
			musicMIDI.addTempo(track,time, 120)
			channel = (time%15)
			pitch = ord(ch)	
			musicMIDI.addNote(track,channel,pitch,time,duration,volume)
			track += 1
			time +=1

		midiFilename = "tweet.mid"
		binfile = open(midiFilename, 'wb')
		musicMIDI.writeFile(binfile)
		binfile.close()

		os.system('timidity '+ midiFilename)
