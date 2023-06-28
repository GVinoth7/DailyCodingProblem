import base64


def hex_to_base64(hex_str):
    
    bytes_data = bytes.fromhex(hex_str)

    # Encode bytes as base64
    base64_data = base64.b64encode(bytes_data)
    
    # Convert base64 bytes to string
    base64_str = base64_data.decode('utf-8')
    
    return base64_str


print(hex_to_base64('asdfhe'))