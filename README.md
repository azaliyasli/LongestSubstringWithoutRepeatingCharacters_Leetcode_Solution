# 🟡 Longest Substring Without Repeating Characters

**Problem link:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
**Difficulty:** Medium  
**Runtime:** 1138 ms  
**Memory Usage:** 18 MB  

---

### 🧠 Approach
- Use a **brute-force** method.
- Loop through each index `i` in the string.
- At each position, build a substring (`substringList`) by adding characters one by one.
- If a character is repeated, break the loop.
- Update `maxLength` if the current substring is longer.

Although not an optimal one, this solution clearly demonstrates the logic of checking for duplicates and substring expansion.
