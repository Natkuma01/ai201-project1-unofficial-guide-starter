# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

This system focuses on aggregating and indexing student reviews for Computer Science professors at Southern New Hampshire University (SNHU). Because SNHU has a massive online student body, genuine student insights regarding professor teaching styles, grading strictness, and responsiveness are scattered across deep Reddit threads and individual review pages. This system centralizes that knowledge, making it easy for students to quickly find the best instructors for their learning style before registration.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Rate My Professors | Rating of all professors from the CS department in SNHU | https://www.ratemyprofessors.com/search/professors/667?q=*&did=11 |
| 2 | Reddit (r/SNHU) | Comprehensive thread on CS Professors to choose or avoid | https://www.reddit.com/r/SNHU/comments/mlry5g/cs_professors_to_chooseavoid |
| 3 | Reddit (r/SNHU) | Student recommendations for the best CS Major Professors | https://www.reddit.com/r/SNHU/comments/18ce4w2/best_computer_science_major_professors_ive_had_so/ |
| 4 | Reddit (r/SNHU) | Instructor selection advice for difficult courses like CS330/CS340 | https://www.reddit.com/r/SNHU/comments/pogy8i/help_picking_good_instructors/ |
| 5 | Reddit (r/SNHU) | Discussion thread tracking experiences in CS 210 and student burnout | https://www.reddit.com/r/SNHU/comments/1s3lq09/cs_210_woes/ |
| 6 | Rate My Professors | Professor Loay Alnaji - Computer Science Profile | https://www.ratemyprofessors.com/professor/2290372 |
| 7 | Rate My Professors | Professor Cynthia Marcello - Computer Science Profile | https://www.ratemyprofessors.com/professor/2103445 |
| 8 | Rate My Professors | Professor James Shinevar - Computer Science Profile | https://www.ratemyprofessors.com/professor/2642511 |
| 9 | Rate My Professors | Professor Megan Allen Black - Computer Science Profile | https://www.ratemyprofessors.com/professor/2789110 |
| 10 | Rate My Professors | Professor Robert Whale - Computer Science Profile | https://www.ratemyprofessors.com/professor/2591140 |


---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Which SNHU Computer Science professors are known for giving detailed, helpful feedback on coding projects? | Kraya Ramsey |
| 2 | Is there a specific professor for CS-410 (Programming Languages) who is highly recommended? | Suresh Sigera |
| 3 | Which professors should I avoid generally? | Mike Prasad |
| 4 | How accessible are professors via email or Discord when online students get stuck on a coding assignment? | Depend on the professor, they are suppose to reply within 24 hours, but some professor do not reply at all or some professor reply within an hour |
| 5 | Which instructors are noted for strictly enforcing deadlines versus those who offer extensions? | Daniel Ward |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
