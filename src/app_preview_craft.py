import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class TemplateType(str, Enum):
    DEFAULT = "default"
    CUSTOM = "custom"

@dataclass
class AppInfo:
    name: str
    screenshots: List[str]

class AppPreviewCraft:
    def __init__(self):
        self.templates = {
            TemplateType.DEFAULT: "default_template",
            TemplateType.CUSTOM: "custom_template"
        }

    def generate_video(self, app_info: AppInfo, template_type: TemplateType) -> str:
        if template_type not in self.templates:
            raise ValueError("Invalid template type")
        video_data = {
            "app_name": app_info.name,
            "screenshots": app_info.screenshots,
            "template": self.templates[template_type]
        }
        return json.dumps(video_data)

    def download_video(self, video_data: str) -> str:
        return f"Downloaded video: {video_data}"
