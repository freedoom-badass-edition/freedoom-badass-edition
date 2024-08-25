# OUTDATED - Arguments: wadinfo name (no extension, but the file has to be .txt)
# Made by rostuhan
import os, shutil, sys, re
from omg import *
if os.path.exists("Build"):
    shutil.rmtree("Build")
os.mkdir("Build")
for Dir in ["graphics", "levels", "lumps", "musics", "sounds", "sprites"]:
    os.mkdir(os.path.join("Build", Dir))
    for f in os.listdir(Dir):
        f = Dir + "/" + f
        if os.path.isfile(f):
            if not f.split(".")[-1] == "mp3":
                shutil.copy(f, os.path.join("Build", f))
            else:
                shutil.copy(f, os.path.join("Build", "{}.mid".format(f.split(".")[0]))) # Gaslighting DeuTex
for Map in os.listdir("Build/levels"):
    Map = os.path.join("Build/levels/", Map)
    os.rename(Map, re.sub("badass(.*)", r"map\1", Map)) # Some regex magic
with open("wadinfo.txt", "r") as wadinfo:
    with open("Build/wadinfo.txt", "w") as buildwadinfo:
        buildwadinfo.write(re.sub("BADASS(.*)", r"MAP\1", wadinfo.read())) # Even more regex magic
        wadinfo.close()
        buildwadinfo.close()
for f in os.listdir("lumps/classes"):
    f = "lumps/classes/" + f
    with open(f, "r") as f:
        with open("Build/lumps/decorate.lmp", "a") as dec:
            dec.write("\n\n" + f.read())
            dec.close()
    f.close()
shutil.copy("IWAD.wad", "Build/doom2.wad")
os.chdir("Build")
os.system("deutex -rate accept -doom2 doom2.wad -build wadinfo.txt ../freedoom_badass_edition.wad")
os.chdir('..')
shutil.rmtree("Build")
ThisWAD = WAD()
ThisWAD.from_file("freedoom_badass_edition.wad")
# Gaslighting DeuTex again
for Map in ThisWAD.maps:
    ThisWAD.maps.rename(Map, re.sub("MAP(.*)", r"BADASS\1", Map))
for Map in ThisWAD.glmaps:
    ThisWAD.glmaps.rename(Map, re.sub("MAP(.*)", r"BADASS\1", Map))
for Map in ThisWAD.udmfmaps.find("*"): # Had to add a pattern for some reason?
    ThisWAD.udmfmaps.rename(Map, re.sub("MAP(.*)", r"BADASS\1", Map))
ThisWAD.to_file("freedoom_badass_edition.wad")