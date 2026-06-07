# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

## Domain

This system focuses on tracking and searching student reviews for Computer Science professors at Southern New Hampshire University (SNHU). 
This knowledge is highly valuable because official course descriptions only list syllabus topics, completely hiding an instructor's actual
teaching style, grading speed, responsiveness on Discord/email, and clarity of project feedback. Because SNHU has a massive online student
population, these crucial student experiences are buried across hundreds of unorganized Reddit threads and individual review sites, making 
them incredibly difficult for a student to find quickly during course registration.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Which SNHU Computer Science professors are known for giving detailed, helpful feedback on coding projects? | Kraya Ramsey |
| 2 | Is there a specific professor for CS-410 (Programming Languages) who is highly recommended? | Suresh Sigera |
| 3 | Which professors should I avoid generally? | Mike Prasad |
| 4 | How accessible are professors via email or Discord when online students get stuck on a coding assignment? | Depend on the professor, they are suppose to reply within 24 hours, but some professor do not reply at all or some professor reply within an hour |
| 5 | Which instructors are noted for strictly enforcing deadlines versus those who offer extensions? | Daniel Ward |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
