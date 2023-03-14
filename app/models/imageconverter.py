import base64

class ImageConverter:

    def __init__(self):
        pass

    def convert_image_to_base_64(self,file):
        if file:
            file_contents = file.read()
            encoded_file = base64.b64encode(file_contents)
            return encoded_file.decode('utf-8')
        else:
            return None