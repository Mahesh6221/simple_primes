from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'input_page.html',{})


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def output_page(request):
    if request.method == 'POST':
        n = int(request.POST.get('number', 0))
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        
        return render(request, 'output_page.html', {'primes': primes, 'number': n})
    return render(request, 'input_page.html')