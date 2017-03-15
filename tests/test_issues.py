"""Test the with statement for Byterun."""

from __future__ import print_function
from . import vmtest
from byterun import issue

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
        assert(res.issues[0] == issue.TypeChange(type(5),
                                               type(""),
                                               "a"))
        assert(len(res.issues) == 1)

    def test_types_consistent(self):
        res = self.assert_ok("""\
                def foo():
                    a = 5
                    bar()
                def bar():
                    a = "fish"
                foo()
                """)
        assert(len(res.issues) == 0)
    
    def test_object_sametype(self):
        res = self.assert_ok("""\
                import datetime
                class newdatetime(datetime.datetime):
                    pass
                a = datetime.datetime(12, 12, 12)
                a = newdatetime(12, 12, 12)
                """)
        assert(len(res.issues) == 0)
    
    def test_object_difftype(self):
        res = self.assert_ok("""\
                import datetime
                class newdatetime(datetime.datetime):
                    pass
                a = datetime.datetime(12, 12, 12)
                a = datetime.time()
                """)
        assert(res.issues[0] == issue.TypeChange(type(5),
                                               type(""),
                                               "a"))
        assert(len(res.issues) == 1)
                

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
        assert(res.issues[0] == issue.DictionaryIter())
        assert(len(res.issues) == 1)

    def test_iter_dict_keys(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.keys():
                    pass
                """)
        assert(len(res.issues) == 0)

    def test_iter_dict_values(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.values():
                    pass
                """)
        assert(len(res.issues) == 0)

    def test_iter_dict_items(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.items():
                    pass
                """)
        assert(len(res.issues) == 0)

    def test_iter_dict_iteritems(self):
        res = self.assert_ok("""\
                a = {'a': 1, 'b': 2, 'c': 3}
                for _ in a.iteritems():
                    pass
                """)
        assert(len(res.issues) == 0)
