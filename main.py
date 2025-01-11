import psutil
import time
from pygame import mixer

TARGET_APP = "code" # Name of the program to monitor
BREAK_TIME = 3600
MUSIC_FILE = "music/Jam.mp3" # Path to music file

def is_program_running(program_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == program_name:
            return True
    return False

def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

def main():
    print(f"Monitoring if '{TARGET_APP}' is running...")
    time_open = 0
    while True:
        if is_program_running(TARGET_APP):
            print(f"{TARGET_APP} is running... Time open: {time_open} seconds")
            time.sleep(1)
            time_open += 1
            if time_open >= BREAK_TIME:
                print("Time to take a break!")
                play_music(MUSIC_FILE)
                time_open = 0
        else:
            print(f"{TARGET_APP} is not running.")
            time_open = 0
            time.sleep(5)

if __name__ =="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Goodbye!")