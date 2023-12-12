from django.shortcuts import redirect

from .models import PaymentManager

from main.models import Notification, RentalManager, NotificationTypes

# Create your views here.
def payment_view(request, notification_id):
    pay_notification = Notification.objects.filter(id=notification_id)[0]
    notification = Notification.objects.filter(
        game = pay_notification.game, 
        user_sender = pay_notification.user_receiver, 
    )
    
    notification = notification.last()
    
    new_payment = PaymentManager()
    new_payment.handle_payment(notification.user_sender, notification.game)
    pay_notification.set_title('Pagamento Concluido')
    pay_notification.set_isActive(False)
    
    notification.set_title("Empréstimo - Pago")

    response = Notification()
    response.newNotification(
        title='Resultado: Empréstimo',
        description=f"O usuário @{notification.user_receiver.username} aceitou emprestar o jogo {notification.game.title}!",
        receiver=notification.user_sender,
        type=NotificationTypes.info
    )
    
    return redirect('home')