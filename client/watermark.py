import c2pa

def decode_c2pa(src_filepath: str):
    try:
        return c2pa.read_file(src_filepath, None)
    except Exception as e:
        return {"Exception": str(e)}



