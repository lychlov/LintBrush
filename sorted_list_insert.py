class Solution:
    def sorted_list_insert(self, sorted_list, n):
        if len(sorted_list) <= 1:
            sorted_list.append(n)
            return sorted_list
        if sorted_list[0] <= sorted_list[-1]:
            if n <= sorted_list[0]:
                sorted_list.insert(0, n)
                return sorted_list
            if n >= sorted_list[-1]:
                sorted_list.append(n)
                return sorted_list
        else:
            if n >= sorted_list[0]:
                sorted_list.insert(0, n)
                return sorted_list
            if n <= sorted_list[-1]:
                sorted_list.append(n)
                return sorted_list
        for i in range(len(sorted_list) - 1):
            if (sorted_list[i] <= n <= sorted_list[i + 1]) or (sorted_list[i] >= n >= sorted_list[i + 1]):
                sorted_list.insert(i + 1, n)
                return sorted_list


sol = Solution()
print(sol.sorted_list_insert([1, 1, 1, 1, 1], 10))
print(sol.sorted_list_insert([9, 7, 5, 4, 3, 1], 100))
