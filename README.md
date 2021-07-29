# youtube-subtitle
Fetch subtitles for given Youtube Video(s)

Wrapper on top of the excellent [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) library.

Current code takes as input a Youtube Video url and outputs a JSON file containing the subtitles.

Input Formats:
1. Single url
2. List of urls, space separated

Output Formats:
1. JSON file - one for each video

If a file has already been written, it won't overwrite.

## Installation

Clone the repo

Then install from requirements:

`pip install -r requirements.txt`

## Sample Usage

### Single URL

`python get_subtitles.py --url https://www.youtube.com/watch\?v\=exaWOE8jvy8`

```
(py39) ➜  youtube-subtitle git:(main) ✗ python get_subtitles.py --url https://www.youtube.com/watch\?v\=exaWOE8jvy8
  0%|                                                                                                | 0/1 [00:00<?, ?it/s]url:  https://www.youtube.com/watch?v=exaWOE8jvy8
JSON file written at: exaWOE8jvy8.json
100%|████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.04s/it]
```

### Multiple URLs

`python get_subtitles.py --urls https://www.youtube.com/watch\?v\=exaWOE8jvy8 https://www.youtube.com/watch\?v\=DbeIqrwb_dE`

```
(py39) ➜  youtube-subtitle git:(main) ✗ python get_subtitles.py --urls https://www.youtube.com/watch\?v\=exaWOE8jvy8 https://www.youtube.com/watch\?v\=DbeIqrwb_dE
  0%|                                                                                                                                                     | 0/2 [00:00<?, ?it/s]url:  https://www.youtube.com/watch?v=exaWOE8jvy8
JSON file written at: exaWOE8jvy8.json
 50%|██████████████████████████████████████████████████████████████████████▌                                                                      | 1/2 [00:00<00:00,  1.03it/s]url:  https://www.youtube.com/watch?v=DbeIqrwb_dE
JSON file written at: DbeIqrwb_dE.json
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.00s/it]
```

## To-Do
1. Add reading URL's from a text file containing the data