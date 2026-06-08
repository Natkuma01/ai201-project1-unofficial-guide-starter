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
| 6 | Rate My Professors | Professor Philip Enkema - Computer Science Profile | https://www.ratemyprofessors.com/professor/2810257 |
| 7 | Rate My Professors | Professor Mahmud Hasan - Computer Science Profile | https://www.ratemyprofessors.com/professor/2860204 |
| 8 | Rate My Professors | Professor Jason Proske - Computer Science Profile | https://www.ratemyprofessors.com/professor/2112092 |
| 9 | Rate My Professors | Professor Thomas Butler - Computer Science Profile | https://www.ratemyprofessors.com/professor/2883676|
| 10 | Rate My Professors | Professor Vivian Lyon - Computer Science Profile | https://www.ratemyprofessors.com/professor/2706344 |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
500 characters

**Overlap:**
100 characters

**Why these choices fit your documents:**
Student responses on platforms like Reddit or Rate My Professors are typically dense, opinion-driven, and short (ranging from 1 to 3 paragraphs). 
A chunk size of 500 characters cleanly isolates a student's individual sentiment without diluting their review with comments about completely 
different professors or courses. The 100-character sliding window overlap serves as a bridge, ensuring that names, course codes 
(like CS-210), or structural context are not clipped across string slice thresholds. Prior to running this slicing mechanism, our 
preprocessing pipeline clean-normalizes excessive spaces, newlines, and structural blank lines to optimize vector space density.

**Final chunk count:**
180 chunks
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2 
**Production tradeoff reflection:**
If this tool were scaled for a production ecosystem serving thousands of active users, we would weigh upgrading to a hosted commercial embedding engine like OpenAI's `text-embedding-3-large` or Cohere's native models. Commercial engines provide significantly larger token context windows and deeper accuracy on nuanced, domain-specific slang (e.g., matching student shorthand like "prof", "easy A", or course codes more robustly). However, switching to a hosted API introduces financial per-query costs and external network latency. Our current model runs locally on disk with zero cost, no rate-limiting, and immediate availability.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
Our system prompt in `app.py` isolates the LLM's attention using explicit boundary rules and direct instructions to eliminate hallucinations:
You are an assistant for the Unofficial Guide to SNHU Computer Science professors. Your absolute core directive is to answer the user's question using ONLY the provided text fragments. 
Strict Guidelines: 
1. Rely exclusively on the clear facts mentioned directly in the fragments. 
2. Do NOT use outside general knowledge or assumptions about professors. 
3. If the provided text fragments do not contain enough specific facts to answer the question, you must respond word-for-word with: 'I do not have enough information on that based on student reviews.' 
4. Keep your response factual, concise, and professional.

**How source attribution is surfaced in the response:**
Source attribution is enforced programmatically outside the influence of the language model's text window. When ChromaDB queries text chunks, our Python backend extracts the `source` attribute directly from the chunk's accompanying metadata (`meta['source']`). These names are collected into a unique Python `set()` to eliminate duplicates, sorted, and pushed directly into a dedicated Gradio `sources_box` component. This system architecture guarantees that citations cannot be fabricated or hallucinated by the LLM.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Which SNHU Computer Science professors are known for giving detailed, helpful feedback on coding projects? | Relevant |
| 2 | Is there a specific professor for CS-230 (Programming Languages) who is highly recommended? | Relevant |
| 3 | Which professors should I avoid generally? | Off-target |
| 4 | How accessible are professors via email or Discord when online students get stuck on a coding assignment? | Relevant |
| 5 | Which instructors are noted for strictly enforcing deadlines versus those who offer extensions? | Off-target |

**Retrieval quality:** Relevant  
**Response accuracy:** Accurate 

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
"what professor you recommend for CS410"

**What the system returned:**
"I do not have enough information on that based on student reviews."

**Root cause (tied to a specific pipeline stage):**
While our text documents successfully cover course reviews for introductory and full-stack classes, our raw data collection completely lacks 
any student review text mentioning "CS-410". Because this data is missing from the physical text files, the embedding model (`all-MiniLM-L6-v2`) 
could not find semantic matches in ChromaDB. The generation pipeline worked correctly by enforcing our strict system prompt safety 
guardrail, preventing a hallucination by refusing to answer.

**What you would change to fix it:**
To fix this, I would expand the data corpus by scraping or copying student reviews specifically from the r/SNHU subreddit 
or Rate My Professors pages that mention CS-410. I would save this data into a new `doc11.txt` file inside the `data/` folder 
and re-run `python ingest.py` to rebuild the vector store embeddings.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Drafting `planning.md` forced me to establish my mechanical chunking rules (500 character boundaries and 100 character overlaps) 
before writing any code. Having these design requirements locked down prevented guessing games during implementation, allowing 
me to build a clean index-based sliding loop directly within `ingest.py` on the first try.

**One way your implementation diverged from the spec, and why:**
Our initial specification assumed that the LLM would dynamically read context documents and format its own textual inline citations. 
During development, I realized this left a structural vulnerability to citation hallucination. I changed the design to extract 
the metadata directly from ChromaDB's query results using standard Python dictionaries, bypassing the LLM entirely for source attribution.

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
  I provided the model with my manual string cleaning requirements and asked it to construct a sliding character window loop for `ingest.py`.
- *What it produced:*
  It generated a standard indexing loop that stepped through strings using arithmetic offsets based on character length.
- *What I changed or overrode:*
  I manually inserted an explicit conditional check (`if len(chunk_content) > 0`) to act as a strict pipeline filter, ensuring that empty space strings wouldn't get saved into the vector store database.

**Instance 2**

- *What I gave the AI:*
  I supplied my exact grounding requirements and asked it to write a system prompt to keep the Groq LLM contained to the retrieved chunks.
- *What it produced:*
  It returned a generalized prompt instructing the model to focus on the provided context and try its best to be helpful.
- *What I changed or overrode:*
  I rewrote the phrasing to replace open-ended instructions with rigid constraints, incorporating a mandatory, word-for-word string match fallback requirement to ensure completely predictable response behavior when information is missing.
