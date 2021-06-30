#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##
# Copyright 2021 FIWARE Foundation, e.V.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
##

import HtmlTestRunner
from tests.testlinks import ChromeSearch
from unittest import main, TestLoader, TextTestRunner

__author__ = 'Fernando López'

if __name__ == "__main__":
    main()

    suite = TestLoader().loadTestsFromTestCase(ChromeSearch)
    TextTestRunner(verbosity=2).run(suite)

    outfile = open("report.html", "w")

    runner = HtmlTestRunner.HTMLTestRunner(
                    stream=outfile,
                    report_title='Test Report')

    runner.run(suite)