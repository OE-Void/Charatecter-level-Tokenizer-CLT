with open("token.txt", 'r') as f:
    text = f.read()

# checking some imp things

vocab_size = len(set(text))
vocab = set(text)

# create the mapping of token and words

char_to_idx = {ch: i for i, ch in enumerate(vocab)}
idx_to_char = {i: ch for i, ch in enumerate(vocab)}

# here are the encode and decode funtions

def encode(s):
    return [char_to_idx[ch] for ch in s]

def decode(indices):
    return ''.join([idx_to_char[i] for i in indices])

