from django.shortcuts import render
from django.http import HttpResponse
import os

def find_winner(bidder_details):
    high_bidder = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > high_bidder:
            high_bidder = bidding_price
            winner = bidder
    return winner, high_bidder

def submit_bid(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = int(request.POST.get('price'))
        more_bidders = request.POST.get('more_bidders')

        # Store the bid information (temporary storage for simplicity)
        if not hasattr(request.session, 'bid_price'):
            request.session['bid_price'] = {}

        bid_price = request.session['bid_price']
        bid_price[name] = price
        request.session['bid_price'] = bid_price

        # Check if there are more bidders
        if more_bidders == 'no':
            winner, highest_bid = find_winner(bid_price)
            return render(request, 'bid_success.html', {'winner': winner, 'highest_bid': highest_bid})

        return render(request, 'submit_bid.html')  # Reload page to accept another bidder

    return render(request, 'submit_bid.html')  # Initial form for submitting bids
