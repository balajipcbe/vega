from shutil import which
from pytube import YouTube
import argparse
import os
import subprocess


class YouTubeMp3Downloader:
    def __init__(self, videoUrl=None, dl_dir=os.getcwd()):
        self.__url = videoUrl
        self.__dir = dl_dir
        self.__ytObj = None
        self.__ytStreamObj = None

    def downloadYouTube(self):
        self.__ytObj = YouTube(self.__url)
        self.__ytStreamObj = self.__ytObj.streams.filter(progressive=True,
                                            file_extension='mp4'). \
                                            order_by('resolution'). \
                                            desc().first()
        print('Downloading ... '+self.__ytObj.title)
        self.__ytStreamObj.download(self.__dir)


    def check_file_exists(self,name):
        ret_val = which(name)
        if ret_val is None:
            print('Please install '+name)
            exit(1)

    def convertToMp3(self):
        new_filename =  self.__ytStreamObj.default_filename[:
                        self.__ytStreamObj.default_filename.find('.')]+'.mp3'
        default_filename =  os.path.join(self.__dir,
                                         self.__ytStreamObj.default_filename)
        new_filename = os.path.join(self.__dir, new_filename)

        self.check_file_exists('ffmpeg')
        subprocess.call(['ffmpeg','-i', default_filename,
                         new_filename],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

        self.check_file_exists('rm')
        subprocess.call(['rm',default_filename])
        print(new_filename +' downloaded')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Paste your youtube URL")
    parser.add_argument("--dir", default=os.getcwd(), help="Download directory\
                        (default : current directory)")
    args = parser.parse_args()

    if args.dir and not os.path.exists(args.dir):
        os.makedirs(args.dir)

    yt = YouTubeMp3Downloader(args.url,args.dir)
    yt.downloadYouTube()
    yt.convertToMp3()
