from django.shortcuts import render, redirect
from .models import Fungi, FungiImage

def fungi_list(request):
    fungi = Fungi.objects.all()
    return render(request, 'fungi/fungi_list.html', {'fungi': fungi})

def fungi_detail(request, fungi_id):
    fungus = Fungi.objects.get(pk=fungi_id)
    return render(request, 'fungi/fungi_detail.html', {'fungus': fungus})

def quiz(request):
    feedback = None
    correct = False
    image = None

    if 'next' in request.POST:  # If the "Next" button was clicked
        image = FungiImage.objects.order_by('?').first()
    elif request.method == "POST":
        user_guess = request.POST.get('guess')
        correct_answer = request.POST.get('correct_answer')
        image_id = request.POST.get('image_id')
        image = FungiImage.objects.get(id=image_id)  # Get the current image based on its ID

        if user_guess.lower() == correct_answer.lower():
            feedback = "Correct!"
            correct = True
        else:
            feedback = f"Wrong! The correct answer was {correct_answer}."
    else:
        image = FungiImage.objects.order_by('?').first()

    return render(request, 'fungi/quiz.html', {
        'image': image, 
        'feedback': feedback,
        'correct': correct
    })

