import hashlib
text = input("Texto: ")
text_sha1 = hashlib.sha1(text.encode());
hex_dig = text_sha1.hexdigest()
print(hex_dig)
