from typing import Union, Literal


class Metadata:
    def __init__(self, modpackName: str, modpackVersion: str, modloaderType: str, modloaderVersion: str, minecraftVersion: str, manifestVersion: str = 1):
        self.manifestVersion = manifestVersion
        self.minecraftVersion = minecraftVersion

        self.modpackName = modpackName
        self.modpackVersion = modpackVersion

        self.modloaderType = modloaderType
        self.modloaderVersion = modloaderVersion

    def getAll(self):
        return {
            "manifest": {
                "version": self.manifestVersion,
            },
            "minecraft": {
                "version": self.minecraftVersion,
            },
            "modpack": {
                "name": self.modpackName,
                "version": self.modpackVersion,
            },
            "modloader": {
                "type": self.modloaderType,
                "version": self.modloaderVersion
            }
        }


class Mod:
    def __init__(self, version: str, origin: Union[Literal["curseforge", "modrinth", "custom", "manual"], None] = None, originId: Union[str, int, None] = None, downloadUrl: Union[str, None] = None, isClient: bool = False, isServer: bool = False):
        self.version = version
        self.origin = origin

        if origin is not None:
            if origin in ["curseforge", "modrinth"]:
                if originId is None:
                    raise "Need to provide origin mod ID"
                self.originId = originId
            if origin == "custom":
                self.downloadUrl = downloadUrl

        self.client = isClient
        self.server = isServer

    def getMod(self):
        return self

class Manifest:
    def __init__(self, metadata: Metadata, mods: Union[None]):
        ...
