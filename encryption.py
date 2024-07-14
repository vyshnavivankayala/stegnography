from PIL import Image

def encode_text_in_image(image_path, output_image_path, text):
    # Open the image
    img = Image.open(image_path)
    encoded = img.copy()
    
    width, height = img.size
    index = 0

    # Convert the text to binary
    binary_text = ''.join([format(ord(i), "08b") for i in text])
    binary_text += '1111111111111110'  # End delimiter

    data_len = len(binary_text)

    for row in range(height):
        for col in range(width):
            if index < data_len:
                pixel = list(img.getpixel((col, row)))
                
                # Modify the least significant bit
                for n in range(3):  # RGB channels
                    if index < data_len:
                        pixel[n] = int(format(pixel[n], '08b')[:-1] + binary_text[index], 2)
                        index += 1
                
                encoded.putpixel((col, row), tuple(pixel))

    # Save the encoded image
    encoded.save(output_image_path)

# Usage
image_path = r"C:\Users\DELL\OneDrive\Desktop\New folder\benz car.jpeg"
output_image_path = r"C:\Users\DELL\OneDrive\Desktop\New folder\encrypted.jpeg"
text = "you know me"

encode_text_in_image(image_path, output_image_path, text)

