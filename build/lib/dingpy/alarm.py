from pydub import AudioSegment
from pydub.playback import play

import os

class Alarm:
    def __init__(self, path, alarm_config=None):
        '''
        Constructor
        '''
        if alarm_config and alarm_config['alarm_audio_path']:
             self.alarm_audio_path = alarm_config['alarm_audio_path']
        else:
            self.alarm_audio_path = path + "/alarm_audio/school_bell_1.wav"

    # def load_config(self=None, config_file_name="/.dingpy.conf"):
    #     config = {}
    #     config_file_path = os.getcwd() + config_file_name
    #     with open(config_file_path) as config_file:
    #         config = json.load(config_file)
    #         return config

    def ring(self):
        '''
        play an alarm sound
        '''
        print(self.alarm_audio_path)
        alarm = AudioSegment.from_wav(self.alarm_audio_path)
        play(alarm)
