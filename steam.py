import random
import string

N=5

print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)) + "-" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)) + "-" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)))
