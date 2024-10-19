# from typing import Union, Literal
from modules.types import Metadata, Mod
import argparse
import os, sys, json

parser = argparse.ArgumentParser(description = "Yet Another MineCraft ModPack Downloader")
parser.add_argument("init", nargs = '?', type = bool,
                    help = "Init a new mod pack.")
args = parser.parse_args()

def initNewPack():
    modpackName: str = input("Enter mod pack name: ")
    if modpackName == "":
        print("Required a mod pack name!")
        sys.exit(1)

    modpackVersion: str = input("(optional) Enter mod pack version: ")
    if modpackVersion == "":
        modpackVersion = "1"

    modloaderType: str = input("Enter mod loader name: ")
    if modloaderType == "":
        print("Required a mod loader name!")
        sys.exit(1)

    modloaderVersion: str = input("(optional) Enter mod loader version: ")
    if modloaderVersion == "":
        modloaderVersion = "latest"

    minecraftVersion: str = input("Enter minecraft version: ")
    if minecraftVersion == "":
        print("Required a minecraft version!")
        sys.exit(1)

    metadata = Metadata(modpackName, modpackVersion, modloaderType, modloaderVersion, minecraftVersion).getAll()
    print(f"""
Manifest Version: {' ':<4}{metadata['manifest']['version']}
Mod Pack Name: {' ':<7}{modpackName}
Mod Pack Version: {' ':<4}{modpackVersion}
Mod Loader: {' ':<10}{modloaderType}
Mod Loader Version: {' ':<2}{modloaderVersion}
Minecraft Version: {' ':<3}{minecraftVersion}
""")

    isOk = input("Is this okay? [Y/n]")
    if isOk.lower() in ["", "y", "yes", "true"]:
        os.makedirs(f"{modpackName}", exist_ok=True)
        if os.path.exists(f"{modpackName}/pack.manifest.json"):
            isOk = input("This modpack already exists, overwrite the manifest? [Y/n]")
            if isOk.lower() in ["", "y", "yes", "true"]:
                os.remove(f"{modpackName}/pack.manifest.json")
            else:
                print("Initialization cancelled")
                sys.exit()
        with open(f"{modpackName}/pack.manifest.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(metadata))
    else:
        print("Initialization cancelled")


if __name__ == "__main__":
    if args.init:
        initNewPack()