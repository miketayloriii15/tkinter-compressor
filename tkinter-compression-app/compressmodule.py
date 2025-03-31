import zlib
import base64

# Compress a text file using zlib and base64
def compress(inputfile, outputfile):
    """
    Compresses the contents of the input file using zlib and base64 encoding.
    Saves the compressed data to the specified output file.
    """
    with open(inputfile, 'r', encoding='utf-8') as f:
        data = f.read()

    data_bytes = data.encode('utf-8')
    compressed_data = zlib.compress(data_bytes, level=9)
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')

    with open(outputfile, 'w', encoding='utf-8') as f:
        f.write(encoded_data)

# Decompress a base64 and zlib-compressed file back to plain text
def decompress(inputfile, outputfile):
    """
    Decompresses a file that was compressed using the compress function.
    Saves the original text to the specified output file.
    """
    with open(inputfile, 'r', encoding='utf-8') as f:
        encoded_content = f.read()

    decoded_bytes = base64.b64decode(encoded_content.encode('utf-8'))
    decompressed_data = zlib.decompress(decoded_bytes).decode('utf-8')

    with open(outputfile, 'w', encoding='utf-8') as f:
        f.write(decompressed_data)

# Example usage (can be removed or commented out for production)
# compress('ot.txt', 'compressed_output.txt')
# decompress('compressed_output.txt', 'decompressed_output.txt')
