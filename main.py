import os

LINE = "fix: the 2am version of me left a comment saying 'trust me'; I no longer trust either of us"

# Gate: entry must be 1-200 characters, one line, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip() == LINE

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
