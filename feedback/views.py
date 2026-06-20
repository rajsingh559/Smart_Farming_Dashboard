from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackRatingForm
from .models import Feedback, Rating

@login_required
def feedback_list_view(request):
    """View to submit feedback & ratings, and view submission log based on user role."""
    if request.method == 'POST':
        form = FeedbackRatingForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['feedback_text']
            score = form.cleaned_data['score']
            
            # Save feedback record
            Feedback.objects.create(user=request.user, feedback_text=text)
            
            # Save rating record
            Rating.objects.create(user=request.user, score=int(score))
            
            messages.success(request, "Thank you for your valuable feedback!")
            return redirect('feedback_list')
    else:
        form = FeedbackRatingForm()
        
    # Check roles to filter data views
    if request.user.is_staff:
        # Admins see everything
        feedbacks = Feedback.objects.all().order_by('-created_at')
        ratings = Rating.objects.all().order_by('-created_at')
        
        # Calculate stats
        total_count = ratings.count()
        avg_score = sum(r.score for r in ratings) / total_count if total_count > 0 else 0
    else:
        # Farmers see only their own
        feedbacks = Feedback.objects.filter(user=request.user).order_by('-created_at')
        ratings = Rating.objects.filter(user=request.user).order_by('-created_at')
        total_count = ratings.count()
        avg_score = sum(r.score for r in ratings) / total_count if total_count > 0 else 0

    # Combine items for easier display
    context = {
        'form': form,
        'feedbacks': feedbacks,
        'ratings': ratings,
        'avg_score': round(avg_score, 1),
        'total_count': total_count,
    }
    return render(request, 'feedback/feedback.html', context)
