from django.shortcuts import render, redirect
from gen_qr.models import QR 

def render_my_qr(request):
    qrcodes = QR.objects.all()
    if request.method == "POST":
        for key in request.POST:
            if key.startswith("del-"):
                qr_id = key.split("-")[1]
                QR.objects.filter(pk=qr_id).delete()
                return redirect('my_qr')   
    
    return render(request, 'qr.html', context={'qrs': qrcodes})