# leetcode-2812-o-n2-solution
a pure O(n²) solution – faster than the standard O(n² log n) approaches.
​# An $O(n^2)$ Solution for LeetCode 2812 – Faster than the Standard Approach

Hello! I am **AL-ASADI HUSAM ADEL HADI ALI**, a Yemeni student currently studying in Chongqing, China[span_0](start_span)[span_0](end_span). This project is the result of my work developing an innovative solution for the **Maximum Safeness Factor** problem (LeetCode 2812)[span_1](start_span)[span_1](end_span).

While standard optimal approaches run in $O(n^2 \log n)$ time complexity[span_2](start_span)[span_2](end_span), this solution achieves a true **$O(n^2)$** time complexity[span_3](start_span)[span_3](end_span).

---

## The Core Idea

During my study of Python and Breadth-First Search (BFS) algorithms, I observed that the difference in Manhattan distance between any two adjacent cells is always **at most 1**[span_4](start_span)[span_4](end_span).

This key observation allowed me to design a "forward-looking radar" mechanism that dynamically selects the best immediate move without the overhead of a Min-Heap (Dijkstra) or Binary Search[span_5](start_span)[span_5](end_span). This directly reduces the overall time complexity:

1. **Phase 1 (Multi-source BFS):** A standard multi-source BFS is run from all thief coordinates to compute the minimum safeness distance for every cell in the grid[span_6](start_span)[span_6](end_span).
2. **Phase 2 (Guided Expansion):** A targeted traversal using a standard queue, utilizing diagonal bridge-checks to ensure each cell is visited only a constant number of times[span_7](start_span)[span_7](end_span).

---

## Complexity Analysis

* **Time Complexity:** $O(n^2)$ – We traverse the grid a constant number of times[span_8](start_span)[span_8](end_span).
* **Space Complexity:** $O(n^2)$ – To store the distance grid and the traversal queues[span_9](start_span)[span_9](end_span).

---

## Repository Files

* `solution.py` : The final optimized implementation in Python 3[span_10](start_span)[span_10](end_span).
* `README.md` : This explanatory document[span_11](start_span)[span_11](end_span).

---

## My LeetCode Profile

You can find my LeetCode profile and check out my submissions here:
👉 [leetcode.com/u/Haudsialm/](https://leetcode.com/u/Haudsialm/)[span_12](start_span)[span_12](end_span)

---

## Connect with Me

I am always open to connecting with professionals, educators, and fellow developers!

* **LinkedIn:** [Husam Adel Hadi Ali AL-ASADI](https://www.linkedin.com/in/husam-adel-hadi-ali-al-asadi-6572b03aa)[span_13](start_span)[span_13](end_span)
* **Email:** [haudsialm@gmail.com](mailto:haudsialm@gmail.com)[span_14](start_span)[span_14](end_span)

---

> **Note:** I am at the beginning of my university journey and am actively seeking learning opportunities, academic mentorship, or guidance[span_15](start_span)[span_15](end_span). I would be deeply grateful for any feedback, code reviews, or advice you can share[span_16](start_span)[span_16](end_span)!
