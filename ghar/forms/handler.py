# from .prop_img_upload import ImageUploadForm
# from django.shortcuts import redirect
# from makaan.ghar.models import PropertyImage
#
#
# def upload_images(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             images = request.FILES.getlist('images')  # Retrieve the list of uploaded files
#
#             for i in range(1, len(images) + 1):
#                 image = {'image' + str(i): images(i)}
#                 PropertyImage.objects.create(title=title, **image)
#
#             return redirect('prop_img_upload')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload.html', {'form': form})
#
