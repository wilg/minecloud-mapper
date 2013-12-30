from subprocess import call
import urllib

print("-----> [minecloud-mapper/setup.py] Installing dependencies with pip")

call(["pip", "install", "numpy==1.8.0"])
call(["pip", "install", "Pillow==2.2.2"])
call(["pip", "install", "wsgiref==0.1.2"])
call(["pip", "install", "boto==2.21.0"])
call(["pip", "install", "boto-rsync==0.8.1"])

print("-----> [minecloud-mapper/setup.py] Cloning overviewer")
call(["git", "clone", "--depth=1", "https://github.com/overviewer/Minecraft-Overviewer.git", "overviewer"])


print("-----> [minecloud-mapper/setup.py] Downloading headers")

urllib.urlretrieve('http://hg.effbot.org/pil-117/raw/f356a1f64271/libImaging/Imaging.h', 'overviewer/Imaging.h')
urllib.urlretrieve('http://hg.effbot.org/pil-117/raw/f356a1f64271/libImaging/ImPlatform.h', 'overviewer/ImPlatform.h')

print("-----> [minecloud-mapper/setup.py] Building overviewer from source")

call(["python", "overviewer/setup.py", "build"])
