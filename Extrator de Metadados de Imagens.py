from PIL import Image
from PIL.ExifTags import TAGS
 
def extract_exif(image_path: str) -> dict:
    image = Image.open(image_path)
    exif_data = image._getexif()
    
    if not exif_data:
        print("[-] Nenhum dado EXIF encontrado.")
        return {}

    metadata = {}
    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)
        metadata[tag_name] = value

    return metadata

if __name__ == "__main__":
    # Substitua pelo caminho de uma imagem real
    file_path = "exemplo.jpg"
    try:
        data = extract_exif(file_path)
        for key, val in data.items():
            print(f"{key}: {val}")
    except FileNotFoundError:
        print(f"[-] Arquivo '{file_path}' não encontrado.")
