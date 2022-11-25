n = int(input())
answers = []
score = 0

for i in range(n):
    answers.append(input())

for j in range(n):
    if input() == answers[j]:
        score += 1

print(score)