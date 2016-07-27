"""Tests for records."""

import cPickle as pickle
import unittest

import mutablerecords

TestRecord = mutablerecords.Record(
    'TestRecord', ['required'], {'optional': 'opt_value'})

Name = mutablerecords.Record('Name', ['required'], {'name_opt': True})
Simple = mutablerecords.Record('Simple', [], {'simple': True})
Recursive = mutablerecords.Record(
    'Recursive', [], {'subrec': Simple, 'lst': list})


class Subclass(mutablerecords.Record('Rec', ['req'], {'opt': None})):
    def ExtraMethod(self):
        return True


class RecordsTest(unittest.TestCase):

    def testRecordCreation(self):
        obj = Name('req')
        self.assertEqual(obj.required, 'req')
        self.assertTrue(obj.name_opt)

        obj = Name('req2', name_opt=5)
        self.assertEqual(obj.required, 'req2')
        self.assertEqual(obj.name_opt, 5)

    def testCopyRecord(self):
        obj = Name('name')
        new_obj = mutablerecords.CopyRecord(obj)
        self.assertIsNot(obj, new_obj)

        self.assertIsInstance(Recursive().subrec, Simple)
        self.assertEqual(Recursive().lst, [])
        rec_obj = Recursive()
        new_rec_obj = mutablerecords.CopyRecord(rec_obj)
        self.assertIsNot(rec_obj, new_rec_obj)
        self.assertIsNot(rec_obj.subrec, new_rec_obj.subrec)
        self.assertIsNot(rec_obj.lst, new_rec_obj.lst)
        self.assertEqual(rec_obj.lst, [])

    def testPickleRecord(self):
        rec_obj = Name('reqd_value')
        pickled_obj = pickle.loads(pickle.dumps(rec_obj))
        self.assertEqual(rec_obj, pickled_obj)
        self.assertEqual(Name, type(pickled_obj))

    def testPickleRecordSubclass(self):
        obj = Subclass(True)
        unpickled = pickle.loads(pickle.dumps(obj))
        self.assertEqual(obj, unpickled)
        self.assertTrue(unpickled.ExtraMethod())


if __name__ == '__main__':
    unittest.main()
