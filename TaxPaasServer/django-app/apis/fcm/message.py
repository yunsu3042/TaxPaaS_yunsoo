from pyfcm import FCMNotification

__all__ = ('messaging', )


def messaging(message_body, category, order, registration_id):
    data_message = {'category': category,
                    'order': order}
    message_title = "completed"
    api_key = ""
    push_service = FCMNotification(api_key=api_key)
    push_service.notify_single_device(
        registration_id=registration_id,
        message_title=message_title,
        message_body=message_body,
        data_message=data_message
    )