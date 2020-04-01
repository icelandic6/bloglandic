from django.shortcuts import render


def post_list(request):
    print('\nREQUEST:\n', request, '\n')
    print('\nREQUEST DIR:\n', dir(request), '\n')

    nm = ['Alex', 'Xena', 'Niko']
    return render(request, 'blog/index.html', context={'names': nm})
