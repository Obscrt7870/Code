from PIL import Image

def extract_lsb(image_path: str, max_bytes: int = 100):
    img = Image.open(image_path).convert('RGB')
    binary_data = ""
     
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            if len(binary_data) >= max_bytes * 8:
                break
        if len(binary_data) >= max_bytes * 8:
            break

    # Converte os bits para texto ASCII
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    extracted_text = "".join([chr(int(b, 2)) for b in bytes_data])
    
    print(f"[+] Amostra LSB (primeiros {max_bytes} bytes):")
    print(repr(extracted_text))

if __name__ == "__main__":
    # Certifique-se de ter uma imagem .png no diretório
    try:
        extract_lsb("exemplo.png")
    except FileNotFoundError:
        print("[-] Crie ou aponte para um arquivo PNG existente.")
