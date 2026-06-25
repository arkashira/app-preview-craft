# App Video Pro
App Video Pro is a Python library for creating and exporting high-quality App Store preview videos.

## Usage
1. Create a `VideoTemplate` instance with the desired template name, format, width, and height.
2. Create an `AppVideoPro` instance with the `VideoTemplate` instance.
3. Call the `create_video` method with a list of assets to create a high-quality App Store preview video.
4. Call the `export_video` method with the created video data and the desired output format to export the video.
5. Call the `upload_video` method with the exported video data to upload the video to the App Store.

## Testing
Run the tests using `pytest` to ensure the library is working correctly.
