import os
import shutil

import swiss

storage_path = '/tmp/pdfator-test/storage'
storage = swiss.Cache(storage_path)
from collections import deque
class Queue(deque):
    pass
queue = Queue()

def get_text(name):
    # id = map_name_to_id(name)
    id = name
    stream = storage.stream(id)
    if stream is None:
        queue.append(name)
        return 'No PDF text yet, added to queue, please check back in 10m'
    else:
        return stream

class TestItAll:
    name = '1609'

    @classmethod
    def setup_class(self):
        if os.path.exists(storage_path):
            shutil.rmtree(storage_path)
        os.makedirs(storage_path)
        fp = storage.cache_path(self.name)
        fo = open(fp, 'w')
        fo.write('Testing')
    
    @classmethod
    def teardown_class(self):
        pass

    def test_get_text(self):
        out = get_text('1608')
        assert out.startswith('No PDF')

    def test_get_text_real(self):
        out = get_text('1609')
        assert out.read() == 'Testing'

