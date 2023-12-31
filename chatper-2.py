# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def list_comprehension_and_lambda():
    a = range(10)
    print("list comprehensions")
    squares = [x**2 for x in a]
    print(squares)

    print("lambda")
    squares_map = map(lambda x: x**2, a)
    print(list(squares_map))

    print("list comprehensions with filter")
    squares_filter = [x ** 2 for x in a if x % 2 == 0 ]
    print(squares_filter)
    print(type(squares_filter))

    print("lambda with filter")
    squares_map_filter = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
    print(list(squares_map_filter))
    print(type(squares_map_filter))

    print("Reverting a dict")
    chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    reverted_chile_ranks = {rank: name for name, rank in chile_ranks.items()}
    print(reverted_chile_ranks)
    print(type(reverted_chile_ranks))

    print("Creating a set")
    set_of_chile_name_lengths = {len(name) for name in chile_ranks.keys()}
    print(set_of_chile_name_lengths)
    print(type(set_of_chile_name_lengths))

def list_comprehension_continued():
    print("Multiple levels of looping")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)

    print("Replicate 2 level of matrix")
    squares = [[x**2 for x in row] for row in matrix]
    print(squares)

    matrix_level3 = [
        [[1, 2, 3],  [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]]
    ]

    flat = [x for sublist1 in matrix_level3
            for sublist2 in sublist1
            for x in sublist2]

    print(flat)

    flat = []
    for sublist1 in matrix_level3:
        for sublist2 in sublist1:
            flat.extend(sublist2)

    print(flat)

    print("Filtering with list expressions")
    a = range(10)
    b = [x for x in a if x > 5 and x % 2 == 0]
    c = [x for x in a if x > 5 if x % 2 == 0]
    print(b)
    print(c)
    assert b == c

    filtered_matrix = [[x for x in row if x % 3 == 0]
                       for row in matrix if sum(row) >= 10]
    print("Multiple level filtering")
    print(filtered_matrix)

    print("Avoid using more than 2 complex expressions in list comprehensions")

def generator_expressions():
    import random
    with open("/tmp/files_tmp.txt", 'w') as f:
        for _ in range(10):
            f.write('a' * random.randint(1, 100))
            f.write("\n")

    value = [len(x) for x in open("/tmp/files_tmp.txt")]
    print("Comparing with generator expressions")
    print(value)

    print()
    print("Looping over iterator")
    value_iterator = (len(x) for x in open("/tmp/files_tmp.txt"))
    is_loop_completed = False
    while not is_loop_completed :
        try:
            print("value\t" + str(next(value_iterator)))
        except StopIteration as e:
            print("Exception occurred")
            is_loop_completed = True

    value_iterator = (len(x) for x in open("/tmp/files_tmp.txt"))
    sqrt = ((x, x**0.5) for x in value_iterator)
    is_loop_completed = False
    while not is_loop_completed:
        try:
            print("sqrt\t" + str(next(sqrt)))
        except StopIteration as e:
            print("Exception occurred")
            is_loop_completed = True

def consider_generators_instead_of_returning_lists():
    print("Without Generators")
    def index_words(text):
        result = []
        if text:
            result.append(0)
        for index, word in enumerate(text):
            if word == ' ':
                result.append(index + 1)
        return result
    sentence = "As he entered the church he could hear the soft voice of someone whispering into a cell phone."
    print(index_words(sentence))

    print("With Generators")
    def index_words_with_generators(text):
        if text:
            yield 0
        for index, word in enumerate(text):
            if word == ' ':
                yield index + 1
    sentence = "As he entered the church he could hear the soft voice of someone whispering into a cell phone."
    it = index_words_with_generators(sentence)
    is_loop_completed = False
    while not is_loop_completed:
        try:
            print("index\t" + str(next(it)))
        except StopIteration as e:
            print("Exception occurred")
            is_loop_completed = True

def being_defensive_while_iterating():
    a = [15, 80, 16]  # Population of a city in a year
    print("Percentage of population of the total")
    def calc_perc(data):
        total = sum(data)  # Iteration 1
        return [100 * (x/total) for x in data]  # Iteration 2
    print(calc_perc(a))

    print("For large values")
    def calc_perc_iter(get_iter):
        total = sum(get_iter())  # Iteration 1
        return [100 * (x/total) for x in get_iter()]  # Iteration 2

    with open("/tmp/population.txt",'w') as f:
        for x in a:
            f.write("%d\n" % x)
    def read_population_numbers():
        with open("/tmp/population.txt") as f:
            for line in f:
                yield int(line)

    get_iter = lambda: read_population_numbers()
    print(calc_perc_iter(get_iter))  # Reading the file twice
    print(calc_perc_iter(get_iter))

    print("Override __iter__ and __next__")
    class ReadVisits:

        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

        def __init__(self, data_path):
            self.data_path = data_path

    visits = ReadVisits("/tmp/population.txt")
    print(calc_perc(visits))  # Doesnt fail since __iter__ is called twice with sum and for loop which reads the file twice

    print()
    print("Same Object is returned for multiple iter operations on the same visits object")
    it = iter(visits)
    it2 = iter(it)
    print(it)
    print(it2)

    print()
    print("Different objects are returned for the when iter 2 new objects are created from visits object")
    it = iter(visits)
    it2 = iter(visits)
    print(it)
    print(it2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_comprehension_and_lambda()
    list_comprehension_continued()
    generator_expressions()
    consider_generators_instead_of_returning_lists()
    being_defensive_while_iterating()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
