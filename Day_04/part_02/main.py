from collections import Counter
import time

def main():
    start_time = time.time()
    doShit()
    print("--- %s seconds ---" % (time.time() - start_time))


def doShit():
    MIN = 152085
    MAX = 670283

    good_passwords = set()

    for test_pass in range(MIN, MAX + 1):
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
        digit_counter = Counter(digits)
        if(rule2 and rule3):
            if 2 in digit_counter.values():
                good_passwords.add(test_pass)

    print(f"# of good passwords = {len(good_passwords)}")
    #print(good_passwords)



if __name__ == "__main__":
    main()