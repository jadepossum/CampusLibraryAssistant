from rest_framework.views import APIView
from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from bot.models import Subject ,Book ,PQP ,PPT
from datetime import date,timedelta
import json

def entrance(request):
    return render(request,'index.html')

def searchbook(request):
    qs = Book.objects
    depts = qs.values('Dept').distinct()
    if request.method == "POST":
        dpt = request.POST.get("Dept")
        print(dpt)
        if dpt:
            qs = qs.filter(Dept=dpt)
        title = request.POST.get("Title")
        if title:
            title = title.upper().strip()
            Words = title.split()
            wlen = len(Words)
            for i in Words:
                if i!='':
                    qs = qs.filter(Title__icontains=i)
        author = request.POST.get("Author")
        if author:
            author = author.upper().strip()
            Words = author.split()
            print("Author",Words)
            wlen = len(Words)
            for i in Words:
                if i!='':
                    qs = qs.filter(Author__icontains=i)
    qs = qs.all()    
    return render(request,'search.html',{'availableBooks':qs.all(),'Depts':depts})


def deleteAllBooks(request):
    Book.objects.all().delete()
    return HttpResponse({"All Books are removed from the database."})

def TitleStrip(request):
    for book in Book.objects.all():
        book.Title = book.Title.strip()
        book.save(force_update=True)
    return HttpResponse({"leading and trailing whitespaces are removed"})

def chatInterface(request):
    return render(request,'chatbot.html')

def LibDetails(request):
    return render(request,'lib_details.html')

