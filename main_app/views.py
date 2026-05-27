from .models import QuizScore

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import landscape, A4

from reportlab.lib.colors import darkblue, black, gold

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


def home(request):

    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/login/')

        else:

            print(form.errors)

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )


@login_required
def dashboard(request):

    return render(request, 'dashboard.html')


def courses(request):

    return render(request, 'courses.html')


def python_course(request):

    return render(request, 'python_course.html')


def django_course(request):

    return render(request, 'django_course.html')


@login_required
def ai_course(request):

    # SAVE QUIZ SCORE
    if request.method == "POST":

        score = int(request.POST.get("score", 0))

        QuizScore.objects.create(

            user=request.user,

            course_name="Artificial Intelligence",

            score=score

        )

    return render(
        request,
        'ai_course.html'
    )


def certificates(request):

    return render(request, 'certificates.html')


@login_required
def certificate(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = (
        'attachment; filename="SkillForge_Certificate.pdf"'
    )

    p = canvas.Canvas(response, pagesize=landscape(A4))

    width, height = landscape(A4)

    # GET COURSE NAME DYNAMICALLY
    course_name = request.GET.get(
        'course',
        'Python Programming Course'
    )

    # OUTER BORDER
    p.setStrokeColor(darkblue)
    p.setLineWidth(8)

    p.rect(
        30,
        30,
        width - 60,
        height - 60
    )

    # INNER BORDER
    p.setLineWidth(2)

    p.rect(
        50,
        50,
        width - 100,
        height - 100
    )

    # TITLE
    p.setFont("Helvetica-Bold", 32)
    p.setFillColor(darkblue)

    p.drawCentredString(
        width / 2,
        height - 120,
        "CERTIFICATE OF COMPLETION"
    )

    # SUBTITLE
    p.setFont("Helvetica", 18)
    p.setFillColor(black)

    p.drawCentredString(
        width / 2,
        height - 180,
        "This certificate is proudly presented to"
    )

    # USERNAME
    p.setFont("Helvetica-Bold", 30)
    p.setFillColor(gold)

    p.drawCentredString(
        width / 2,
        height - 260,
        request.user.username.upper()
    )

    # COURSE TEXT
    p.setFont("Helvetica", 20)
    p.setFillColor(black)

    p.drawCentredString(
        width / 2,
        height - 330,
        "For successfully completing the"
    )

    # DYNAMIC COURSE NAME
    p.setFont("Helvetica-Bold", 24)

    p.drawCentredString(
        width / 2,
        height - 380,
        course_name
    )

    # FOOTER
    p.setFont("Helvetica-Oblique", 16)

    p.drawCentredString(
        width / 2,
        100,
        "SkillForge • AI Powered Learning Platform"
    )

    # SIGNATURE LINE
    p.line(
        width - 250,
        150,
        width - 100,
        150
    )

    p.setFont("Helvetica", 14)

    p.drawString(
        width - 220,
        130,
        "Authorized Signature"
    )

    p.save()

    return response


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

    return render(
        request,
        'registration/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('/')


@login_required
def chatbot(request):

    reply = ""

    if request.method == "POST":

        user_message = request.POST.get("message")

        # SIMPLE AI RESPONSES
        if "python" in user_message.lower():

            reply = (
                "Python is a powerful programming language "
                "used in AI, Web Development and Data Science."
            )

        elif "django" in user_message.lower():

            reply = (
                "Django is a Python framework used to build "
                "modern web applications."
            )

        elif "ai" in user_message.lower():

            reply = (
                "Artificial Intelligence enables machines "
                "to think and learn like humans."
            )

        elif "hello" in user_message.lower():

            reply = (
                "Hello 👋 Welcome to SkillForge AI Chatbot!"
            )

        else:

            reply = (
                "Sorry, I am still learning 🤖"
            )

    return render(
        request,
        'chatbot.html',
        {
            'reply': reply
        }
    )


@login_required
def leaderboard(request):

    scores = QuizScore.objects.order_by('-score')[:10]

    return render(
        request,
        'leaderboard.html',
        {
            'scores': scores
        }
    )