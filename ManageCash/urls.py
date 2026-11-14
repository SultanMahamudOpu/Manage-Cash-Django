from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Home and Dashboard
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # User Profile
    path('profile/', views.profile, name='profile'),

    # Cash and Expense
    path('add-cash/', views.add_cash, name='add_cash'),
    path('add-expense/', views.add_expense, name='add_expense'),

    # Transactions
    path('transactions/', views.transactions, name='transactions'),

    # Edit Transactions
    path('edit-cash/<int:pk>/', views.edit_cash, name='edit_cash'),
    path('edit-expense/<int:pk>/', views.edit_expense, name='edit_expense'),

    # Delete Transactions
    path('delete-cash/<int:pk>/', views.delete_cash, name='delete_cash'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='delete_expense'),
]
