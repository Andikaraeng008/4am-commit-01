import os

LINE = "fix: at 4:12am I finally reproduced the crash by typing the user's password wrong 214 times, exactly like the user did — and the server locked us both out"

# Gate: entry must be 1-200 characters, one line, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip() == LINE

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
