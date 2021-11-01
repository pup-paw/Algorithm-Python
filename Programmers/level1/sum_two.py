def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return answer
