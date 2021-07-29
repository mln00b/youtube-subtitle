from .get_subtitles import get_subtitles

def test_single_video_from_url(url):
    get_subtitles(url)

if __name__ == '__main__':
    test_single_video_from_url("https://www.youtube.com/watch?v=jrjdsVCG32k&list=PLyvuS7237e7_vJCTjJSWXgSiRbDSaYrB6&index=1")