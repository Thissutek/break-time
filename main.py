import psutil
import time
import os
import random
from pygame import mixer

TARGET_APP = "code" # Name of the program to monitor
BREAK_TIME = 5
MUSIC_FILE = "music/Jam.mp3" # Path to music file
MUSIC_FOLDER = './music'

def is_program_running(program_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == program_name:
            return True
    return False

def get_music_files():
    files = os.listdir(MUSIC_FOLDER)
    music_files = [file for file in files if file.endswith('.mp3')]
    return music_files

def play_music():
    music_files = get_music_files()
    if not music_files:
        print(f"No music files found in the folder!")
        return

    random_music = random.choice(music_files)
    music_path = os.path.join(MUSIC_FOLDER, random_music)

    mixer.init()
    mixer.music.load(music_path)
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
                play_music()
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