def check_quicksort(lists=[35, 50, 15, 25, 80, 20, 90, 45]):
    if len(lists) < 2:
        return lists, 0
    pivot = lists[0]
    start = 1
    end = len(lists) - 1

    while start < len(lists):
        if lists[start] >= pivot:
            while end > 0:
                if lists[end] <= pivot:
                    break
                end -= 1

            #if end <= start:
             #   lists[0], lists[end] = lists[end], lists[0]
              #  break
            #else:
             #   lists[start], lists[end] = lists[end], lists[start]
        elif lists[end] < pivot:
            while start < len(lists):
                if lists[start] >= pivot:
                    break
                start += 1
        if start >= end or end <= start :
            lists[0], lists[end] = lists[end], lists[0]
            break
        else:
            lists[start], lists[end] = lists[end], lists[start]

        start += 1
        end -= 1
    return lists, end


def perform_sorting(lists):
    if len(lists) < 2:
        return lists
    nlist, mid = check_quicksort(lists)
    left = check_quicksort(nlist[mid + 1:])
    right = check_quicksort(nlist[:mid])
    left[0].append(nlist[mid])
    return perform_sorting(right[0]) + perform_sorting(left[0])


check = perform_sorting([11,9,29,7,2,15,28])
print(check)
