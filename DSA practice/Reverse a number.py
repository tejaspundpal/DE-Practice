if __name__ == "__main__":
    class NumberReverser:
        def reverseNumber(self, n):
            revNum = 0
            while n > 0:
                lastDigit = n % 10
                revNum = (revNum * 10) + lastDigit
                n = n // 10
            return revNum

    num = 121
    reverser = NumberReverser()
    reversed_num = reverser.reverseNumber(num)
    print(f"Reversed number of {num} is {reversed_num}")