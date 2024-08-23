# Arguments: wadinfo name (no extension, but the file has to be .txt)
# Made by rostuhan
import os, shutil, sys
if os.path.exists("Build"):
    shutil.rmtree("Build")
os.mkdir("Build")
for Dir in ["graphics", "levels", "lumps", "musics", "sounds", "sprites"]:
    os.mkdir(os.path.join("Build", Dir))
    for f in os.listdir(Dir):
        f = os.path.join(Dir, f)
        if os.path.isfile(f):
            if not f.split(".")[-1] == "mp3":
                shutil.copy(f, os.path.join("Build", f))
            else:
                shutil.copy(f, os.path.join("Build", "{}.mid".format(f.split(".")[0]))) # gaslighting DeuTex
shutil.copy("{}.txt".format(sys.argv[1]), "Build/wadinfo.txt")
for f in os.listdir("lumps/classes"):
    f = os.path.join("lumps/classes", f)
    with open(f, "r") as f:
        with open("Build/lumps/decorate.lmp", "a") as dec:
            dec.write("\n\n" + f.read())
            dec.close()
    f.close()
shutil.copy("IWAD.wad", "Build/doom2.wad")
shutil.copy("deutex", "Build/deutex")
os.chdir("Build")
os.system("./deutex -rate accept -doom2 doom2.wad -build wadinfo.txt \"../freedoom_badass_edition.wad\"".format(sys.argv[1]))
os.chdir('..')
shutil.rmtree("Build")