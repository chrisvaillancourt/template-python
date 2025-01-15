def main():
    print(hello("python!"))


def hello(string: str) -> str:
    return f"Hello {string}"


if __name__ == "__main__":
    main()
