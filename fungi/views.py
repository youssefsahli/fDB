from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Fungi, FungiImage, Genre

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

    if 'dont_know' in request.POST:
        correct_answer = request.POST.get('correct_answer')
        feedback = f"The correct answer was {correct_answer}."
        image_id = request.POST.get('current_image_id')
        image = FungiImage.objects.get(id=image_id)

    elif 'next' in request.POST:  # If the "Next" button was clicked
        image = FungiImage.objects.order_by('?').first()
    elif request.method == "POST":
        selected_species_id = request.POST.get('selected_species')

        # Check if selected_species_id is provided and not empty
        if not selected_species_id:
            feedback = "Please select a species."
            # image = FungiImage.objects.order_by('?').first()  # Fetch a new random image
        else:
            try:
                selected_species = Fungi.objects.get(id=selected_species_id)
                correct_answer = request.POST.get('correct_answer')
                image_id = request.POST.get('image_id')
                image = FungiImage.objects.get(id=image_id)  # Get the current image based on its ID

                if selected_species.latin_name.lower() == correct_answer.lower():
                    feedback = "Correct!"
                    correct = True
                else:
                    feedback = f"Wrong! The correct answer was {correct_answer}."

            except Fungi.DoesNotExist:
                feedback = "Selected species does not exist. Please try again."

    else:
        image = FungiImage.objects.order_by('?').first()

    genres = Genre.objects.all().order_by('name')
    return render(request, 'fungi/quiz.html', {
        'image': image, 
        'feedback': feedback,
        'correct': correct,
        'genres': genres,
    })


def get_species(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    species = Fungi.objects.filter(genre=genre)
    species_data = [{"name": specie.latin_name, "id": specie.id} for specie in species]
    return JsonResponse({"species": species_data})

