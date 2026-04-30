from django.shortcuts import render
from .forms import QRcodeForm
import qrcode 
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method =='POST':
        form = QRcodeForm(request.POST)
        if form.is_valid():
            resturant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            #generate QR code
            qr = qrcode.make(url)
            file_name=resturant_name.replace(" ","_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)

            #image url
            qr_url  =os.path.join(settings.MEDIA_URL,file_name)
            context ={
                resturant_name: resturant_name,
                'qr_url': qr_url
                
            }
            return render(request , 'qr_code_result.html',context)
            
    else:
        form = QRcodeForm()
        context ={
            'form': form
        }

    return render(request,'generate_qr_code.html',context)

