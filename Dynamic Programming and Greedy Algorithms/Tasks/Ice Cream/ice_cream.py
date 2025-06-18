def ice_cream( T ):
    def counting_sort(input_array):
        M = max(input_array)
        count_array = [0] * (M + 1)

        for num in input_array:
            count_array[num] += 1

        for i in range(1, M + 1):
            count_array[i] += count_array[i - 1]

        output_array = [0] * len(input_array)

        for i in range(len(input_array) - 1, -1, -1):
            output_array[count_array[input_array[i]] - 1] = input_array[i]
            count_array[input_array[i]] -= 1

        return output_array

    n = len(T)
    T = counting_sort(T)[::-1]
    melt = 0
    result = 0
    
    for i in range(n):
        if T[i] - melt <= 0:
            break

        result += T[i] - melt
        melt += 1

    return result