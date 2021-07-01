from django.shortcuts import render, redirect, get_object_or_404
from .models import Donate, Taker, Volunteer, Feedback
from .forms import TakerForm, DonateForm, VolunteerForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import View, ListView
from account.forms import UserForm
from django.contrib.auth.models import User

def index_view(request):
    return render(request, 'core/index.html')

class GiverView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        taker = Taker.objects.filter(approve=True)
        return render(self.request, 'core/giver.html', {'taker':taker})

class GiverDetailView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        taker = Taker.objects.get(pk=self.kwargs['pk'])
        return render(self.request, 'core/giver_detail.html', {'taker':taker})

class HistoryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/history.html')

class AboutUsView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/about_us.html')

class TakerView(LoginRequiredMixin, View):
    def post(self,request):

        t_form = TakerForm(request.POST, request.FILES)
        if t_form.is_valid():
            dilip = t_form.save(commit=False)
            dilip.user=request.user
            dilip.save()
            messages.success(request, "updated successfully")
            return redirect(".")
        else:
            messages.info(request, "Form is not valid")
            return redirect(".")
    def get(self,request):
        t_form = TakerForm()
        context = {
            't_form':t_form,
        }
        return render(self.request, 'core/taker.html', context)

class FAQView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/faq.html')

class MissionView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/mission.html')

class VisionView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/vision.html')

class PhoneView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/phone.html')

class FeedBackView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'core/feedback.html')

#################################################################
class TakerListView(ListView):
    model = Taker
    template_name = "core/admin_taker_list.html"

@login_required
def approval_view(request, pk):
    taker = Taker.objects.get(id=pk)
    taker.approve = True
    taker.save()
    return redirect("/core/admin-taker/")

@login_required
def unapproval_view(request, pk):
    taker = Taker.objects.get(id=pk)
    taker.approve = False
    taker.save()
    return redirect("/core/admin-taker/")

@login_required
def donate_view(request,username, pk):
    user = get_object_or_404(User, username=username)
    donate = get_object_or_404(Donate, pk=pk)
    # user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = DonateForm(request.POST)
        if form.is_valid():
            dilip = form.save(commit=False)
            dilip.giver = request.user
            dilip.taker = user
            dilip.save()
            messages.success(request, "Amount is donated")
            return redirect(".")
        else:
            messages.warning(request, "form is invalid")
            return redirect(".")
    form = DonateForm()
    return render(request, 'core/donate.html', {'form':form})

@login_required
def volunteer(request, pk, username):
    volunteer_taker = get_object_or_404(User, username=username)
    # volunteer_taker = get_object_or_404(Volunteer, volunteer_taker__user=user)
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            dilip = form.save(commit=False)
            dilip.volunteer_taker=volunteer_taker
            dilip.volunteer_giver=request.user
            dilip.save()
            messages.success(request, "your request has been sent to admin")
            return redirect(".")
        messages.success(request, "invalid data")
        return redirect(".")

    form = VolunteerForm()
    return render(request, 'core/volunteer.html', {'form':form})

def volunteer_list_view(request):
    volunteer = Volunteer.objects.all()
    return render(request, 'core/admin_volunteer_list.html', {'volunteer':volunteer})

def donation_history(request):
    if request.user.is_superuser:
        donate = Donate.objects.all()
        context={'donate':donate}
    else:
        donate = Donate.objects.filter(giver=request.user)
        context={'donate':donate}
    return render(request, 'core/donate_history_list.html', context)
@login_required
def feedback_view(request, pk):
    form = FeedbackForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            dilip = form.save(commit=False)
            dilip.feedback_giver=request.user
            dilip.feedback_to = User.objects.get(pk=pk)
            dilip.save()
            return redirect(".")

    donate = Donate.objects.filter(taker=User.objects.get(pk=pk))
    feedback = Feedback.objects.all()
    # taker = Donate.objects.get(User.objects.get(pk=pk))
    context={'donate':donate,
            'form':form,
            'feedback':feedback,
            # 'taker':taker
                }
    return render(request, 'core/feedback.html', context)

####################################################################################################
from django.contrib.auth.hashers import check_password
from django.views import View


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')




from django.shortcuts import render , redirect , HttpResponseRedirect


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

