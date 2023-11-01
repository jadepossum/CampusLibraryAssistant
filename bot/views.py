from rest_framework.views import APIView
from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from bot.models import Subject ,Book ,PQP
from datetime import date,timedelta
import json

def searchbook(request):
    if request.method == "POST":
        title = request.POST.get("Title").upper().strip()
        for book in Book.objects.all():
            if book.Title == title:
                return HttpResponse({"found"})
            
        return HttpResponse({"not found"})
    return render(request,'search.html')

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
            for book in Book.objects.all():
                if book.Title == title:
                    resp = book.Title
                    if book.Author!='-':
                        resp+=" by "+book.Author
                    if book.Location:
                        bloc = book.Location.split(" ")
                        resp+=" is available at "+bloc[0]+" rack side "+bloc[1]+" in the main stacks area."
                    else :
                        resp+=" is available at the library"
                    textResponse.append({"text": {"text": [resp]}})
            if textResponse:
                return Response({"fulfillmentMessages": textResponse})
            return Response({"fulfillmentMessages": textResponse})




        if request.data["queryResult"]["intent"]["displayName"] == "getListSubjects":
            textResponse = []

            for subject in Subject.objects.all():
                textResponse.append({"text": {"text": [subject.name]}})

            return Response({"fulfillmentMessages": textResponse})


        if request.data["queryResult"]["intent"]["displayName"] == "getPQP":
            responseText = []
            subject = request.data["queryResult"]["parameters"]["subject"]
            for paper in PQP.objects.all():
                if paper.Subject == subject:
                    responseText.append({"text": {"text": [paper.link]}})
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
                                        "link":paper.link
                                    },
                                    ]
                                }
                            ]
                        ]
                        }
                    })

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