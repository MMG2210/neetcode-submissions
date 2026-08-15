class Solution {
    List<Integer> subset = new ArrayList<>();
    Set<List<Integer>> powerSet = new HashSet<>();

    private void backtrack(int[] nums, int idx){
        if(idx == nums.length){
            powerSet.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[idx]);
        backtrack(nums, idx + 1);
        subset.remove(subset.size() - 1);
        backtrack(nums, idx + 1);
    }

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0);
        return new ArrayList<>(powerSet);
    }
}
