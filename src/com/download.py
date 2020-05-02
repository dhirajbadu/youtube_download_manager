from pytube import YouTube
import os
from pathlib import Path
import argparse


parser = argparse.ArgumentParser(description='youtube download manager')
parser.add_argument('-link', dest='link', help='provide link')
parser.add_argument('-audioOnly', dest='audioOnly', help='provide audioOnly' , default=False , required=False)
parser.add_argument('-quality', dest='quality', help='provide quality' , default="D" , required=False)

args = parser.parse_args()

link = args.link
audioOnly = args.audioOnly
quality = args.quality

class Download:

    def getPath(self):
        home = str(os.path.join(Path.home(), "Downloads"))
        print("downloading....!!")
        print(home)

        return home

    def DownDefaultVideo(self , link):
        print("dd")
        YouTube(str(link)).streams.first().download(output_path=self.getPath())
        print("successfully downloaded")

    def downHighQalityVideo(self , link):
        print("hv")
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=self.getPath())
        print("successfully downloaded")

    def downLowQalityVideo(self, link):
        print("lv")
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().last().download(output_path=self.getPath())
        print("successfully downloaded")

    def downDefaultAudio(self , link):
        print("da")
        yt = YouTube(link)
        yt.streams.get_audio_only(subtype="mp4").download(output_path=self.getPath())
        print("successfully downloaded")

    def downLowQalityAudio(self , link):
        print("la")
        yt = YouTube(link)
        yt.streams.filter(only_audio=True, subtype="mp4").order_by("abr").desc().last().download(output_path=self.getPath())
        print("successfully downloaded")

    def downHeighQalityAudio(self, link):
        print("ha")
        yt = YouTube(link)
        yt.streams.filter(only_audio=True, subtype="mp4").order_by("abr").desc().first().download(output_path=self.getPath())
        print("successfully downloaded")



switcher = {
            "dv": Download.DownDefaultVideo,
            "hv": Download.downHighQalityVideo,
            "lv": Download.downLowQalityVideo,
            "da": Download.downDefaultAudio,
            "la": Download.downLowQalityAudio,
            "ha": Download.downHeighQalityAudio,
            "dd": Download.DownDefaultVideo
}


def main():
    manager = None
    if(audioOnly):
        manager = switcher.get(str(quality).lower()+"a" , "dd")
    else:
        manager = switcher.get(str(quality).lower()+"v", "dd")
    manager(Download(), link)

if __name__ == '__main__':
    main()
