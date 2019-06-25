from pydub import AudioSegment
from pydub.playback import play
import os

class Alarm:
    def __init__(self, path, alarm_config=None):
        '''
        Constructor
        '''
        # set directory of audio file
        if alarm_config and alarm_config['alarm_audio_path']:
             self.alarm_audio_path = alarm_config['alarm_audio_path']
        else:
            self.alarm_audio_path = path + "/alarm_audio/school_bell_1.wav"

    def ring(self):
        '''
        play an alarm sound
        '''
        print(self.alarm_audio_path)
        alarm = AudioSegment.from_wav(self.alarm_audio_path)
        play(alarm)

def ding():
    # alarm_config = Alarm.load_config()
    # alarm = Alarm(alarm_config)
    # get the dirname of the absolute path
    alarm = Alarm(path=os.path.dirname(os.path.abspath(__file__)))
    alarm.ring()

if __name__ == "__main__":
    ding()

