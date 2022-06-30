#!/usr/bin/env python  
#This is a shebang line, Used to give the python interpreter's path. We cannot write anything in the shebang line.
#let's start by checking our Internet Connectivity using requests module
import requests
from pytube import YouTube

def connectivity(url='https://www.google.com/', timeout= 5):
    try:
        req = requests.get(url, timeout= timeout)
        req.raise_for_status()
        print("You are connected to the internet!")
        return True

    except requests.HTTPError as e:
        print("Internet Connection failed, status code{0}".format(e.response.status_code))

    except requests.ConnectionError:
        print("No connection available")
        return False


def youtube_download():
    youtube_video_url = input("Please enter the URL of the video you want to download: ")

    try:
        yt_object = YouTube(youtube_video_url)
        filters = yt_object.streams.filter(progressive=True, file_extension='mp4')
        filters.get_highest_resolution().download()

        print("Video downloaded successfully.")

    except Exception as e:
        print(e)


if connectivity():
    youtube_download()
