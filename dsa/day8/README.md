# 📦 DSA – Day 8

### ✅ Problems Solved:
1. [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
2. [Peak element](https://leetcode.com/problems/find-peak-element/)
3. [Minimum in rotated sorted array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

---

## 🧠 Learnings & Takeaways
- Finding median of two sorted arrays
- **Binary Search isn’t just about sorted arrays.** It's a versatile tool for problems where the answer lies in a **monotonic search space**.
- Learned how to shrink search space based on patterns like `nums[mid] > nums[mid+1]` or `nums[mid] > nums[right]`.
- Realized that:
  - When looking for *peaks*, we follow the slope.
  - When looking for *minimums*, we trust the unsorted half.
- Improved intuition for when to move `left = mid + 1` vs. `right = mid`.
- Strengthened understanding of binary edge conditions and loop invariants (`left <= right` vs. `left < right`).
- Getting more comfortable breaking down and **dry-running** binary search iterations.

🔥 Binary search is no longer scary — it’s a pattern I can now twist and control confidently.
