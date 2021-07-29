import os

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from argparse import ArgumentParser, Namespace
from tqdm import tqdm

from typing import List


def _get_video_id_from_url(url: str) -> str:
    assert "watch?v=" in url, "URL format is incorrect. Should contain something like youtube.com/watch?v="
    return url.split("watch?v=")[-1].split("&")[0]

def _write_to_json(data: List, dest_fname: str = None) -> None:
    formatter = JSONFormatter()
    json_formatted = formatter.format_transcript(data)

    dest_path = dest_fname + ".json"
    if os.path.exists(dest_path):
        print(f"Dest file alread exists: {dest_path}. Not overwriting")
    else:
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(json_formatted)
        
        print(f"JSON file written at: {dest_path}")


def _get_transcript_from_video_id(video_id: str, dest_fname: str = None) -> None:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=('en','en-IN'))

    if dest_fname is None: 
        dest_fname = video_id
    _write_to_json(transcript, dest_fname)

def get_subtitles(url: str = None, urls: List = None) -> None:
    assert url is not None or urls is not None, "Both url & urls can't be empty. Either give 1 url or list of urls"
    if not urls and url:
        urls = [url]
    
    failures = []
    for url in tqdm(urls):
        try:
            print("url: ", url)
            video_id = _get_video_id_from_url(url)
            _get_transcript_from_video_id(video_id)
        except Exception as e:
            print(e)
            failures.append(url)
    
    if failures:
        print(f"List of failed urls: {failures}")

if __name__ == '__main__':
    parser = ArgumentParser(description="Youtube Subtitle Downloader")
    parser.add_argument("--url", default=None,type=str,help='Single Video URL')
    parser.add_argument("--urls", default=None,nargs="+", help='List of urls, space separated')

    args = parser.parse_args()
    get_subtitles(url = args.url, urls = args.urls)
