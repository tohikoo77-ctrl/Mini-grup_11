from django.urls import path

from .views import CreateUserView, VerifyAPIView, GetNewVerification, \
    UpdateUserInformationView, LoginView, LoginRefreshView, \
    LogOutView, ResetPasswordView, PasswordGeneratorView, test_login, ForgotPasswordView

urlpatterns = (
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('test-login/', test_login, name='test-login'),
    path('', UpdateUserInformationView.as_view(), name='update'),
    path('generate-password/', PasswordGeneratorView.as_view(), name='generate-password'),
    path('login/refresh/', LoginRefreshView.as_view(), name='refresh'),
    path('new-verify/', GetNewVerification.as_view(), name='new-verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('forget-password/', ForgotPasswordView.as_view(), name='forget-password'),
    path('reset-password/', ResetPasswordView.as_view()),
)