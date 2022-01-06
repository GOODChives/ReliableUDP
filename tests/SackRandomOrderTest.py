import random

from tests.BasicTest import BasicTest

"""
This tests random packet drops. We randomly decide to drop about half of the
packets that go through the forwarder in either direction.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""


class SackRandomOrderTest(BasicTest):
    def __init__(self, forwarder, input_file):
        super(SackRandomOrderTest, self).__init__(forwarder, input_file, sackMode=True)

    def handle_packet(self):
        for p in self.forwarder.in_queue:
            self.forwarder.out_queue.append(p)  # append all
        
        random.shuffle(self.forwarder.out_queue)
        # empty out the in_queue
        self.forwarder.in_queue = []