"""Tests for records."""

import unittest

import mutablerecords


class RecordsTest(unittest.TestCase):

    def testRecordCreation(self):
        cls = mutablerecords.Record('Name', ['required'], {'optional': True})
        obj = cls('req')
        self.assertEqual(obj.required, 'req')
        self.assertTrue(obj.optional)

        obj = cls('req2', optional=5)
        self.assertEqual(obj.required, 'req2')
        self.assertEqual(obj.optional, 5)

    def testCopyRecord(self):
        cls = mutablerecords.Record('Name', [], {'optional': True})
        obj = cls()
        new_obj = mutablerecords.CopyRecord(obj)
        self.assertIsNot(obj, new_obj)

        rec_cls = mutablerecords.Record(
            'Recursive', [], {'subrec': cls, 'lst': list})
        self.assertIsInstance(rec_cls().subrec, cls)
        self.assertEqual(rec_cls().lst, [])
        rec_obj = rec_cls()
        new_rec_obj = mutablerecords.CopyRecord(rec_obj)
        self.assertIsNot(rec_obj, new_rec_obj)
        self.assertIsNot(rec_obj.subrec, new_rec_obj.subrec)
        self.assertIsNot(rec_obj.lst, new_rec_obj.lst)
        self.assertEqual(rec_obj.lst, [])


if __name__ == '__main__':
    unittest.main()
