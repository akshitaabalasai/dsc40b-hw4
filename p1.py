def knn_distance(arr, q, k):
    def dist(num):
        return abs(num - q)

    def split(nums, start, end, pivot):
        pivot_dist = dist(nums[pivot])

        nums[pivot], nums[end] = nums[end], nums[pivot]

        spot = start
        for curr in range(start, end):
            if dist(nums[curr]) < pivot_dist:
                nums[spot], nums[curr] = nums[curr], nums[spot]
                spot += 1

        nums[spot], nums[end] = nums[end], nums[spot]
        return spot

    def select(nums, start, end, wanted):
        while start <= end:
            pivot = (start + end) // 2
            pivot = split(nums, start, end, pivot)

            if pivot == wanted:
                return nums[pivot]
            if wanted < pivot:
                end = pivot - 1
            else:
                start = pivot + 1

    wanted = k - 1
    point = select(arr, 0, len(arr) - 1, wanted)
    return (abs(point - q), point)
