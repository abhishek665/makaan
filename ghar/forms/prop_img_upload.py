# from django import forms
#
# from ..models import PropertyImage
#
# class MyModelForm(forms.ModelForm):
#     image1 = forms.FileField(multiple=True)
#     image2 = forms.FileField(multiple=True)
#     image3 = forms.FileField(multiple=True)
#     image4 = forms.FileField(multiple=True)
#     image5 = forms.FileField(multiple=True)
#     image6 = forms.FileField(multiple=True)
#     image7 = forms.FileField(multiple=True)
#     image8 = forms.FileField(multiple=True)
#     image9 = forms.FileField(multiple=True)
#     image10 = forms.FileField(multiple=True)
#     image11 = forms.FileField(multiple=True)
#     image12 = forms.FileField(multiple=True)
#     image13 = forms.FileField(multiple=True)
#     image14 = forms.FileField(multiple=True)
#     image15 = forms.FileField(multiple=True)
#     image16 = forms.FileField(multiple=True)
#     image17 = forms.FileField(multiple=True)
#     image18 = forms.FileField(multiple=True)
#     image19 = forms.FileField(multiple=True)
#     image20 = forms.FileField(multiple=True)
#
#     class Meta:
#         model = PropertyImage
#         fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10'
#                   , 'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17', 'image18', 'image19', 'image20']
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#
#         # Iterate over the uploaded files and assign them to the corresponding image fields.
#         for i in range(1, 11):
#             image = getattr(self, f'image{i}')
#             for file in image.files:
#                 instance[f'image{i}'] = file
#
#         if commit:
#             instance.save()
#
#         return instance