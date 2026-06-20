import json
from app_preview_craft import AppPreviewCraft, AppInfo, TemplateType
import pytest

def test_generate_video_default_template():
    app_preview_craft = AppPreviewCraft()
    app_info = AppInfo("Test App", ["screenshot1", "screenshot2"])
    video_data = app_preview_craft.generate_video(app_info, TemplateType.DEFAULT)
    assert json.loads(video_data) == {
        "app_name": "Test App",
        "screenshots": ["screenshot1", "screenshot2"],
        "template": "default_template"
    }

def test_generate_video_custom_template():
    app_preview_craft = AppPreviewCraft()
    app_info = AppInfo("Test App", ["screenshot1", "screenshot2"])
    video_data = app_preview_craft.generate_video(app_info, TemplateType.CUSTOM)
    assert json.loads(video_data) == {
        "app_name": "Test App",
        "screenshots": ["screenshot1", "screenshot2"],
        "template": "custom_template"
    }

def test_generate_video_invalid_template_type():
    app_preview_craft = AppPreviewCraft()
    app_info = AppInfo("Test App", ["screenshot1", "screenshot2"])
    with pytest.raises(ValueError):
        app_preview_craft.generate_video(app_info, "invalid_template")

def test_download_video():
    app_preview_craft = AppPreviewCraft()
    video_data = json.dumps({"app_name": "Test App", "screenshots": ["screenshot1", "screenshot2"]})
    downloaded_video = app_preview_craft.download_video(video_data)
    assert downloaded_video == f"Downloaded video: {video_data}"
