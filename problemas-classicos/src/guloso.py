def particao_gulosa(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        # Retornar listas vazias se a soma total é ímpar
        return [], []
    nums.sort(reverse=True)
    conjunto1, conjunto2 = [], []
    soma1, soma2 = 0, 0

    # Itera sobre cada número na lista ordenada
    for num in nums:
        if soma1 <= soma2:
            conjunto1.append(num)
            soma1 += num
        else:
            conjunto2.append(num)
            soma2 += num
    return conjunto1, conjunto2
