# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def slice_sequences():
    # Use a breakpoint in the code line below to debug your script.
    arr = range(10)
    arr2 = ["{:d}".format(x) for x in arr[:3]]
    print("First 3 elements:" + str(arr2))

    arr3 = ["{:d}".format(x) for x in arr[3:]]
    print("Starting from 3rd element:" + str(arr3))

    arr4 = ["{:d}".format(x) for x in arr[3:-3]]
    print("Starting from 3rd element and ending on 3rd last:" + str(arr4))

    arr4 = ["{:d}".format(x) for x in arr[::2]]
    print("Every even indexed element:" + str(arr4))

    arr5 = ["{:d}".format(x) for x in arr[1::2]]
    print("Every odd indexed element:" + str(arr5))

def enumerate_example():
    arr = range(10)
    print("Enumerate Example")
    for index,element in enumerate(arr):
        print("index:{:d}\telement:{:d}".format(index, element))

def zip_two_lists():
    arr = range(10)
    print("Zip Example")
    arr6 = list('abcdefghij')
    for elem1, elem2 in zip(arr, arr6):
        print("Zip Element1: {:d} Element2: {:s}".format(elem1, elem2))

    arr6.append('k')
    # In Python 2 zip is not lazy
    # In Python 2 and 3 uneven list dont take extra elements
    for elem1, elem2 in zip(arr, arr6):
        print("Uneven Zip Element1: {:d} Element2: {:s}".format(elem1, elem2))

    # in Python 2 its called izip_lo ngest
    from itertools import zip_longest
    for elem1, elem2 in zip_longest(arr, arr6):
        if elem1 is None:
            print("%s is of unknown length" % elem2)
        else:
            print("Uneven Zip_Longest Element1: {:d} Element2: {:s}".format(elem1, elem2))

def else_of_for_loop():
    for x in range(10):
        print("%d" % x)
    else:
        print("Else of For loop.")

    print("\nTry else test 1")
    try:
        raise Exception("test")
        print("Not Reached")
    except Exception as e:
        print("Caught exception %s" % e.__str__())
    else:
        print("Everything is fine")
    finally:
        print("Always runs")

    print("\nTry else test 2")
    try:
        print("No Exception")
    except Exception as e:
        print("Caught exception %s" % e.__str__())
    else:
        print("Everything is fine")
    finally:
        print("Always runs")

    print()
    print("Else doesnt run for for loop when break is called in between")
    for x in range(10):
        if x==2:
            break
        print("%d" % x)
    else:
        print("Else block of for")

    print()
    print("Else runs for for loop empty list is present")
    for x in []:
        print("Wont run")
    else:
        print("Else block of for")

    print()
    print("Else runs for while loop when loop condition is False")
    while False:
        print("Wont run")
    else:
        print("Else block of while")

    print()
    print("Use of else blocks for loops")
    a = 4
    b = 9
    for x in range(2, min(a, b)+1):
        if(a % x ==0 and b % x == 0):
            print("Co Prime %d" % d)
            break
    else:
        print("Not Co Prime")

    print()
    print("Without else of for loop")
    def coprime(x:int, y:int):
        for z in range(2, min(x, y) + 1):
            if (x % z == 0 and y % z == 0):
                print("Co Prime %d" % z)
                return True
        return False
    print("Are a: %d and b: %d coprime? : %s" % (a, b, coprime(a, b)))

def exception_handling():
    print()
    print("Read and write files with exception handling")
    handle = open("/tmp/test-file.txt", 'w', encoding='utf-8')
    handle.write("success\nand\nnew\nlines")
    handle.close()

    handle = open("/tmp/test-file.txt")
    try:
        data = handle.read()
    finally:
        handle.close()
    print("Data: " + data)

    print()
    print("Read Json Key Func")
    import json
    def load_json_key(data, key):
        try:
            result_dict = json.loads(data)  # Could raise Value Error
        except ValueError as e:
            raise KeyError from e
        else:
            return result_dict[key]  # Could raise Key Error

    print("Read Json Key Func Bad Payload")
    try:
        load_json_key('{"foo": bad payload', 'foo')
    except KeyError as e:
        print("Got Key Error")

    print("Read Json Key Func Bad Key")
    try:
        value = load_json_key('{"foo": "bar"}', 'stuff')
        print("Value: %s" % value)
    except KeyError as e:
        print("Got Key Error")

    print("Read file and json read")
    UNDEFINED = object()
    def divide_json(path):
        handle = open(path, 'r+')  # Could Raise IO exception
        try:
            data = handle.read()  # Unicode decode error
            op = json.loads(data)  # Value error
            value = op['numerator']/op['denominator']  # Could raise division by zero exception
        except ZeroDivisionError as e:
            print("ZeroDivisionError occurred: %s" % e.__str__())
            return UNDEFINED
        else:
            op['result'] = value
            result = json.dumps(op)
            handle.write(result)    # Could raise io error
            return value
        finally:
            handle.close()

    temp_path = "/tmp/random_data.json"
    with open(temp_path, 'w') as handle:
        handle.write('{"numerator": 1, "denominator": 0}')

    print("Value returned: %s" % divide_json(temp_path).__str__())

def usage_of_with_and_context_manager():
    print()
    print("Lock Acquire and release")
    from threading import Lock
    lock = Lock()
    with lock:
        print("Lock is held")

    lock.acquire()
    try:
        print("Lock is also held with try")
    finally:
        lock.release()

    import logging
    logging.getLogger().setLevel(logging.WARNING)

    logging.warning("With Context manager")

    def my_func():
        logging.debug("Some debug info")
        logging.error("A real error")
        logging.debug("More debugging")

    my_func() # Context can boost log level

    from contextlib import contextmanager
    import logging

    print("")
    print("With context manager")
    @contextmanager
    def debug_logging(level):
        logger = logging.getLogger()
        old_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        try:
            yield  #
        finally:
            logger.setLevel(old_level)

    with debug_logging(logging.DEBUG):
        my_func()

    import logging
    @contextmanager
    def swallow_exception(cls):
        try:
            yield
        except cls:
            logging.exception("Swallowing exception")  # print stack trace

    value = 20
    with swallow_exception(ZeroDivisionError):
        value /= 0
    print('Done')

    @contextmanager
    def log_level(level, name):
        logger = logging.getLogger(name)
        old_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        try:
            yield  logger
        finally:
            logger.setLevel(old_level)

    with log_level(logging.DEBUG, 'my-test-app') as logger:
        logging.debug("test-logging")
        logger.debug("test-logger")

    logging.debug("test-logging-2")
    logger.debug("test-logger-2")
    logging.error("test-logging-2")
    logger.error("test-logger-2")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    slice_sequences()
    enumerate_example()
    zip_two_lists()
    else_of_for_loop()
    exception_handling()
    usage_of_with_and_context_manager()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
