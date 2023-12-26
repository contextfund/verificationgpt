import cv2
from imwatermark import WatermarkDecoder, WatermarkEncoder

def decode(bgr, src_filepath: str = None, length_bits: int = 16):
    length_range = [length_bits] if length_bits is not None else range(8, 320, 8)
    if not bgr:
        bgr = cv2.imread(src_filepath)
    for length_bits in length_range:
        print(length_bits)
        decoder = WatermarkDecoder('bytes', length_bits)
        watermark = decoder.decode(bgr, 'dwtDct')
        print('watermark')
        print(watermark.decode('utf-8'))
    return watermark.decode()
def encode(src_filepath: str, wm: str):
    bgr = cv2.imread(src_filepath)

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', wm.encode('utf-8'))
    bgr_encoded = encoder.encode(bgr, 'dwtDct')

    cv2.imwrite(f'{src_filepath}_1', bgr_encoded)