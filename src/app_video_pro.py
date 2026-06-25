import json
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class VideoFormat(Enum):
    MP4 = "mp4"
    MOV = "mov"

@dataclass
class VideoTemplate:
    name: str
    format: VideoFormat
    width: int
    height: int

class AppVideoPro:
    def __init__(self, template: VideoTemplate):
        self.template = template

    def create_video(self, assets: list) -> str:
        # Create a high-quality App Store preview video
        video_data = {
            "template": self.template.name,
            "format": self.template.format.value,
            "width": self.template.width,
            "height": self.template.height,
            "assets": assets
        }
        return json.dumps(video_data)

    def export_video(self, video_data: str, output_format: VideoFormat) -> str:
        # Export the video in the required format
        video_data_dict = json.loads(video_data)
        video_data_dict["format"] = output_format.value
        return json.dumps(video_data_dict)

    def upload_video(self, video_data: str) -> bool:
        # Upload the video to the App Store (simulated)
        try:
            # Simulate upload process
            print("Uploading video to App Store...")
            return True
        except Exception as e:
            print(f"Error uploading video: {e}")
            return False
