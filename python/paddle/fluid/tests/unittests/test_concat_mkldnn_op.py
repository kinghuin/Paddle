#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import unittest
from test_concat_op import TestConcatOp, TestConcatOp2, TestConcatOp3


class TestMKLDNNConcatOp(TestConcatOp):
    def setUp(self):
        super(TestMKLDNNConcatOp, self).setUp()
        self.attrs["use_mkldnn"] = True

    def test_check_grad(self):
        pass

    def init_kernel_type(self):
        self.use_mkldnn = True

class TestMKLDNNConcatOp2(TestConcatOp2):
    def setUp(self):
        super(TestMKLDNNConcatOp2, self).setUp()
        self.attrs["use_mkldnn"] = True

    def test_check_grad(self):
        pass

    def init_kernel_type(self):
        self.use_mkldnn = True

class TestMKLDNNConcatOp3(TestConcatOp3):
    def setUp(self):
        super(TestMKLDNNConcatOp3, self).setUp()
        self.attrs["use_mkldnn"] = True

    def test_check_grad(self):
        pass

    def init_kernel_type(self):
        self.use_mkldnn = True


if __name__ == '__main__':
    unittest.main()
