def encode_with_zero_width(text):
  encoded_text = ""
  for char in text:
    binary_char = format(ord(char),
                         '08b')  # Convert character to 8-bit binary string
    for bit in binary_char:
      if bit == '0':
        encoded_text += "\u200B"  # Zero Width Space for '0'
      else:
        encoded_text += "\u200C"  # Zero Width Non-Joiner for '1'
  return encoded_text


def decode_zero_width(encoded_text):
  binary_string = ""
  for char in encoded_text:
    if char == "\u200B":
      binary_string += '0'
    elif char == "\u200C":
      binary_string += '1'
  decoded_text = ""
  for i in range(0, len(binary_string), 8):
    byte = binary_string[i:i + 8]
    decoded_text += chr(int(byte, 2))
  return decoded_text


original_text = "Gage Howe"
print("Original Text:", original_text)

encoded_text = encode_with_zero_width(original_text)
print("encoded text:", encoded_text)

decoded_text = decode_zero_width(encoded_text)
print("decoded text:", decoded_text)

```
Sample output:

Original Text: Gage Howe
encoded text: ​‌​​​‌‌‌​‌‌​​​​‌​‌‌​​‌‌‌​‌‌​​‌​‌​​‌​​​​​​‌​​‌​​​​‌‌​‌‌‌‌​‌‌‌​‌‌‌​‌‌​​‌​‌
Gage Howe

Output: 38 binary characters, u200B or u200C
```
