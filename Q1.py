"""
Author: Jack Edwards
jackedwards1215@gmail.com
April 13, 2024

Q1: Consider a simple class-based messaging system.
This system has two types of members – sender and receiver.
Create classes to model the stream of messages from the sender to the receiver.
Your implementation should have methods for sending a message,
receiving a message, and viewing all of the delivered messages.
"""

# Message objects contain information about sender, receiver, and content
class Message:
  def __init__(self, sender, receiver, content):
    self.sender = sender
    self.receiver = receiver
    self.content = content

# Senders are named but do not keep track of messages
class Sender:
  def __init__(self, name):
    self.name = name
    
  def send_message(self, receiver, content):
    message = Message(self, receiver, content)
    receiver._receive_message(message)

# Receiver has name and dictionary of received message lists
class Receiver:
  def __init__(self, name):
    self.name = name
    self.received_messages = {}

  # Should only be called via send_message unless user constructs message
  def _receive_message(self, message):
    name = message.sender.name
    if name not in self.received_messages:
      self.received_messages[name] = []
    self.received_messages[name].append(message.content)

  def view_messages(self, sender):
    if not isinstance(sender, Sender):
      raise TypeError("%s is not a Sender." % type(sender).__name__)
    if sender.name not in self.received_messages:
      print(f"No messages from {sender.name} to {self.name}")
    else:
      print(f"Messages from {sender.name} to {self.name}:")
      for message in self.received_messages[sender.name]:
        print(f"- {message}")

# Example usage
andy = Sender("Andy")
ben = Sender("Ben")
jack = Receiver("Jack")
kate = Receiver("Kate")

andy.send_message(jack, "What is your favorite color?")
andy.send_message(jack, "Let me know soon, please.")
ben.send_message(jack, "Don't be late for work!")

jack.view_messages(andy)
jack.view_messages(ben)
kate.view_messages(ben)

"""
Things to Consider:

One-way messaging

Senders do not keep track of sent messages:
  Receiver could delete message history entirely
  Tradeoff is less redundancy and no need for centralized data structure

No security:
  Could add authentication methods, e.g. username/password
  Messages could be encrypted by receiver and decrypted by receiver
  No privacy or encapsulation
  
Individual dictionaries of lists not the best way to keep track of messages:
  Real-world implementations use a central database
  
Slightly inefficient hashing by using strings:
  May be marginally faster to use numeric IDs
  User or Conversation IDs would also solve name uniqueness
    

"""