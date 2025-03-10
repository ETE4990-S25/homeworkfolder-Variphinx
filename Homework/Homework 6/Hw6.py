
## David Long

def Run():
    import itertools

    ## basic Lambda Function
    Even = lambda x: 'Even' if x % 2 == 0 else 'Odd'

    print("\nBasic Even or Odd function:")
    print(Even(7)) 
    print(Even(10))  


    ## Sum with Lambda
    SumList = lambda x: sum(x)    ## This was suppose to be more advanced? was I not meant to use sum()?
    aList = [1,2,3,4,5,6,7,8,9,10]

    print("\nSum lambda function:")
    print(f"list: {aList}")
    print(f"Sum of list: {SumList(aList)}")


    # Sorting
    Sorted = lambda x: sorted(x)
    Unsorted = [3, 1, 4, 8, 5, 10, 9, 2, 6, 7]

    print("\nSorted list:")
    print(Sorted(Unsorted))


    # Filtering
    filtered = list(filter(lambda x: x%2 == 0, aList))

    print("\nFiltered lambda function:")
    print(filtered)


    # Mapping
    squares = list(map(lambda x: x ** 2, aList))

    print("\nmapping lambda function:")
    print(squares)


    ## Reduce?? Not part of itertools and not in lecture?
    from functools import reduce   ## From Chatgpts help

    Max = reduce(lambda x, y: x if x>y else y, Unsorted)

    print("\nReduce lambda function to find max value:")
    print(Max)

    # Enumerate
    DaysofWeek = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    enumerated = list(enumerate(DaysofWeek, start=1))

    print("\nEnumerate lambda function (starting at 1):")
    print(enumerated)

    # Zip
    Dates = list(range(1, 32))
    Month = list(zip(Dates, itertools.cycle(DaysofWeek)))

    print("\nEvery day of the month starting with Mon the 1st using zip and cycle:")
    print(Month)
