def main() -> None:
    phones: list = [
        "Xiaomi Redmi Note 10S",
        "Смартфон Xiaomi Redmi Note 10 Pro",
        "Apple iPhone 13",
        "Apple iPhone 11",
        "Huawei nova Y70",
        "Смартфон Apple iPhone 13 Pro"
    ]

    apple_phones: list = [phone for phone in phones if "apple" in phone.lower()]
    print(*apple_phones, sep='\n')


if __name__ == '__main__':
    main()
