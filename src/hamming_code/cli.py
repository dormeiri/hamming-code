import argparse

from src.hamming_code import fix, detect, decode, encode

COMMANDS = {
    "encode": encode,
    "decode": decode,
    "detect": detect,
    "fix": fix
}


def data(s):
    if any(ch not in ["1", "0"] for ch in s):
        raise ValueError
    return list(map(int, s))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=COMMANDS)
    parser.add_argument("data", type=data)
    args = parser.parse_args()
    result = COMMANDS[args.command](args.data)
    print(result)


if __name__ == "__main__":
    main()
