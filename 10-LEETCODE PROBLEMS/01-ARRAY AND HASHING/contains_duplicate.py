import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
class TestContainsDuplicate(unittest.TestCase):

    def test_empty_array(self):
        """Test with an empty array."""
        nums = []
        result = Solution().containsDuplicate(nums)
        self.assertFalse(result)

    def test_single_element_array(self):
        """Test with an array containing a single element."""
        nums = [1]
        result = Solution().containsDuplicate(nums)
        self.assertFalse(result)

    def test_array_with_duplicates(self):
        """Test with an array containing duplicates."""
        nums = [1, 2, 3, 1]
        result = Solution().containsDuplicate(nums)
        self.assertTrue(result)

    def test_array_without_duplicates(self):
        """Test with an array without duplicates."""
        nums = [1, 2, 3, 4]
        result = Solution().containsDuplicate(nums)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
