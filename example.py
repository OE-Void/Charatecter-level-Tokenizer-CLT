from clt.clt import decode, encode, vocab, vocab_size

en = encode("hello bro")

print(en)

print(decode(en))

print(f"Vocab: {vocab}")
print(f"Vocab_Size: {vocab_size}")