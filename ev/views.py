from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import qrcode
from .models import Exam, QRCode
import io

def generate_qr_code(request):
    exams = Exam.objects.all()
    if request.method == 'POST':
        exam_regis = request.POST['stu-regis']
        exam_name = request.POST['stu-full-name']

        exam = Exam.objects.create(exam_regis=exam_regis, exam_name=exam_name)
        exam.save()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f'http://127.0.0.1:8000/validate/{exam_regis}')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        image_io = io.BytesIO()
        img.save(image_io, format='PNG')
        qr_code = QRCode.objects.create(exam=exam)
        qr_code.code_image.save(f'{exam_regis}_qr.png', image_io)
    return render(request, 'generate_qr_code.html', {'exams': exams})


from django.shortcuts import render
from PIL import Image
from pyzbar.pyzbar import decode
from .models import Exam

def validate_exam(request, exam_regis):
    exam = Exam.objects.get(exam_regis=exam_regis)
    qr_code_path = exam.qrcode.code_image.path

    decoded_objects = decode(Image.open(qr_code_path))
    if decoded_objects:
        decoded_data = decoded_objects[0].data.decode('utf-8')
        if decoded_data == f'http://127.0.0.1:8000/validate/{exam_regis}':
            return render(request, 'validate_exam.html', {'exam': exam})
        else:
            error_message = "Invalid QR Code"
    else:
        error_message = "No QR Code detected in the image"

    return render(request, 'validation_error.html', {'error_message': error_message})


