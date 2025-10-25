"""
CS1 Lab 5, 2251
Instructor: Tony Audi
Author: Abdulaziz
"""

def file_type(fn: str):
   end = fn[-5:]
   if ".txt" in end:
       print("Text")
       return "text"
   elif ".mud" in end:
       print("Mud")
       return "mud"
   else:
       print("Neither")
       return "neither"


def other_filename(fn: str):
   end = fn[-5:]
   if ".txt" in end:
       new_fn = fn[:-4] + ".mud4"
       return new_fn
   elif ".mud" in end:
       new_fn = fn[:-5] + ".2.txt"
       return new_fn

def shift(s, n):
    new_str=""
    for ch in s:
        num=ord(ch)
        num+=n
        new_str+=chr(num)
    return new_str


def muddle(s, n, keyword):
    new_str = ""
    for ch in s:
        if ch in keyword:
            num = ord(ch)
            num += 110 + n
            new_str += chr(num)
        else:
            num = ord(ch)
            num += n
            new_str += chr(num)
    return new_str

def clarify(s, n):
    new_str = ""
    for ch in s:
        num=ord(ch)
        if num <= 135:
            num -= n
        else:
            num -= (n + 110)
        new_str += chr(num)
    return new_str

def test_muddle():
    if muddle("hello", 3, "he") == "ÙÖoor":
        print("Test passed")
    else:
        print("Test failed")
    if muddle("Read!", 3, "Re") == "ÃÖdg$":
        print("Test passed")
    else:
        print("Test failed")
    if muddle("Muddle", 3, "le") == "PxggÝÖ":
        print("Test passed")
    else:
        print("Test failed")
    if muddle("Aziz", 2, "z") == "Cêkê":
        print("Test passed")
    else:
        print("Test failed")
    if muddle("Programming is fun", 8, "m") == "Xzwoziããqvo(q{(n}v":
        print("Test passed")
    else:
        print("Test failed")
    if clarify("ÙÖoor", 3) == "hello":
        print("Test passed")
    else:
        print("Test failed")
    if clarify("ÃÖdg$", 3) == "Read!":
        print("Test passed")
    else:
        print("Test failed")
    if clarify("PxggÝÖ", 3) == "Muddle":
        print("Test passed")
    else:
        print("Test failed")
    if clarify("Cêkê", 2) == "Aziz":
        print("Test passed")
    else:
        print("Test failed")
    if clarify("Xzwoziããqvo(q{(n}v", 8) == "Programming is fun":
        print("Test passed")
    else:
        print("Test failed")


def main():
    infile = input("Enter the input file name: ").strip()

    with open(infile, "r") as f:
        contents = f.read()

    ftype = file_type(infile)
    if ftype == "neither":
        print("Error; invalid file type")
        return

    elif ftype == "text":
        while True:
            offset = int(input("Enter offset (1-9): "))
            if 1 <= offset <= 9:
                break
            else:
                print("Invalid offset, try again.")
        output = shift(contents, offset)
        outfile = infile[:-4] + f".mud{offset}"

    elif ftype == "mud":
        offset = int(infile[-1])  # assumes the last character is the number
        output = clarify(contents, offset)
        outfile = other_filename(infile)

    choice = input(f"Enter 'y' to write results to file {outfile}: ")
    if choice == "y":
        with open(outfile, "w") as f:
            f.write(output)
        print(f"Results written to {outfile}")
    else:
        print(output)

if __name__ == "__main__":
    main()