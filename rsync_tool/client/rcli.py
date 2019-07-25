#!/usr/bin/env python3
import socket

def client_process(host, port):
    chunk_list = []
    counter = 0
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))
        while True:
            data = s.recv(1024)
            if not data:
                break
            #print(data)
            print('Recd chunk ',counter)
            counter += 1
            chunk_list.append(data)
    return chunk_list

def bin_file_writer(filename, chunk_list):
    with open(filename,'wb') as writer:
        for chunk in chunk_list:
            writer.write(chunk)

cl = client_process('127.0.0.1',65432)
bin_file_writer('cli.jpg',cl)
