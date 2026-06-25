import os
import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class Media:
    path: str
    resolution: str

def get_xcode_project_folder():
    parser = ArgumentParser()
    parser.add_argument('--folder', help='Xcode project folder')
    args = parser.parse_args()
    return args.folder

def parse_assets_folder(folder):
    assets_folder = os.path.join(folder, 'Assets.xcassets')
    if not os.path.exists(assets_folder):
        raise ValueError('Invalid Xcode project folder')
    screenshots = []
    for root, dirs, files in os.walk(assets_folder):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpeg'):
                screenshots.append(Media(os.path.join(root, file), 'Unknown'))
    return screenshots

def detect_screen_recordings(folder):
    resources_folder = os.path.join(folder, 'Resources')
    if not os.path.exists(resources_folder):
        raise ValueError('Invalid Xcode project folder')
    screen_recordings = []
    for root, dirs, files in os.walk(resources_folder):
        for file in files:
            if file.endswith('.mov') or file.endswith('.mp4'):
                screen_recordings.append(Media(os.path.join(root, file), 'Unknown'))
    return screen_recordings

def get_media_resolution(media):
    # For simplicity, assume resolution is the same as the file name
    return os.path.basename(media.path)

def import_media(folder):
    screenshots = parse_assets_folder(folder)
    screen_recordings = detect_screen_recordings(folder)
    media = screenshots + screen_recordings
    for m in media:
        m.resolution = get_media_resolution(m)
    return media

def main():
    folder = get_xcode_project_folder()
    if not folder:
        print('Please provide a valid Xcode project folder')
        return
    try:
        media = import_media(folder)
        print(json.dumps([m.__dict__ for m in media], indent=4))
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
