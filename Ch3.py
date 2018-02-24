# Attempts at exercises for Downey "Think Python" chapter 3

def right_justify(raw_str):
    pad = 70 - len(raw_str)
    if pad < 0:
        right_justify("Line too long")
    else:
        print (' ' * pad) + raw_str

print "Testing right_justify"
right_justify("Hello")
right_justify("Hello world - the quick brown fox jumps over the lazy dog")
right_justify("Hello world!" * 8)
