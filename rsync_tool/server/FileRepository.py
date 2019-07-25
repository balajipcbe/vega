#!/usr/bin/env python3
import os
import hashlib
from stat import *

class FileRepository:
    def __init__(self, path=os.getcwd()):
        self.__path = path
        self.__repo = {}

    def get_path(self):
        return self.__path

    def buildFileRepository(self, pathname=get_path()):
        for f in os.listdir(pathname):
            pathname = os.path.join(pathname,f)
            mode = os.stat(pathname).st_mode

            if S_ISDIR(mode):
                self.buildFileRepository(pathname)
            elif S_ISREG(mode):
                statinfo = os.stat(pathname)
                keystr = pathname+str(statinfo.st_mtime)+str(statinfo.st_ctime)
                keybyte = keystr.encode()
                key = self.compute_hash(keybyte)
                self.__repo[key] = pathname

    def display_repo(self):
        for key,value in self.__repo.items():
            print(key,value)

    def get_repo(self):
        return self.__repo

    def compute_hash(self,bytestring):
        hash = hashlib.sha256(bytestring)
        return hash.hexdigest()


