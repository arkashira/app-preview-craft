import os
import json
import sys
from app_preview_craft import Media, parse_assets_folder, detect_screen_recordings, import_media, get_media_resolution
import pytest

@pytest.fixture
def temp_folder():
    folder = 'temp_folder'
    os.mkdir(folder)
    yield folder
    import shutil
    shutil.rmtree(folder)

def test_parse_assets_folder(temp_folder):
    assets_folder = os.path.join(temp_folder, 'Assets.xcassets')
    os.mkdir(assets_folder)
    screenshot = 'screenshot.png'
    with open(os.path.join(assets_folder, screenshot), 'w') as f:
        f.write('dummy content')
    screenshots = parse_assets_folder(temp_folder)
    assert len(screenshots) == 1
    assert screenshots[0].path == os.path.join(assets_folder, screenshot)

def test_detect_screen_recordings(temp_folder):
    resources_folder = os.path.join(temp_folder, 'Resources')
    os.mkdir(resources_folder)
    screen_recording = 'screen_recording.mov'
    with open(os.path.join(resources_folder, screen_recording), 'w') as f:
        f.write('dummy content')
    screen_recordings = detect_screen_recordings(temp_folder)
    assert len(screen_recordings) == 1
    assert screen_recordings[0].path == os.path.join(resources_folder, screen_recording)

def test_import_media(temp_folder):
    assets_folder = os.path.join(temp_folder, 'Assets.xcassets')
    os.mkdir(assets_folder)
    screenshot = 'screenshot.png'
    with open(os.path.join(assets_folder, screenshot), 'w') as f:
        f.write('dummy content')
    resources_folder = os.path.join(temp_folder, 'Resources')
    os.mkdir(resources_folder)
    screen_recording = 'screen_recording.mov'
    with open(os.path.join(resources_folder, screen_recording), 'w') as f:
        f.write('dummy content')
    media = import_media(temp_folder)
    assert len(media) == 2
    assert media[0].path == os.path.join(assets_folder, screenshot)
    assert media[1].path == os.path.join(resources_folder, screen_recording)

def test_import_media_invalid_folder():
    with pytest.raises(ValueError):
        import_media('invalid_folder')

def test_get_media_resolution():
    media = Media('path/to/media.png', 'Unknown')
    assert get_media_resolution(media) == 'media.png'
