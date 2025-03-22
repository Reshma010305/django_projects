from django.shortcuts import render
def carousel_view(request):
    print("DEBUG: View is being accessed!") 
    return render(request,'carousel.html')