from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote

def main(request):
    #get
    quotes = Quote.objects.all()
#    quoto_filter = Quote.objects.filter(is_active=True)
#    quoto = Quote.objects.get(id=1)

    context = {
        'quotes':quotes,
        #'quoto_filter':quoto_filter,
        #'quoto':quoto
    }
   #update
    quote = Quote.objects.get(id=1)
    quote.is_active = False
    quote.first_name= 'shohjahon'
    quote.save()
   #crete
    for i in range(5):
        Quote.objects.create(
        first_name = str(i+1),
        last_name = 'shoh',
        phone = '+998999999999',
        message = 'sadsafa'
    )
   
   #delete
    Quote.objects.get(id=6).delete()

    return HttpResponse('salom')
