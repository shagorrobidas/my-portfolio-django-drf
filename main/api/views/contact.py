from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
from main.models import ContactMessage
from main.api.serializers.contact import ContactMessageSerializer


class ContactMessageCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    authentication_classes = []  # Exempt from CSRF/Session auth

    def perform_create(self, serializer):
        # Save the instance first
        instance = serializer.save()

        # Send email notification
        subject = f"New Portfolio Contact: {instance.subject}"
        message = (
            f"From: {instance.full_name} <{instance.email}>\n\n"
            f"Subject: {instance.subject}\n\n"
            f"Message:\n{instance.message}"
        )
        recipient_list = [settings.CONTACT_EMAIL]

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            # We log the error but don't fail the request since the message is saved
            print(f"Error sending contact email: {e}")

