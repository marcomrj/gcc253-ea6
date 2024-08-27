def backtrack(index, soma_atual, conjunto, used_indices, nums, target, n):
    if soma_atual == target:
        return True, conjunto, used_indices
    if index >= n or soma_atual > target:
        return False, [], []
    encontrado, resultado, indices = backtrack(index + 1,
                                               soma_atual + nums[index],
                                               conjunto + [nums[index]],
                                               used_indices + [index],
                                               nums, target, n)
    if encontrado:
        return True, resultado, indices
    return backtrack(index + 1, soma_atual, conjunto, used_indices, nums, target, n)

def pode_particionar(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False, [], []
    target = total_sum // 2
    n = len(nums)
    return backtrack(0, 0, [], [], nums, target, n)
