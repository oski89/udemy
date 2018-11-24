# Error handling

try:
    f = open('testfile2', 'r')
    f.write("Write a test line")
except TypeError:
    print("Hey, there was a TypeError")
except OSError:
    print("Hey, you have an OSError")
except:
    print("All other exceptions!")
finally:
    print("I always run!")


def ask_for_int():

    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number!")
            continue
        else:
            print("Thank you!")
            break
        finally:
            print("End of try/except/finally.")


ask_for_int()
