from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

image = PIL.open("./images/imagen3.png")
decoder = PDF417Decoder(image)

if decoder.decode() > 0:
    decoded = decoder.barcode_data_index_to_string(0)
    print(decoded)