# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from decimal import Decimal, ROUND_HALF_EVEN

MONEY_PRECISION = Decimal('0.01')

def parse_money(s: str) -> int:
    """Convert '12.34' → 1234 cents"""
    d = Decimal(s).quantize(MONEY_PRECISION, rounding=ROUND_HALF_EVEN)
    return int(d * 100)

def format_money(cents: int) -> str:
    """1234 cents → '$12.34'"""
    return f"${cents / 100:.2f}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
