from django.shortcuts import render

# Create your views here.
def scanqr(request):
    """
    This view handles the QR code scanning functionality.
    It renders the 'scanqr.html' template.
    """
    return render(request, 'scanqr.html')