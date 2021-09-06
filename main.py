from logic.add import DollarAdder


def main(raw_input: str = input("Paste text here containing Dollar ($) amounts to add: ")):
    print(DollarAdder().get_dollar_amts(raw_input))
    return


if __name__ == '__main__':
    main()
