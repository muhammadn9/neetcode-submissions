class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> check = new HashSet<>();
        for(int num : nums) {
            if(!check.add(num)) return true;
        }
        return false;

        //Initialize the HashSet
        //for loop goes through the nums since we care for the values
        //not the indexes
    }
}