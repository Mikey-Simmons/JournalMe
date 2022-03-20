from django.shortcuts import render, redirect
from .models import User, JournalEntry
import bcrypt, re
from django.contrib import messages

def index(request):
    return render(request,'index.html')
