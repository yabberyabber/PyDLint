"""Test the with statement for Byterun."""

from __future__ import print_function
from . import vmtest
from byterun import issue

import sys

import six
PY3 = six.PY3

class TestTypesIssues(vmtest.VmTestCase):
    """
    Issue a warning on variable type change
    """
    def test_change_types(self):
        res = self.assert_ok("""\
                a = 5
                a = "oops"
                """)
        self.assertEqual(res.issues[0], issue.TypeChange(type(5),
                                               type(""),
                                               "a"))
        self.assertEqual(len(res.issues), 1)

    def test_types_consistent(self):
        res = self.assert_ok("""\
                def foo():
                    a = 5
                    bar()
                def bar():
                    a = "fish"
                foo()
                """)
        self.assertEqual(len(res.issues), 0)
    
    def test_object_sametype(self):
        res = self.assert_ok("""\
                import datetime
                class newdatetime(datetime.datetime):
                    pass
                a = datetime.datetime(12, 12, 12)
                a = newdatetime(12, 12, 12)
                """)
        self.assertEqual(len(res.issues), 0)
    
    def test_object_difftype(self):
        import datetime
        res = self.assert_ok("""\
                import datetime
                class newdatetime(datetime.datetime):
                    pass
                a = datetime.datetime(12, 12, 12)
                a = datetime.time()
                """)
        self.assertEqual(res.issues[0],
                issue.TypeChange(type(datetime.datetime(12, 12, 12)),
                                 type(datetime.time()),
                                 "a"))
        self.assertEqual(len(res.issues), 1)
                

class TestDictIter(vmtest.VmTestCase):
    """
    Issue a warning on iteration through naked dict
    """
    def test_iter_dict_bad(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a:
                    pass
                """)
        self.assertEqual(res.issues[0], issue.DictionaryIter())
        self.assertEqual(len(res.issues), 1)

    def test_iter_dict_keys(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.keys():
                    pass
                """)
        self.assertEqual(len(res.issues), 0)

    def test_iter_dict_values(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.values():
                    pass
                """)
        self.assertEqual(len(res.issues), 0)

    def test_iter_dict_items(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.items():
                    pass
                """)
        self.assertEqual(len(res.issues), 0)

    def test_iter_dict_iteritems(self):
        if sys.version_info.major == 2:
            res = self.assert_ok("""\
                    a = {'a': 1, 'b': 2, 'c': 3}
                    for _ in a.iteritems():
                        pass
                    """)
            self.assertEqual(len(res.issues), 0)

    def test_set_caps(self):
        res = self.assert_ok("""\
                CONSTANT = 6
                """)
        self.assertEqual(len(res.issues), 0)
