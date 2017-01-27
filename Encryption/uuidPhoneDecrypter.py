import sys
import uuid
import time
import argparse
import itertools

# UUID Phone Decrypter
# Author: Summon Agus (github.agusmakmun)
# MIT License


def UUIDecrypter(hash='sha1', salt=None, key=None, spliter=None):
    """
    Explanation:
    1. `NAMESPACE_DNS` only found at UUID3 and UUID5, so you need to try both.
        the UUID3 using MD5 hash, and the UUID5 using SHA-1 hash.

    2. `hash` string hash type, usage for `sha1` or `md5`. by default is `sha1`.

    3. `salt` is a reference to the base of a telephone numbers, for examples:
        0857, 0878, 0813, 0821 or etc.

    4. `key` is hex key from the uuid.
        >>> import uuid
        >>> uuid.uuid5(uuid.NAMESPACE_DNS, '0821-0120-2902').hex
        '0fce9b8a388354fa8990f168b873dfd0'

    5. `spliter` is used for formatting telephone numbers.
        generally telephone numbers using separators such as `-` on every 4 digits.
        but some others are not used it.

    6. `phone_range` a phone number that generally amounts to 12 digits.
        in this situation, if the `salt` is not None, so, actually you just need
        to decrypt the keys starting from the `salt`.

    Example:
        $ python3 uuidPhoneDecrypter.py --hash=sha1 --salt=0821 --key=0fce9b8a388354fa8990f168b873dfd0 --spliter=-
        [i] starting at 10:43:25
        [i] tying 0821-0120-2902 : 0fce9b8a388354fa8990f168b873dfd0
        [i] phone number found `0821-0120-2902`
        [i] end at 10:44:44
    """
    string_digits = '0123456789'
    phone_range = 12

    if salt is not None:
        phone_range = phone_range - len(salt)

    print("[i] starting at {}".format(time.strftime("%H:%M:%S")))
    time.sleep(2)

    try:
        for n in range(phone_range, phone_range + 1):
            for xs in itertools.product(string_digits, repeat=n):
                phone = ''.join(xs)

                if salt is not None:
                    phone = str(salt) + phone

                if spliter is not None:
                    left = phone[:4]
                    center = phone[4:8]
                    right = phone[8:]
                    phone = str(spliter).join([left, center, right])

                if hash.lower() == 'md5':
                    bruteForceUUID = uuid.uuid3(uuid.NAMESPACE_DNS, phone).hex
                elif hash.lower() == 'sha1':
                    bruteForceUUID = uuid.uuid5(uuid.NAMESPACE_DNS, phone).hex

                sys.stdout.write("\r[i] tying {0} : {1}".format(phone, bruteForceUUID))
                sys.stdout.flush()

                if key == bruteForceUUID:
                    print("\n[i] phone number found `{}`".format(phone))
                    print("[i] end at {}".format(time.strftime("%H:%M:%S")))
                    sys.exit()

    except KeyboardInterrupt:
        print("\n[!] aborted!")
        sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='UUID Phone Decrypter for MD5 hash and SHA-1 hash.\n'
        '\n Usage Example: \n'
        ' $ python3 %(file)s --hash=<hash> --salt=<salt> --key=<key> --spliter=<spliter>\n'
        ' $ python3 %(file)s --hash=sha1 --salt=0821 --key=0fce9b8a38835...* --spliter=-\n' % {
            'file': __file__}
    )
    parser.add_argument(
        '--hash', default='sha1',
        help='string hash type, usage for `sha1` or `md5`. by default is `sha1`')
    parser.add_argument(
        '--salt', default=None,
        help='is a reference to the base of a telephone numbers,\n'
             'for examples: `0857`, `0878`, `0813`, `0821` or etc. by default is None')
    parser.add_argument(
        '--key', help='is hex key from the uuid.\n'
        'an example: 0fce9b8a388354fa8990f168b873dfd0')
    parser.add_argument(
        '--spliter', default=None,
        help='optional character separators used for formatting telephone numbers.\n'
             'generally telephone numbers using separators such as `-` on every 4 digits.\n'
             'but some others are not used it.')

    args = parser.parse_args()
    if args.key is None:
        parser.print_help()
        sys.exit()
    UUIDecrypter(args.hash, args.salt, args.key, args.spliter)
