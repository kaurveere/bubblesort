# Array with 100 elements
array_with_100_elements = [842, 152, 969, 780, 496, 845, 91, 23, 763, 455,
            615, 577, 500, 198, 823, 684, 295, 632, 116, 730,
            336, 728, 401, 176, 582, 961, 916, 248, 810, 975,
            546, 402, 751, 638, 185, 358, 665, 983, 328, 160,
            439, 912, 389, 773, 800, 140, 223, 873, 293, 365,
            349, 453, 996, 241, 472, 618, 258, 762, 922, 145,
            236, 721, 594, 721, 81, 633, 432, 291, 664, 557,
            267, 929, 168, 985, 385, 866, 112, 726, 301, 604,
            239, 169, 910, 774, 986, 962, 424, 784, 288, 631,
            530, 306, 596, 312, 810, 989, 869, 111, 674, 940]


array = array_with_100_elements*100 #Change this constant


def bubble_sort(arr):
   for n in range(len(arr) - 1, 0, -1):
       swapped = False
       for i in range(n):
           if arr[i] > arr[i + 1]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
               swapped = True
       if not swapped:
           break


# Sorting
print("Efficient sorting started")
bubble_sort(array)
print(f"Efficient sorting finished")