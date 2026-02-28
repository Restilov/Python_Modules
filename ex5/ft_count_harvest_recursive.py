def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def helper(i,total):
        if i > total:
            return
        print(f"Day {i}")
        helper(i + 1, total)
    helper(1,days)
    print("Harvest time!")