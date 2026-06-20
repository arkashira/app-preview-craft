import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class AppInfo:
    name: str
    screenshots: list

@dataclass
class Template:
    name: str
    description: str

def create_video_preview(app_info: AppInfo, template: Template) -> str:
    video_preview = {
        "app_name": app_info.name,
        "screenshots": app_info.screenshots,
        "template_name": template.name,
        "template_description": template.description
    }
    return json.dumps(video_preview)

def main():
    parser = ArgumentParser()
    parser.add_argument("--app_name", help="Name of the app")
    parser.add_argument("--screenshots", help="Screenshots of the app", nargs="+")
    parser.add_argument("--template_name", help="Name of the template")
    parser.add_argument("--template_description", help="Description of the template")
    args = parser.parse_args()

    app_info = AppInfo(args.app_name, args.screenshots)
    template = Template(args.template_name, args.template_description)

    video_preview = create_video_preview(app_info, template)
    print(video_preview)

if __name__ == "__main__":
    main()
