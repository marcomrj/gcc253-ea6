def backtrack(index, soma_atual, conjunto, used_indices, nums, target, n):
    if soma_atual == target:
        subconjunto1 = conjunto
        subconjunto2 = [nums[i] for i in range(n) if i not in used_indices]
        return True, subconjunto1, subconjunto2
    if index >= n or soma_atual > target:
        return False, [], []

    encontrado, resultado1, resultado2 = backtrack(index + 1,
                                                   soma_atual + nums[index],
                                                   conjunto + [nums[index]],
                                                   used_indices + [index],
                                                   nums, target, n)
    if encontrado:
        return True, resultado1, resultado2

    return backtrack(index + 1, soma_atual, conjunto, used_indices, nums, target, n)


def pode_particionar(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False, [], []
    target = total_sum // 2
    n = len(nums)
    return backtrack(0, 0, [], [], nums, target, n)