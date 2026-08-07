class Solution:
    def smallestNumber(self, num, t):
        kFactorCounts = {
            0: {}, 1: {}, 2: {2: 1}, 3: {3: 1}, 4: {2: 2},
            5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1}, 8: {2: 3}, 9: {3: 2},
        }

        def get_prime_count(t):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while t % p == 0:
                    t //= p
                    count[p] += 1
            return count, t == 1

        def get_prime_count_from_string(s):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for ch in s:
                for p, f in kFactorCounts[int(ch)].items():
                    count[p] += f
            return count

        def get_factor_count(count):
            count8 = count[2] // 3
            remaining2 = count[2] % 3
            count9 = count[3] // 2
            count3 = count[3] % 2
            count4 = remaining2 // 2
            count2 = remaining2 % 2
            count6 = 0
            if count2 == 1 and count3 == 1:
                count2, count3, count6 = 0, 0, 1
            if count3 == 1 and count4 == 1:
                count2, count6, count3, count4 = 1, 1, 0, 0
            return {
                2: count2, 3: count3, 4: count4, 5: count[5],
                6: count6, 7: count[7], 8: count8, 9: count9,
            }

        def construct(factors):
            return ''.join(str(d) * factors.get(d, 0) for d in range(2, 10))

        def is_subset(a, b):
            return all(b.get(k, 0) >= v for k, v in a.items())

        def subtract(a, b):
            res = dict(a)
            for k, v in b.items():
                res[k] = max(0, res.get(k, 0) - v)
            return res

        def sum_values(count):
            return sum(count.values())

        prime_count, is_divisible = get_prime_count(t)
        if not is_divisible:
            return "-1"

        factor_count = get_factor_count(prime_count)
        if sum_values(factor_count) > len(num):
            return construct(factor_count)

        n = len(num)
        prime_count_prefix = get_prime_count_from_string(num)
        first_zero_index = num.find('0')
        if first_zero_index == -1:
            first_zero_index = n
            if is_subset(prime_count, prime_count_prefix):
                return num

        for i in range(n - 1, -1, -1):
            d = int(num[i])
            prime_count_prefix = subtract(prime_count_prefix, kFactorCounts[d])
            space_after = n - 1 - i
            if i > first_zero_index:
                continue
            for bigger_digit in range(d + 1, 10):
                needed = subtract(subtract(prime_count, prime_count_prefix),
                                   kFactorCounts[bigger_digit])
                factors_after = get_factor_count(needed)
                if sum_values(factors_after) <= space_after:
                    fill_ones = space_after - sum_values(factors_after)
                    return (num[:i] + str(bigger_digit) +
                            '1' * fill_ones + construct(factors_after))

        factors_after_extension = get_factor_count(prime_count)
        pad = n + 1 - sum_values(factors_after_extension)
        return '1' * pad + construct(factors_after_extension)