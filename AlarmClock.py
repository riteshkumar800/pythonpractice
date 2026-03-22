import time
import datetime
import pythonquizgame



def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file="my_music.mp3"
    is_running=True

    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm_time:
            print("WAKE UP!")

            pythonquizgame.mixer().init()
            pythonquizgame.mixer.music.load(sound_file)
            pythonquizgame.mixer.music.play()

            while pythonquizgame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

        time.sleep(1)





if __name__=="__main__":
    alarm_time=input("enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

