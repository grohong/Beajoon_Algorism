def solution(n, words):
    answer = [0, 0]

    pre_talk = []
    idx = 0

    pre_word = ""
    for word in words:

        if word not in pre_talk and (pre_word == "" or pre_word[-1:] == word[:1]):
            pre_talk.append(word)
            idx += 1
            pre_word = word
        elif word in pre_talk:
            answer = [idx + 1, int(len(pre_talk) / n) + 1]
            break
        elif pre_word != "" and pre_word[-1:] != word[:1]:
            answer = [idx + 1, int(len(pre_talk) / n) + 1]
            break

        if idx == n:
            idx = 0

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))