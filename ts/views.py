from django.shortcuts import render
from django.http import HttpResponse
import re
from django.db.models import Max
from rest_framework import generics

from .models import Index
from .serializers import HomeSerializer


temp = Index.objects.all().aggregate(Max('document_id'))
g_doc_id = temp['document_id__max'] if temp['document_id__max'] else 0

def search(request):
    context = {}
    return render(request, 'search.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)

def success(request):
    if(request.method == 'POST'):
        all_terms = Index.objects.all()
        print(all_terms)
        global g_doc_id
        print("Global doc id = ",g_doc_id)
        document = request.POST['document']
        print(document)
        document = document.split('\r\n\r\n')
        print(document)
        for i in document:
            appearances_dict = dict()
            i = i.split('\r\n')
            print("\n")
            print(i)
            for j in i:
                clean_text = re.sub(r'[^\w\s]','', j)
                clean_text = clean_text.lower()
                terms = clean_text.split(' ')
                print("terms")
                print(terms)
                
                for term in terms:
                    if term in appearances_dict:
                        term_frequency = appearances_dict[term]
                    else:  term_frequency = 0
                    appearances_dict[term] = term_frequency+1
                print('app')
                print(appearances_dict)
            for term,fre in appearances_dict.items():
                a = Index(document_id = g_doc_id,key = term, frequency = fre)
                a.save()
            g_doc_id +=1
            print("Global doc id = ",g_doc_id)
            
        print(document)
        context = {}
        return render(request, 'success.html',context)
    else :
        return HttpResponse('Invalid path<br> <a href="/">Click here to go back to main page</a>')

def query(request):
    if(request.method == 'POST'):
        # all_terms = Index.objects.all()
        # print(all_terms)
        query = request.POST['query']
        print(query)
        query = query.split()
        result = []
        for i in query:
            print(i)
            temp_result = Index.objects.filter(key = i).order_by('-frequency')[:10]
            if temp_result:
                result.append(temp_result)
        flag = False
        if result:
            flag = True
        context = {
            'result':result,
            'flag': flag,
            'query': query
        }
        return render(request, 'result.html',context)
    else :
        return HttpResponse('Invalid path<br> <a href="/">Click here to go back to main page</a>')


def clear(request):
    Index.objects.all().delete()
    global g_doc_id
    g_doc_id = 0
    print("Global doc id = ",g_doc_id)
    return render(request, 'clear.html')


def home(request):
    a = Index.objects.filter(key = "lorem")
    global g_doc_id
    print(g_doc_id)
    return render(request, 'home.html')

class HomeAPIView(generics.ListAPIView):
    queryset = Index.objects.all()
    serializer_class = HomeSerializer
