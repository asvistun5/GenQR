from django.shortcuts import render
from django.http import HttpResponseRedirect
import qrcode
from .models import QR
from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
from io import BytesIO
import requests

# Create your views here.
def render_gen_qr(request):
    if request.method == "POST":
        url = request.POST.get("url")
        color = request.POST.get("color")
        bg_color = request.POST.get("bgcolor")
        shape = request.POST.get("shape")
        img = request.POST.get("img")

        if url:
            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            qr_img = qr.make_image(fill=color, back_color="white").convert("RGB")
            qr_size = qr_img.size[0]
    
            styled_qr = Image.new("RGB", (qr_size, qr_size), "white")
            draw = ImageDraw.Draw(styled_qr)

            block_size = qr_size // (qr.modules_count + 2)

            for row in range(qr.modules_count):
                for col in range(qr.modules_count):
                    if qr.modules[row][col]: 
                        x0 = (col + 1) * block_size
                        y0 = (row + 1) * block_size
                        x1 = x0 + block_size
                        y1 = y0 + block_size
                        draw.rounded_rectangle((x0, y0, x1, y1), radius=block_size // 2, fill=color)

            if img:
                try:
                    response = requests.get(img)
                    logo = Image.open(BytesIO(response.content)).convert("RGBA")
                    logo_size = qr_size // 4 
                    logo = logo.resize((logo_size, logo_size))

                    pos = ((qr_size - logo_size) // 2, (qr_size - logo_size) // 2)
                    styled_qr.paste(logo, pos, logo)
                except requests.exceptions.RequestException as e:
                    print(e)

            qr_image_io = BytesIO()
            styled_qr.save(qr_image_io, format="PNG")
            qr_image_io.seek(0)

            qr_code = QR.objects.create(url=url, color=color, shape=shape)
            qr_code.img.save(f"qr_{qr_code.id}.png", ContentFile(qr_image_io.read()))

            return HttpResponseRedirect("home/") 

    return render(request, 'gen.html')