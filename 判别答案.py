correct='ABCDEF'
socer=0
an=0
answer = str(input('请输入您的答案：'))
while an<=5:
    if answer[an] == correct[an]:
        socer = socer + 1
    else:
        answer = answer.replace(answer[an], 'X')
        print(answer)
    an+=1
if an==6:
    print('判别结果为', answer)
    print('您的得分是', socer)



