
from BitBooleanFlags import BitBooleanFlags
import unittest

class TestBitBooleanFlagsMethods(unittest.TestCase):

  def test_initialize(self):
      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      self.assertEqual(type(bitBoolenFlags), BitBooleanFlags)

  def test_add_flags(self):
      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      flags = 0
      flags = bitBoolenFlags(flags).add("update","create")

      self.assertTrue(bitBoolenFlags(flags).has("create"))
      self.assertTrue(bitBoolenFlags(flags).has("update"))
      self.assertFalse(bitBoolenFlags(flags).has("read"))
      self.assertFalse(bitBoolenFlags(flags).has("delete"))

      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      flags = 0
      flags = bitBoolenFlags(flags).add("update","create")

      self.assertTrue(bitBoolenFlags(flags).has("create"))
      self.assertTrue(bitBoolenFlags(flags).has("update"))
      self.assertFalse(bitBoolenFlags(flags).has("read"))
      self.assertFalse(bitBoolenFlags(flags).has("delete"))
      
  def test_remove_flags(self):
      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      flags = 0
      flags = bitBoolenFlags(flags).add("update","create")

      self.assertTrue(bitBoolenFlags(flags).has("create"))
      self.assertTrue(bitBoolenFlags(flags).has("update"))
      self.assertFalse(bitBoolenFlags(flags).has("read"))
      self.assertFalse(bitBoolenFlags(flags).has("delete"))

      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      flags = 0
      flags = bitBoolenFlags(flags).add("update","create")

      self.assertTrue(bitBoolenFlags(flags).has("create"))
      self.assertTrue(bitBoolenFlags(flags).has("update"))
      self.assertFalse(bitBoolenFlags(flags).has("read"))
      self.assertFalse(bitBoolenFlags(flags).has("delete"))

      flags = bitBoolenFlags(flags).remove("update")

      self.assertTrue(bitBoolenFlags(flags).has("create"))
      self.assertFalse(bitBoolenFlags(flags).has("update"))
      self.assertFalse(bitBoolenFlags(flags).has("read"))
      self.assertFalse(bitBoolenFlags(flags).has("delete"))

  def test_key_exceptions(self):
      bitBoolenFlags = BitBooleanFlags("create","read","update","delete")
      flags = 0
      flags = bitBoolenFlags(flags).add("update","create")
      with self.assertRaises(KeyError):
          bitBoolenFlags(flags).has("kill")
          bitBoolenFlags(flags).add("kill")
          bitBoolenFlags(flags).remove("kill")

if __name__ == '__main__':
    unittest.main()