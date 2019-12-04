from collections import Counter

def main():
    MIN = 152085
    MAX = 670283

    MIN = 155555
    MAX = 669999
    good_passwords = [MIN, MAX]

    for test_pass in range(MIN, MAX):
        rule2 = False
        rule3 = True
        digits = [int(i) for i in str(test_pass)]
        last_dig = 0
        curr_dig = 0
        for i in range(0, 6):
            curr_dig = digits[i]
            if(curr_dig < last_dig):
                rule3 = False
            if((curr_dig == last_dig) and not rule2):
                rule2 = True
            last_dig = curr_dig
        if(rule2 and rule3):
            good_passwords.append(test_pass)


    final_passwords = []
    for test_pass in good_passwords:
        digits = [int(i) for i in str(test_pass)]
        digit_counter = Counter(digits)
        if 2 in digit_counter.values():
            final_passwords.append(test_pass)

    print(f"# of good passwords = {len(final_passwords)}")
    #print(good_passwords)



if __name__ == "__main__":
    main()