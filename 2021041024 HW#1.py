scores = []


for i in range(5):
    print("%d번째 학생"%(i+1))
    eng = int(input("영어 점수: "))
    clang = int(input("c언어 점수: "))
    py = int(input("파이썬 점수: "))
    sum = eng+clang+py
    avg =  sum/3
    scores.append(sum)
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else :
        grade = 'F'
    print("총점: ",sum, "평균: ",avg, "학점: ",grade, "\n")
    
sorted_scores = sorted(scores, reverse = True)
ranks = [sorted_scores.index(s) + 1 for s in scores]

for i in range(5):
    print("%d 번째 학생: "%(i+1),ranks[i],"등")