from PIL import Image

def decode_text_from_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    binary_text = ""
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            # Extract the least significant bit from each color channel (RGB)
            for n in range(3):
                binary_text += format(pixel[n], '08b')[-1]

    # Split the binary text by 8 bits
    all_bytes = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    
    # Convert binary to characters until the end delimiter is found
    decoded_text = ""
    for byte in all_bytes:
        if byte == "11111110":  # End delimiter
            break
        decoded_text += chr(int(byte, 2))

    return decoded_text

# Usage
image_path = r"C:\Users\DELL\OneDrive\Desktop\New folder\encrypted.jpeg"
decoded_text = decode_text_from_image(image_path)
print("Decoded text:", decoded_text)

