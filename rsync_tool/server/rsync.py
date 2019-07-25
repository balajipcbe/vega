#!/usr/bin/env python3
import hashlib
import socket
from stat import *
import FileRepository
import os

def compute_hash(bytestring):
    hash = hashlib.sha256(bytestring)
    return hash.hexdigest()

def bin_file_reader(srcfilename):
    BLK_SZ = 64
    counter = 0
    chunks = {}
    with open(srcfilename,'rb') as reader:
        while True:
            block = reader.read(BLK_SZ)
            if block:
                index = compute_hash(block)
                chunks[index] = block
                counter += 1
            else:
                break
    return chunks


def build_file_list():
    fp = FileRepository.FileRepository()
    fp.buildFileRepository()
    fp.display_repo()


def server_process(host, port, chunks):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                for key,val in chunks.items():
                    print('sending chunk id : ',key)
                    conn.sendall(val)


build_file_list()
