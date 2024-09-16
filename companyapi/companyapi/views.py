from django.http import HttpResponse, HttpRequest, JsonResponse, request
import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import transaction
## Assignment 2 starts here
##Yes Django signals runs in the same thread as the caller by default
# Signal receiver
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
    print(f"Signal received at: {now()}")
    # Simulate a long-running task
    time.sleep(2)
    print(f"Signal handler finished at: {now()}")

# In the view or wherever you trigger the save action
def save_user_view(request):
    print(f"User save process started in thread: {threading.current_thread().name}")
    print(f"User save process started at: {now()}")
    user = User.objects.create(username="testuser124")
    print(f"User save process ended at: {now()}")
    return HttpResponse("User created")

#### Assignment 2 ends here

#### Assignment 3 starts from here

##Yes by default they run in the same database transaction
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received, creating log for user: {instance.username}")
        # Simulate database action inside the signal
        instance.profile_log = 'Log for ' + instance.username
        instance.save()

# Test the transaction behavior
def create_user_in_transaction():
    try:
        with transaction.atomic():
            print("Creating user inside transaction")
            user = User.objects.create_user('testuser27', 'test23@example.com', 'password')
           
            # Simulating an error to trigger a rollback
            raise ValueError("Error to test transaction rollback")
   
    except Exception as e:
        print(f"Transaction failed: {e}")

# Assuming Django environment is properly set up, this will trigger the signal
create_user_in_transaction()

#### Assignment 3 ends here


######   Assignment 1 Code start from here

## Yes, Django singals are synchronous.
# Define a custom signal
task_completed = Signal()

# Define a receiver function for the signal
@receiver(task_completed)
def signal_handler(sender, **kwargs):
    print("Signal received, starting task...")
    time.sleep(5)  # Simulate a time-consuming task
    print("Task completed.")

# Simulate sending the signal
##def signal_new():
print("Sending signal...")
task_completed.send(sender=None)
print("Signal has been sent, moving to next task...")

#### Assignemnt 1 code ends here

#### Assignment 4 code starts from here
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Use a list to store the dictionary representations of length and width
        self._attributes = [{'length': self.length}, {'width': self.width}]
        self._index = 0  # Initialize the iterator index
        return self

    def __next__(self):
        if self._index < len(self._attributes):
            result = self._attributes[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration  # When iteration is complete

# Example usage:
rectangle = Rectangle(100, 80)

for attribute in rectangle:
    print(attribute)


###### Assignment 4 code ends here
