#Scan download folder and sort using python

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

user = os.environ['USERPROFILE']
source = user + "\\Downloads"
images = source + "\\images"
audio = source + "\\audio"
docs = source + "\\docs"
videos = source + "\\videos"
applications = source + "\\applications"
zips = source + "\\zips"

downloads = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

# Make Directories
def make_dirs():
    if(not os.path.exists(images)):
        os.makedirs(images)
    if(not os.path.exists(audio)):
        os.makedirs(audio)
    if(not os.path.exists(docs)):
        os.makedirs(docs)
    if(not os.path.exists(videos)):
        os.makedirs(videos)
    if(not os.path.exists(applications)):
        os.makedirs(applications)
    if(not os.path.exists(zips)):
        os.makedirs(zips)

# Move files
def move_files():
    for d in downloads:
        if d.endswith(".jpg") or d.endswith(".png") or d.endswith(".jpeg") or d.endswith(".tif") or d.endswith(".gif"):
            os.rename(source + "\\" + d, images + "\\" + d)
            print("Moved " + d + " to " + images)
        elif d.endswith(".mp3") or d.endswith(".wav") or d.endswith(".flac"):
            os.rename(source + "\\" + d, audio + "\\" + d)
            print("Moved " + d + " to " + audio)
        elif d.endswith(".pdf") or d.endswith(".doc") or d.endswith(".docx"):
            os.rename(source + "\\" + d, docs + "\\" + d)
            print("Moved " + d + " to " + docs)
        elif d.endswith(".mp4") or d.endswith(".avi") or d.endswith(".mkv"):
            os.rename(source + "\\" + d, videos + "\\" + d)
            print("Moved " + d + " to " + videos)
        elif d.endswith(".exe") or d.endswith(".msi"):
            os.rename(source + "\\" + d, applications + "\\" + d)
            print("Moved " + d + " to " + applications)
        elif d.endswith(".zip") or d.endswith(".rar"):
            os.rename(source + "\\" + d, zips + "\\" + d)
            print("Moved " + d + " to " + zips)
    
def main():
    make_dirs()
    move_files()
    print("Download directory sorted!")
    input("Press Enter to exit")
    
class Watcher:
    DIRECTORY_TO_WATCH = source
    
    def __init__(self):
        self.observer = Observer()
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()
    
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            main()
        elif event.event_type == 'modified':
            main()
    
if __name__ == "__main__":
    main()
    
