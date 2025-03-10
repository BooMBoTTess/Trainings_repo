def presses(phrase: str):
    phone = ['1adgjmptw* #', 'behknqux0', 'cfilorvy', '234568sz', '79']
    phrase = phrase.lower()
    score = 0
    for letter in phrase:
        for i in range(len(phone)):
            if phone[i].find(letter) != -1:
                score += i+1
    return score

if __name__ == '__main__':
    assert presses('z') == 4
    assert presses('9') == 5
    assert presses('2') == 4
    print('_'*20)
    assert presses('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 56