# This is a sample Python script.
import json


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def closure_interaction_variable_scope():
    numbers = [8, 3, 1, 5, 2, 4, 7, 6, 9]
    group = {2, 3, 5, 7}
    def sort_custom(numbers, group):
        found = False
        def helper(x):
            # Adding "nonlocal" keyword uses the variable from parent scope
            # nonlocal should not be used normally
            # nonlocal only exist in python 3
            nonlocal found
            if x in group:
                found = True
                return (0, x)
            return (1, x)
        numbers.sort(key = helper)
        return found
    print(sort_custom(numbers, group))
    print(numbers)

    # The above can be done as below with the help of a class
    class Sorter(object):
        def __init__(self, group):
            self.found = False
            self.group = group

        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)
            return (1, x)

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    print("Numbers using Class Sorter")
    print(numbers)

    def sorting_order():
        meep=25
        def enclosing():
            foo=15
            def my_func():
                bar=10
                print("bar %d" % bar)
                print("foo %d" % foo)
                print("meep %d" % meep)
                print(str)
                ##print(do_not_exist)
            my_func()
        enclosing()
    sorting_order()

    def defining_variables():
        def enclosing():
            foo = 15  # Defined and initialized
            foo = 25  # Re-Initialized
            def my_func():
                foo = 10  # Re-Defined and initialized
                bar = 5  # Defined and initialized
                print("my_func bar %d" % bar)
                print("my_func foo %d" % foo)
            print("enclosing before my_func call foo %d" % foo)
            #print("enclosing bar %d" % bar) # Gives error since closure doesnt contian bar
            my_func()
            print("enclosing after my_func call foo %d" % foo)
        enclosing()
    defining_variables()


def accept_functions_for_simple_interfaces_instead_of_classes():
    names = ['Shivanshu', 'Ginni', 'Pooja', 'Mummy', 'Papa']
    names.sort(key=lambda x: len(x))
    print(names)

    def increment_and_return(current, increments):
        from collections import defaultdict
        added_count = 0
        def helper():
            nonlocal added_count
            added_count += 1
            return 0
        d = defaultdict(helper, current)
        for key, value in increments:
            d[key] += value
        return d, added_count

    def increment_and_return_with_class(current, increments):
        from collections import defaultdict

        class CountMissing(object):
            def __init__(self):
                self.added_count = 0

            def __call__(self):
                self.added_count += 1
                return 0

        count_missing = CountMissing()
        #d = defaultdict(count_missing.missing, current)
        d = defaultdict(count_missing, current)
        for key, value in increments:
            d[key] += value
        return d, count_missing.added_count

    current = {"green": 12, "orange": 5, "blue": 3}
    increments = [("red", 10), ("orange", 2), ("yellow", 12)]
    print("Without Class")
    print(increment_and_return(current, increments))
    print("With Class")
    print(increment_and_return_with_class(current, increments))

def reduce_visual_noise_with_variable_positioning_arguments():
    def log(message, values):
        if not values:
            print(message)
        else:
            print("%s:%s" % (message, ','.join([str(x) for x in values])))

    log("This is a message", [1, 2, 3])
    log("This is message 2", [])

    print()
    print("To make second parameter optional")
    def log_with_optional_parameter(message, *values):
        if not values:
            print(message)
        else:
            print("%s:%s" % (message, ','.join([str(x) for x in values])))

    log_with_optional_parameter("This is a message", 1, 2, 3)
    log_with_optional_parameter("This is message 2")

    favourites = [8, 27, 99]
    print()
    log_with_optional_parameter("This is a message", favourites)
    log_with_optional_parameter("This is a message", *favourites)

    def get_favourites():
        for x in range(10):
            yield str(x)
    print()
    log_with_optional_parameter("This is a message", *get_favourites())

    def log_with_optional_parameter_with_additional_parameter(seq, message, *values):
        if not values:
            print("%s:%s" % (seq, message))
        else:
            print("%s:%s:%s" % (seq, message, ','.join([str(x) for x in values])))

    print()
    log_with_optional_parameter_with_additional_parameter("Old wrong way to call but still working", *get_favourites())
    log_with_optional_parameter_with_additional_parameter(1, "New Right way to call", *get_favourites())

def provide_optional_behaviour_with_keyword():
    def remainder(numerator, denominator):
        return numerator % denominator
    print(remainder(20, 7))
    print(remainder(numerator=20, denominator=7))
    print(remainder(denominator=7, numerator=20))

    def flow_rate(weight_diff, time_diff, period = 1, unit_per_lb = 1):
        return ((weight_diff / unit_per_lb) / time_diff) * period

    print("%.3f kg per second" % flow_rate(0.5, 3))
    print("%.3f kg per hour" % flow_rate(0.5, 3, period=3600))
    print("%.3f kg per hour" % flow_rate(0.5, 3, period=3600, unit_per_lb=2.2))

