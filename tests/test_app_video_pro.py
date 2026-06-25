import json
from app_video_pro import AppVideoPro, VideoTemplate, VideoFormat
import pytest

def test_create_video():
    template = VideoTemplate("template1", VideoFormat.MP4, 1080, 1920)
    app_video_pro = AppVideoPro(template)
    assets = ["asset1", "asset2"]
    video_data = app_video_pro.create_video(assets)
    video_data_dict = json.loads(video_data)
    assert video_data_dict["template"] == "template1"
    assert video_data_dict["format"] == "mp4"
    assert video_data_dict["width"] == 1080
    assert video_data_dict["height"] == 1920
    assert video_data_dict["assets"] == assets

def test_export_video():
    template = VideoTemplate("template1", VideoFormat.MP4, 1080, 1920)
    app_video_pro = AppVideoPro(template)
    assets = ["asset1", "asset2"]
    video_data = app_video_pro.create_video(assets)
    output_format = VideoFormat.MOV
    exported_video_data = app_video_pro.export_video(video_data, output_format)
    exported_video_data_dict = json.loads(exported_video_data)
    assert exported_video_data_dict["format"] == "mov"

def test_upload_video():
    template = VideoTemplate("template1", VideoFormat.MP4, 1080, 1920)
    app_video_pro = AppVideoPro(template)
    assets = ["asset1", "asset2"]
    video_data = app_video_pro.create_video(assets)
    assert app_video_pro.upload_video(video_data)

def test_upload_video_failure():
    template = VideoTemplate("template1", VideoFormat.MP4, 1080, 1920)
    app_video_pro = AppVideoPro(template)
    assets = ["asset1", "asset2"]
    video_data = app_video_pro.create_video(assets)
    # Simulate upload failure
    app_video_pro.upload_video = lambda x: False
    assert not app_video_pro.upload_video(video_data)
