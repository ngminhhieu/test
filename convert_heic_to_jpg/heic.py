ALLOWED_EXTENSIONS = set(['heic', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if "IMG_2616.HEIC".rsplit('.', 1)[1].lower() == "heic":
    # image_path_heic = os.path.join(DIR, "label.JPG")
    heif_file = pyheif.read('IMG_2616.HEIC')
    image_path_jpg = image_path_heic.replace(".HEIC", ".JPG")
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    image.save(image_path_jpg, "JPEG")