def enforce_clarity_withkeyword_only_argument():
    def safe_division(number, divisor, *, ignore_overflow, ignore_zero_division):
        try:
            return number / divisor
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    # Gives Overflow exception Exception
    # print(safe_division(1.0, 10**500, False, False))
    # Gives Type error since * was added in the param list of safe_division function
    # print(safe_division(1.0, 10**500, True, False))
    print(safe_division(1.0, 10 ** 500, ignore_overflow=True, ignore_zero_division=False))
    # Gives Exception
    # print(safe_division(1.0, 0, False, False))
    # Gives Type error since * was added in the param list of safe_division function
    # print(safe_division(1.0, 0, False, True))
    print(safe_division(1.0, 0, ignore_overflow=False, ignore_zero_division=True))

    print()

    def safe_division_with_kwargs(number, divisor, **kwargs):
        ignore_overflow = kwargs.pop("ignore_overflow", False)
        ignore_zero_division = kwargs.pop("ignore_zero_division", False)
        if kwargs:
            raise TypeError("Unexpected kwargs %r passed" % kwargs)
        try:
            return number / divisor
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    # Gives Overflow exception Exception
    # print(safe_division(1.0, 10**500, False, False))
    # Gives Type error since * was added in the param list of safe_division function
    # print(safe_division(1.0, 10**500, True, False))
    print(safe_division_with_kwargs(1.0, 10 ** 500, ignore_overflow=True, ignore_zero_division=False))
    # Gives Exception
    # print(safe_division(1.0, 0, False, False))
    # Gives Type error since * was added in the param list of safe_division function
    # print(safe_division(1.0, 0, False, True))
    print(safe_division_with_kwargs(1.0, 0, ignore_overflow=False, ignore_zero_division=True))
    # Throws "TypeError: Unexpected kwargs {'bad': 'value'} passed" when passed
    # print(safe_division_with_kwargs(1.0, 0, ignore_overflow=False, ignore_zero_division=True, bad='value'))

def use_none_and_docstrings_to_specify_dynamic_default_args():
    from datetime import datetime
    from time import sleep
    def log(message, when=datetime.now()):
        print("%s:%s" % (when, message))

    log("Message 1")
    sleep(1)
    log("Message 2")  # time is same in both log message

    print()
    # Video Solution
    def log_with_correction_and_doc(message, when = None):
        """Log a message at certain time.

        Args:

        :param message: Message to print
        :param when: datetime of when the message occurred. Defaults to the present time
        :return:
        """
        if when is None:
            when = datetime.now()
        print("%s:%s" % (when, message))

    log_with_correction_and_doc("Message 1")
    sleep(1)
    log_with_correction_and_doc("Message 2")

    print()
    # My solution
    def log_func_pass(message, when=datetime.now):
        print("%s:%s" % (when(), message))

    log_func_pass("Message 1")
    sleep(1)
    log_func_pass("Message 2")

    def decode(data, default={}):
        try:
            return json.loads(data)
        except ValueError:
            return default

    foo = decode("bad data")
    foo['stuff'] = 1
    print("foo: %s" % str(foo))
    bar = decode("other bad data")
    bar['other stuff'] = 2
    print("bar: %s" % str(bar))
    print("foo: %s" % str(foo))

    print()

    def decode_with_correction_and_doc(data, default=None):
        """Decodes JSON data and returns default if its bad

        :param data: Data to decode
        :param default: Value to return if decoding fails. Defaults to any empty dict.
        :return:
        """
        if default is None:
            default = {}
        try:
            return json.loads(data)
        except ValueError:
            return default

    foo = decode_with_correction_and_doc("bad data")
    foo['stuff'] = 1
    print("foo: %s" % str(foo))
    bar = decode_with_correction_and_doc("other bad data")
    bar['other stuff'] = 2
    print("bar: %s" % str(bar))
    print("foo: %s" % str(foo))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    closure_interaction_variable_scope()
    accept_functions_for_simple_interfaces_instead_of_classes()
    reduce_visual_noise_with_variable_positioning_arguments()
    provide_optional_behaviour_with_keyword()
    enforce_clarity_withkeyword_only_argument()
    use_none_and_docstrings_to_specify_dynamic_default_args()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
