from pytube import YouTube
from urllib.parse import urlparse, parse_qs
import os
import time

def clean_url(url):
    parsed_url = urlparse(url)
    clean_query = parse_qs(parsed_url.query)
    clean_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    return clean_url

def download_youtube_video(url, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            clean_video_url = clean_url(url)
            yt = YouTube(clean_video_url)
            stream = yt.streams.get_highest_resolution()
            path = os.path.expanduser('~/Downloads/Myapp')
            os.makedirs(path, exist_ok=True)
            stream.download(output_path=path)
            print(f"Video downloaded successfully and saved to {path}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in 5 seconds... (Attempt {retries + 1} of {max_retries})")
                time.sleep(5)
            else:
                print("Max retries reached. Unable to download the video.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)