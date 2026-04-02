import random
import string
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation


password = ''.join(random.choices(characters, k=10))

print( password)