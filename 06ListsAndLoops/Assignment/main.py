def count_falling_grades(percents):
    count = 0
    for percents in percents:
        if percents < 60:
            count = count + 1
    return count

inputlist = ([90,67,4023,59,89])
returnvalue = count_falling_grades(inputlist)
print(returnvalue)

print("################")
def count_act_scores(scores):
    count = 0
    for score in score:
        if score <= 36 and score >= 1:
            count = count + 1 
    return count 

print(count_act_scores([45,12,34,-6]))

print("###############")
def number_sum(numbers):
    total = 0 
    for number in numbers:
        total = total + number
    return total 
print(number_sum([5,3,2,5]))

print("################")
def average_act_score(scores):
        count = 0 
        totalScore = 0 
        for score in scores:
            if score <= 36 and score >= 1:
                count = count + 1
                totalScore = totalScore + score
                avg = totalScore / count
        return avg
print(average_act_score([1,45,23,32,90]))
