def input_info():
    student_info = []
    for i in range(5):
        student_id = input("학번: ")
        student_name = input("이름: ")
        eng_score = int(input("영어: "))
        c_lang_score = int(input("C-언어: "))
        py_score = int(input("파이썬: "))
        student_info.append((student_id, student_name, eng_score, c_lang_score, py_score))
    return student_info

def cal_total_avg(student_info):
    total_scores = []
    for student in student_info:
        total_score = sum(student[2:])
        avg_score = total_score / 3
        total_scores.append((total_score, avg_score)) 
    return total_scores

def cal_grade(avg_score):
    if avg_score >= 95:
        return 'A+'
    elif avg_score >= 90:
        return 'A'
    elif avg_score >= 85:
        return 'B+'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 75:
        return 'C+'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 65:
        return 'D+'
    elif avg_score >= 60:
        return 'D'
    else:
        return 'F'

def cal_rank(total_scores):
    ranked_scores = sorted(total_scores, reverse=True)
    ranks = [ranked_scores.index(score) + 1 for score in total_scores]
    return ranks

def print_student_info(student_info, total_scores, ranks):
    print("{:^90}".format("성적관리 프로그램"))
    print("=" * 90)
    print("{:<10} {:<10} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수"))
    print("=" * 90)
    for i, student in enumerate(student_info):
        print("{:<11} {:<11} {:<8} {:<7} {:<6} {:<6} {:<9} {:<7} {:<10}".format(student[0], student[1], student[2], student[3], student[4], total_scores[i][0], total_scores[i][1], cal_grade(total_scores[i][1]), ranks[i]))

def main():
    student_info = input_info()
    total_scores = cal_total_avg(student_info)
    ranks = cal_rank(total_scores)
    print_student_info(student_info, total_scores, ranks)

if __name__ == "__main__":
    main()
