
#m4Q1_proj6

score = 4
avgScore = 0
grade = 'A'



for sc in range(score):
    sc = int(input('Enter score: '))
    avgScore += sc/ score
    print(avgScore)

if sc >90 and sc < 100:
    grade = 'A'
elif sc >80 and sc < 89:
    grade = 'B'
elif sc >70 and sc < 79:
    grade = 'C'
elif sc >60 and sc < 69:
    grade = 'D'
elif sc < 60:
    grade = 'F'

print('grade ' + grade)

while avgScore >= 100:
    sc = int(input('Reenter the grade score '))
    


  



