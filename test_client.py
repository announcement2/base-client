import announcement_client
import time

@announcement_client.announcement_callback
def announcement(message, sender):
    print('New Announcement: "{}" from {}'.format(message, sender))

announcement_client.run_client('test')

x = 1
while True:
    announcement_client.announce('This is a test message that is sent every 5 seconds. Count: {}'.format(x), 'test')
    x += 1
    time.sleep(5)
