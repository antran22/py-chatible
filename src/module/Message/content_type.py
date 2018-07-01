from urllib.parse import urlparse
import mimetypes

mimetypes.init()


def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext


video_extension = tuple(get_extensions_for_type('video'))
audio_extension = tuple(get_extensions_for_type('audio'))
image_extension = tuple(get_extensions_for_type('image'))


def determine_content_type(content):
    url = urlparse(content)

    def test_extension(extension_list):
        for extension in extension_list:
            if url.path.endswith(extension):
                return True
    if url.scheme == "https" and ('fbcdn.net' in url.hostname or 'fbsbx.com' in url.hostname):
        if test_extension(image_extension):
            return "image"
        if test_extension(audio_extension) or "audioclip" in url.path:
            return "audio"
        if test_extension(video_extension):
            return "video"
    else:
        return "text"
