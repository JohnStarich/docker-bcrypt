import bcrypt
import sys

if len(sys.argv) < 2:
    print('Error: please provide a password.', file=sys.stderr)
    sys.exit(2)
password = sys.argv[1]
strength = None
if len(sys.argv) > 2:
    strength = int(sys.argv[2])
if strength:
    salt = bcrypt.gensalt(rounds=strength)
else:
    salt = bcrypt.gensalt()
password = password.encode('utf-8')
bhash = bcrypt.hashpw(password, salt)
print(bhash.decode('utf-8'), end='', flush=True)
print(file=sys.stderr)

