from pydub import AudioSegment
from pydub.playback import play

class Alarm:
	def __init__(self):
		'''
		Constructor
		'''
		self.alarm_audio_path = "./alarm_audio/school_bell_1.wav"
		
	def ring_alarm(self):
		'''
		play an alarm sound
		'''
		alarm = AudioSegment.from_wav(self.alarm_audio_path)
		play(alarm)
