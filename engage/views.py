from django.shortcuts import render
import qrcode
from PIL import Image
from io import BytesIO
import base64
# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request,'index.html')
    else:
        text = request.POST['text']
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        buffer.seek(0)
        qr_code_base64 = base64.b64encode(buffer.read()).decode()

        return render(request, 'qr.html', {'qr_code_base64': qr_code_base64})