class WebHook(APIView):
    def post(self, request):

        print(json.dumps(request.data, indent=2))

        if request.data["queryResult"]["intent"]["displayName"] == "CalcDueTime":
            curdate = date.today()
            issuedate = date.fromisoformat(request.data["queryResult"]["parameters"]["issueDate"].split('T')[0])
            while issuedate>curdate:
                issuedate-=timedelta(days=365)
            tdelta = timedelta(days=15)
            returndate = issuedate + tdelta
            responseText = []
            if(issuedate>curdate):
                return Response({"fulfillmentMessages": [{"text": {"text": ["Plese enter the date with valid year"]}}]})
            if(curdate > returndate):
                return Response({"fulfillmentMessages": [{"text": {"text": ["fined ",(curdate - returndate).days," rupees as of today"]}}]})
            else:
                return Response({"fulfillmentMessages": [{"text": {"text": ["return the book on or before "+returndate.strftime("%d-%m-%Y")]}}]})



        if request.data["queryResult"]["intent"]["displayName"] == "checkAvailability":
            textResponse = []
            title = request.data["queryResult"]["parameters"]["title"][0].split('\"')[1].upper().strip()
            Words = title.split()
            wlen = len(Words)
            Filter = False
            availCount = 0
            for book in Book.objects.all():
                BookTitle = book.Title
                #testing
                Filter = False
                count = 0
                for i in Words:
                    if i in BookTitle:
                        count+=1
                if count==wlen:
                    Filter = True
                if Filter:
                # if book.Title == title:
                    availCount+=1
                    resp = book.Title
                    if book.Author!='-':
                        resp+=" by "+book.Author
                    if book.Location:
                        bloc = book.Location.split(" ")
                        resp+=" is at "+bloc[0]+" rack side "+bloc[1]+" in the main stacks area."
                    textResponse.append({"text": {"text": [resp]}})
                    if availCount==10:
                        break
            if textResponse:
                if len(textResponse)==1:
                    textResponse[0]["text"]["text"].append(" is available at the library.")
                else:
                    textResponse.append({"text": {"text": ["These are "+str(availCount)+" Titles available at the library."]}})
                textResponse.append({"text": {"text": ["See all available Titles at:\nhttps://saikrishnakota.pythonanywhere.com/search"]}})
                return Response({"fulfillmentMessages": textResponse})
            textResponse.append({"text": {"text": [request.data["queryResult"]["parameters"]["title"][0] + " is currently unavailable."]}})
            textResponse.append({"text": {"text": ["See all available Titles at:\nhttps://saikrishnakota.pythonanywhere.com/search"]}})
            return Response({"fulfillmentMessages": textResponse})



        if request.data["queryResult"]["intent"]["displayName"] == "checkAvailabilitybyAuthor":
            print("checkAvailability::byAuthor")
            textResponse = []
            Author = request.data["queryResult"]["parameters"]["person"]["name"].upper().strip()
            Words = Author.split()
            wlen = len(Words)
            Filter = False
            availCount = 0
            for book in Book.objects.all():
                BookAuthor = book.Author
                #testing
                Filter = False
                count = 0
                for i in Words:
                    if i in BookAuthor:
                        print(i,BookAuthor)
                        count+=1
                if count==wlen:
                    Filter = True
                if Filter:
                # if book.Title == title:
                    availCount+=1
                    resp = book.Title+" by "+book.Author
                    if book.Location:
                        bloc = book.Location.split(" ")
                        resp+=" is available at "+bloc[0]+" rack side "+bloc[1]+" in the main stacks area."
                    textResponse.append({"text": {"text": [resp]}})
                    if availCount==10:
                        break
            if textResponse:
                if len(textResponse)==1:
                    textResponse[0]["text"]["text"].append(" is available at the library.")
                else:
                    textResponse.append({"text": {"text": ["These are "+str(availCount)+" Titles available at the library."]}})
                textResponse.append({"text": {"text": ["See all available Titles at:\nhttps://saikrishnakota.pythonanywhere.com/search"]}})
                return Response({"fulfillmentMessages": textResponse})
            textResponse.append({"text": {"text": ["Books by"+request.data["queryResult"]["parameters"]["person"]["name"] + " are currently unavailable."]}})
            textResponse.append({"text": {"text": ["See all available Titles at:\nhttps://saikrishnakota.pythonanywhere.com/search"]}})
            return Response({"fulfillmentMessages": textResponse})




        # if request.data["queryResult"]["intent"]["displayName"] == "getListSubjects":
        #     textResponse = []

        #     for subject in Subject.objects.all():
        #         textResponse.append({"text": {"text": [subject.name]}})

        #     return Response({"fulfillmentMessages": textResponse})


        if request.data["queryResult"]["intent"]["displayName"] == "getPQP":
            responseText = []
            subject = request.data["queryResult"]["parameters"]["subject"]
            for paper in PQP.objects.all():
                if paper.Subject == subject:
                    responseText.append({"text": {"text": [paper.Link]}})
                    responseText.append({"payload":{
                        "richContent":[
                            [
                                {
                                    "type":"chips",
                                    "options":[
                                    {
                                        "text":paper.Year,
                                        "image":{
                                            "src":{
                                                    "rawUrl":"data:image/png;base64,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"
                                                }
                                        },
                                        "link":paper.Link
                                    },
                                    ]
                                }
                            ]
                        ]
                        }
                    })
            if responseText == []:
                textResponse.append({"text": {"text": ["resource currently unavailable"]}})
            return Response({"fulfillmentMessages": responseText})
        
        if request.data["queryResult"]["intent"]["displayName"] == "getPrepMaterial":
            responseText = []
            subject = request.data["queryResult"]["parameters"]["subject"]
            for paper in PPT.objects.all():
                if paper.Subject == subject:
                    responseText.append({"text": {"text": [paper.Link]}})
                    responseText.append({"payload":{
                        "richContent":[
                            [
                                {
                                    "type":"chips",
                                    "options":[
                                    {
                                        "text":paper.Year,
                                        "image":{
                                            "src":{
                                                    "rawUrl":"data:image/png;base64,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"
                                            }
                                        },
                                        "link":paper.Link
                                    },
                                    ]
                                }
                            ]
                        ]
                        }
                    })
            if responseText == []:
                    textResponse.append({"text": {"text": ["resource currently unavailable"]}})
            return Response({"fulfillmentMessages": responseText})

        subjectCodes = request.data["queryResult"]["parameters"]["subject"]

        responseText = []

        for code in subjectCodes:
            try:
                subject = Subject.objects.get(name=code)
                if subject.documents:
                    for document in subject.documents.all():
                        responseText.append({"text": {"text": [document.url]}})
                        responseText.append({"payload":{
                            "richContent":[
                                [
                                    {
                                        "type":"chips",
                                        "options":[
                                        {
                                            "text":"click to open",
                                            "image":{
                                                "src":{
                                                    "rawUrl":"data:image/png;base64,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"
                                                }
                                            },
                                            "link":document.url
                                        },
                                        ]
                                    }
                                ]
                            ]
                            }
                        })
                else:
                    responseText.append({"text": {"text": ["not available on the other side"]}})
            except Exception as e:
                responseText.append({"text": {"text": [str(e)]}})

        return Response({"fulfillmentMessages": responseText})