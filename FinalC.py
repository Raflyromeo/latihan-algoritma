import sys

def main():
    s = sys.stdin.readline().strip()
    sorted_chars = sorted(s)
    print(''.join(sorted_chars))

if __name__ == "__main__":
    main()
