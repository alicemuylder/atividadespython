def is_valid(s):
    if len(s) < 2 or not s[:2].isalpha():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if any(char.isdigit() for char in s[2:-1]) or s[2].isdigit():
        return False

    if any(char in '.!@#$%^&*()-_+=<>?/\|~`' for char in s):
        return False

    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()