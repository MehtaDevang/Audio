from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Song, AudioBook, Podcast
import json
# Create your views here.

audio_types = ['Song', 'Podcast', 'Audiobook']


@csrf_exempt
@api_view(['POST'])
def create_audio(request):
    if request.method == 'POST':
        audioFileType = request.POST.get('audioFileType')
        audioFileMetadata = request.POST.get('audioFileMetadata')

        dict = {

        }


        print(audioFileType)
        print(type(audioFileMetadata))
        if audioFileType is None or audioFileMetadata is None:
            return JsonResponse({"errorMessage" : "The request is invalid: 400 bad request "})
        if audioFileType not in audio_types:
            return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
        audioFileMetadata = json.loads(audioFileMetadata)
        print(audioFileMetadata)
        if audioFileType == 'Song':
            try:
                model = Song()
                model.name = audioFileMetadata['name']
                model.duration = audioFileMetadata['duration']
                model.save()
            except:
                return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})

        elif audioFileType == 'Podcast':
            try:
                model = Podcast()
                model.name = audioFileMetadata['name']
                model.duration = audioFileMetadata['duration']
                model.host = audioFileMetadata['host']
                if 'participants' in audioFileMetadata:
                    model.participants = audioFileMetadata['participants']
                model.save()
            except:
                return JsonResponse({"errorMessage" : "The request is invalid: 400 bad request"})

        else:
            try:
                model = AudioBook()
                model.title = audioFileMetadata['title']
                model.author = audioFileMetadata['author']
                model.narrator = audioFileMetadata['narrator']
                model.duration = audioFileMetadata['duration']
                model.save()
            except:
                return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})

        return JsonResponse({"message": "Action is successful : 200 OK"})


@csrf_exempt
@api_view(['POST'])
def delete_audio(request, audioFileType, audioFileID):
    if request.method == 'POST':
        print("hello")
        if audioFileType is None or audioFileID is None:
            return JsonResponse({"errorMessage" : "The request is invalid: 400 bad request"})
        if audioFileType not in audio_types:
            return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
        if audioFileType == 'Song':
            try:
                object = Song.objects.get(id=audioFileID)
                object.delete()
            except:
                return JsonResponse({"errorMessage" : "Any error: 500 internal server error"})

        elif audioFileType == 'Podcast':
            try:
                object = Podcast.objects.get(id=audioFileID)
                object.delete()
            except:
                return JsonResponse({"errorMessage" : "Any error: 500 internal server error"})

        else:
            try:
                object = AudioBook.objects.get(id=audioFileID)
                object.delete()
            except:
                return JsonResponse({"errorMessage": "Any error: 500 internal server error"})

        return JsonResponse({"message" : "Action is successful: 200 OK"})


@csrf_exempt
@api_view(['POST'])
def update_audio(request, audioFileType, audioFileID):
    global audio_types

    if request.method == 'POST':
        audioFileMetadata = request.POST.get('audioFileMetadata')
        print(audioFileMetadata)
        if audioFileType is None or audioFileID is None or audioFileMetadata is None:
            return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
        if audioFileType not in audio_types:
            return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
        audioFileMetadata = json.loads(audioFileMetadata)
        print(audioFileMetadata)
        if audioFileType == 'Song':
            try:
                object = Song.objects.get(id=audioFileID)
            except:
                return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
            try:
                if "name" in audioFileMetadata:
                    object.name = audioFileMetadata['name']
                if "duration" in audioFileMetadata:
                    object.duration = audioFileMetadata['duration']
                object.save()
            except:
                return JsonResponse({"errorMessage": "Any error: 500 internal server error"})

        elif audioFileType == 'Podcast':
            try:
                object = Podcast.objects.get(id=audioFileID)
            except:
                return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
            try:
                if "name" in audioFileMetadata:
                    object.name = audioFileMetadata['name']
                if "duration" in audioFileMetadata:
                    object.duration = audioFileMetadata['duration']
                if "host" in audioFileMetadata:
                    object.host = audioFileMetadata['host']
                if "participants" in audioFileMetadata:
                    object.participants = audioFileMetadata['participants']
                object.save()
            except:
                return JsonResponse({"errorMessage": "Any error: 500 internal server error"})

        elif audioFileType == 'Audiobook':
            try:
                object = AudioBook.objects.get(id=audioFileID)
            except:
                return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
            try:
                if "title" in audioFileMetadata:
                    object.title = audioFileMetadata['title']
                if "duration" in audioFileMetadata:
                    object.duration = audioFileMetadata['duration']
                if "author" in audioFileMetadata:
                    object.author = audioFileMetadata['author']
                if "narrator" in audioFileMetadata:
                    object.narrator = audioFileMetadata['narrator']
                object.save()
            except:
                return JsonResponse({"errorMessage": "Any error: 500 internal server error"})


        return JsonResponse({"message" : "Action is successful: 200 OK"})


@csrf_exempt
@api_view(['GET'])
def get_audio(request, audioFileType, audioFileID = None):
    if request.method == "GET":
        songs = []
        if audioFileType is None:
            return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})
        if audioFileType == "Song":
            if audioFileID is None:
                try:
                    songs = Song.objects.all().values()
                    print(songs)
                except:
                    return JsonResponse({"errorMessage": "Any error: 500 internal server error"})
            else:
                try:
                    songs = Song.objects.filter(id=audioFileID).values()
                except:
                    return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})

        if audioFileType == "Podcast":
            if audioFileID is None:
                try:
                    songs = Podcast.objects.all().values
                except:
                    return JsonResponse({"errorMessage": "Any error: 500 internal server error"})
            else:
                try:
                    songs = Podcast.objects.filter(id=audioFileID).values()
                except:
                    return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})

        if audioFileType == "Audiobook":
            if audioFileID is None:
                try:
                    songs = AudioBook.objects.all().values()
                except:
                    return JsonResponse({"errorMessage": "Any error: 500 internal server error"})
            else:
                try:
                    songs = AudioBook.objects.filter(id=audioFileID).values()
                except:
                    return JsonResponse({"errorMessage": "The request is invalid: 400 bad request"})

        all_songs = {}
        temp = []
        for obj in songs:
            temp.append(obj)
        all_songs['songs'] = songs

        return JsonResponse({"songs" : temp})