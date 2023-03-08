
#m4Q1_proj6

score = 4
avgScore = 0
grade = 'A'
tScore = 0

while avgScore <= 100: 
    for sc in range(score):
            sc = int(input('Enter score: ')) 
            tScore = sc + tScore # cal total score entered
            avgScore = tScore / score    # get average score
    print('average ' + str(avgScore))

    if avgScore > 100:
        print('Reenter the grade score ')
    elif avgScore >= 90 and avgScore < 100:
        grade = 'A'
    elif avgScore >= 80 and avgScore < 90:
        grade = 'B'
    elif avgScore >= 70 and avgScore < 80:
        grade = 'C'
    elif avgScore >= 60 and avgScore < 70:
        grade = 'D'
    else:
        grade = 'F'    
  
    print('grade ' + grade)



  



