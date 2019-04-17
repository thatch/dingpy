from .Alarm import Alarm
import os

def main():
    # alarm_config = Alarm.load_config()
    # alarm = Alarm(alarm_config)
    alarm = Alarm(path=os.path.dirname(__file__))
    alarm.ring()

if __name__ == "__main__":
    main()

