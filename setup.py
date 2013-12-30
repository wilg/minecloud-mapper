from subprocess import call
import urllib


print("-----> [minecloud-mapper/setup.py] Cloning overviewer")
call(["git", "clone", "--depth=1", "https://github.com/overviewer/Minecraft-Overviewer.git", "overviewer"])


print("-----> [minecloud-mapper/setup.py] Downloading headers")

urllib.urlretrieve('http://hg.effbot.org/pil-117/raw/f356a1f64271/libImaging/Imaging.h', 'overviewer/Imaging.h')
urllib.urlretrieve('http://hg.effbot.org/pil-117/raw/f356a1f64271/libImaging/ImPlatform.h', 'overviewer/ImPlatform.h')

print("-----> [minecloud-mapper/setup.py] Building overviewer from source")

call(["python", "overviewer/setup.py", "build"])
