import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'github-automate-action'

# Upload index.html
s3.upload_file('index.html', BUCKET_NAME, 'index.html')
print("Uploaded index.html")

# Upload images from folder
image_folder = 'images'

if os.path.exists(image_folder):
    for file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file)

        if file.endswith(('.jpg', '.png')):
            s3.upload_file(file_path, BUCKET_NAME, file)
            print(f"Uploaded {file}")
else:
    print("No images folder found")