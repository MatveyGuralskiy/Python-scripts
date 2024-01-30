from django.shortcuts import render

def index(request):
    context = {
        'favorite_language': 'Bash',
        'image_path': 'FirstWeb3/image.png',
        'background_image_path': 'FirstWeb3/backimage.jpg',
    }
    return render(request, 'FirstWeb3/index.html', context)