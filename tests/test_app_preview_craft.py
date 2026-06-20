from app_preview_craft import create_video_preview, AppInfo, Template
import json

def test_create_video_preview():
    app_info = AppInfo("Test App", ["screenshot1", "screenshot2"])
    template = Template("Test Template", "This is a test template")
    video_preview = create_video_preview(app_info, template)
    expected_video_preview = {
        "app_name": "Test App",
        "screenshots": ["screenshot1", "screenshot2"],
        "template_name": "Test Template",
        "template_description": "This is a test template"
    }
    assert json.loads(video_preview) == expected_video_preview

def test_create_video_preview_empty_screenshots():
    app_info = AppInfo("Test App", [])
    template = Template("Test Template", "This is a test template")
    video_preview = create_video_preview(app_info, template)
    expected_video_preview = {
        "app_name": "Test App",
        "screenshots": [],
        "template_name": "Test Template",
        "template_description": "This is a test template"
    }
    assert json.loads(video_preview) == expected_video_preview

def test_create_video_preview_none_template():
    app_info = AppInfo("Test App", ["screenshot1", "screenshot2"])
    template = Template(None, "This is a test template")
    video_preview = create_video_preview(app_info, template)
    expected_video_preview = {
        "app_name": "Test App",
        "screenshots": ["screenshot1", "screenshot2"],
        "template_name": None,
        "template_description": "This is a test template"
    }
    assert json.loads(video_preview) == expected_video_preview
