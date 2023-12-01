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
print("################")
def all_true(list1):
    for TorF in list1:
        if TorF == "False":
            return False
    else:
        return True 
print(all_true(["True","True","True"]))
print(all_true(["False","False","True"]))
print(all_true(["True","True","True"]))
print("############")
def any_true(list1):
    for TorF in list1:
        if TorF == "True":
            return True 
    else:
        return False
    
print(any_true(["True","True","True"]))
print(any_true(["False","False","True"]))
print(any_true(["False","False","False"]))
print("###########")
def mostly_true(list1):
    TCount = 0
    FCount = 0
    for TorF in list1:
        if TorF == "True":
            TCount == TCount + 1
        elif TorF == "False":
            FCount = FCount + 1
    if TCount > FCount:
        return True
    elif TCount == FCount:
        return "Equal amounts"
    else:
        return False
    
print(mostly_true(["True","False","False","False"]))
print(mostly_true(["True","True","True","False"]))
print(mostly_true(["True","True","False","False"]))

print("###########")

def has_vowel(list1):
    for vowel in list1:
        if vowel in ["a","e","i","o","u"]:
            return True
        else:
            return False 
        
print(has_vowel(["a","t","w"]))
print(has_vowel(["i","g","p"]))
print(has_vowel(["q","r","w"]))


