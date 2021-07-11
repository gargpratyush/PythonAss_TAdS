def binarysearch(List, x, start, end):

    if end >= start:

        mid = (end + start) // 2

        if List[mid] == x:
            return mid

        elif List[mid] > x:
            return binarysearch(List, x, start, mid - 1)

        else:
            return binarysearch(List, x, mid + 1, end)

    else:
        return 0


n = int(input("Number of elements in your list: "))
List = []

for i in range(0, n):
    a = int(input("Enter the elements: "))
    List.append(a)


L = len(List)

x = int(input("Enter the element you are searching for: "))

List.sort()

print(f"Your list(sorted): {List}")

if binarysearch(List, x, 0, L-1) == 0:
    print("Can't find the required number")

else:
    print(f"Position: {binarysearch(List, x, 0, L-1)}")
