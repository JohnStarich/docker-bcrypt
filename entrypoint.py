from passlib.hash import bcrypt
import sys
import argparse
import getpass


class PasswordPrompt(argparse.Action):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, parser, args, values, option_string=None):
        try:
            setattr(args, self.dest, getpass.getpass())
        except:
            print('>> Interrupted <<', file=sys.stderr)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--password', dest='password', help='The password to hash')
parser.add_argument('-P', '--password-prompt', dest='password', action=PasswordPrompt, type=str, nargs=0, help='Prompt for the password to hash')
parser.add_argument('-s', '--strength', type=int, help='Number of hashing rounds to create password hash.')
parser.add_argument('-v', '--verify', type=str, help='Verify with the provided hash.')
args = parser.parse_args()

if not args.password:
    print('Error: Please provide a password.', file=sys.stderr)
    parser.print_usage()
    sys.exit(2)
password = args.password.encode('utf-8')
if args.verify:
    verify = args.verify.encode('utf-8')
    if bcrypt.verify(password, verify):
        print('Success!', file=sys.stderr)
        sys.exit(0)
    else:
        print('Passwords did not match.', file=sys.stderr)
        sys.exit(1)
else:
    if args.strength is not None:
        if args.strength < 4:
            print('Error: Strength cannot be less than 4.', file=sys.stderr)
            sys.exit(2)
        bhash = bcrypt.encrypt(password, rounds=args.strength)
    else:
        bhash = bcrypt.encrypt(password)
    print(bhash, end='', flush=True)
    print(file=sys.stderr)
