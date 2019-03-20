from pyfcm import FCMNotification

__all__ = ('messaging', )


def messaging(message_body, category, order, registration_id):
    data_message = {'category': category,
                    'order': order}
    message_title = "completed"
    api_key = "AIzaSyD85T_x9TX2shewTUJyk6l_LrQboiLM7KU"
    push_service = FCMNotification(api_key=api_key)
    push_service.notify_single_device(
        registration_id=registration_id,
        message_title=message_title,
        message_body=message_body,
        data_message=data_message
    )


<script src="https://www.gstatic.com/firebasejs/4.6.0/firebase.js"></script>
<script>
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyD85T_x9TX2shewTUJyk6l_LrQboiLM7KU",
    authDomain: "taxpaas.firebaseapp.com",
    databaseURL: "https://taxpaas.firebaseio.com",
    projectId: "taxpaas",
    storageBucket: "",
    messagingSenderId: "172264775750"
  };
  firebase.initializeApp(config);
</script>