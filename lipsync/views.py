from django.shortcuts import render, redirect
from .forms import LipSyncForm
from django.http import HttpResponse
from .model import hf_model
from django.shortcuts import render
from django.conf import settings
import os
from .models import LipSyncTask
from .forms import LipSyncForm  

from django.shortcuts import render, redirect
from .models import LipSyncTask

def create_task(request):
    return render(request, 'create.html')



def home(request):
    template_path = os.path.join(settings.BASE_DIR, 'lipsync_app', 'templates', 'home.html')
    return render(request, template_path)



def upload_files(request):
    if request.method == 'POST':
        form = LipSyncForm(request.POST, request.FILES)
        if form.is_valid():
            lip_sync_task = form.save(commit=False)
            lip_sync_task.user = request.user
            lip_sync_task.save()
            process_lip_sync(lip_sync_task)
            return redirect('result', task_id=lip_sync_task.id)
    else:
        form = LipSyncForm()
    return render(request, 'upload.html', {'form': form})



def process_lip_sync(lip_sync_task):
    input_text = lip_sync_task.input_text
    generated_text = hf_model.generate_text(input_text)
    lip_sync_task.generated_text = generated_text
    lip_sync_task.status = 'processed'
    lip_sync_task.save()


def generate_text_view(request):
    input_text = request.GET.get('input', '')
    if input_text:
        generated_text = hf_model.generate_text(input_text)
        return HttpResponse({'generated_text': generated_text})
    return HttpResponse({'error': 'No input text provided'}, status=400)



def login_view(request):
    # Render the custom login template
    return render(request, 'login.html')


def signup_view(request):
    # Render the custom signup template
    return render(request, 'signup.html')