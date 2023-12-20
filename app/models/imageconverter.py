import base64
from PIL import Image
from io import BytesIO

class ImageConverter:

    def __init__(self):
        pass

    def convert_image_to_base64(self, file, max_size_kb=50, max_resolution=(800, 800)):
        if file:
            # Read the file content
            file_contents = file.read()

            # Open the image using PIL
            image = Image.open(BytesIO(file_contents))

            # Convert to RGB mode if the image is in RGBA mode
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Calculate the compression ratio based on resolution
            target_width, target_height = max_resolution
            compression_ratio_width = target_width / image.width
            compression_ratio_height = target_height / image.height
            compression_ratio = min(compression_ratio_width, compression_ratio_height)

            if compression_ratio < 1:
                # Resize the image while maintaining the aspect ratio
                new_width = int(image.width * compression_ratio)
                new_height = int(image.height * compression_ratio)
                image = image.resize((new_width, new_height), resample=Image.LANCZOS)

            # Convert the image to bytes
            buffered = BytesIO()
            image.save(buffered, format="JPEG")  # You can change the format if needed
            buffered_contents = buffered.getvalue()

            # Encode the compressed image into base64
            encoded_file = base64.b64encode(buffered_contents)

            return encoded_file.decode('utf-8')
        else:
            return None
