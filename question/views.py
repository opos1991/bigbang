from django.shortcuts import render
from .models import Exam
from bs4 import BeautifulSoup
# Create your views here.

def exam(request):
    content = dict()
    tp = dict()
    # 考试界面题
    soup = BeautifulSoup(open('static/index.html', encoding='UTF-8'))
    for b in soup.find_all('b'):
        s = b.string.split('.')
        if s[0] == '网络部测试题':
            pass
        else:
            text = s[1]
            questions = Exam.objects.filter(question__icontains=text)
            tp[s[0]] = questions

    content['tp'] = tp
    return render(request, 'question/exam.html', content)
    # 搜索题部分
    #
    # qus = request.POST.get('text', '')
    # if qus == '':
    #     return render(request, 'question/exam.html', {})
    # else:
    #     question = Exam.objects.filter(question__icontains=qus)
    #     content['question'] = question
    #     print(content['question'])
    #     return render(request, 'question/exam.html', content)

