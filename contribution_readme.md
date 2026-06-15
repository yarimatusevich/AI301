# Contribution [#1]: Pandas DataFrame.update Silent Error

**Contribution Number:** 1
**Student:** Yaroslav Matusevich  
**Issue:** https://github.com/pandas-dev/pandas/issues/19905
**Status:** Phase 1 Complete

---

## Why I Chose This Issue

[1-2 paragraphs explaining why this issue interests you, how it matches your skills/learning goals, what you hope to learn]


This issue interests me because pandas is a library I use regularly in my Python work, and contributing to it feels like a natural next step in deepening my understanding of how it actually works under the hood. The bug itself is a silent failure that definitely is a headache to encounter when using the library, so I want to fix it.

Solving this bug requires Python, which I have substantial experience with, and this feels like a good opportunity to get hands-on experience contributing code to a large, established codebase. I want to move beyond writing Python in isolation and understand how production-scale projects are structured and maintained.
---

## Understanding the Issue

### Problem Description

DataFrame.update() modifies a data frame using the values from another data frame. When you pass raise_conflict=1, as a parameter Pandas ignores it and does not raise any errors.

### Expected Behavior

When a user passes an invalid or unrecognized keyword argument to DataFrame.update(), pandas should raise an error.

### Current Behavior

Passing raise_conflict=True (or any unrecognized keyword) to DataFrame.update() does nothing.

### Affected Components

pandas/core/frame.py

---

## Reproduction Process

### Environment Setup

[Notes on setting up your local development environment - challenges you faced, how you solved them]
Setup a python virtual environment and installed Pandas using pip.

### Steps to Reproduce

1. Created two data frames with overlapping values.
2. Call df.update(raise_conflict=True) on one the data frames using the other.
3. No errors are raied and df1 (the oen I called .update on) is silently updated.

### Reproduction Evidence

- **Commit showing reproduction:** https://github.com/yarimatusevich/AI301/blob/main/error_reprod.py
- **Screenshots/logs:** <img width="246" height="208" alt="image" src="https://github.com/user-attachments/assets/966cd34b-8140-48a2-ad47-19939fa9afec" />
- **My findings:**
- Pandas indeed does not raise a conflict error if there are mismatching data types between two dataframes. Although the .update function still behaves correctly (not changing anything), the error silently falls through as a result this keeps user in the
- dark as to what actually went wrong. 

---

## Solution Approach

### Analysis

[Your analysis of the root cause - what's causing the issue?]

### Proposed Solution

[High-level description of your fix approach]

### Implementation Plan

Using UMPIRE framework (adapted):

**Understand:** [Restate the problem]

**Match:** [What similar patterns/solutions exist in the codebase?]

**Plan:** [Step-by-step implementation plan]
1. [Modify file X to do Y]
2. [Add function Z]
3. [Update tests]

**Implement:** [Link to your branch/commits as you work]

**Review:** [Self-review checklist - does it follow the project's contribution guidelines?]

**Evaluate:** [How will you verify it works?]

---

## Testing Strategy

### Unit Tests

- [ ] Test case 1: [Description]
- [ ] Test case 2: [Description]
- [ ] Test case 3: [Description]

### Integration Tests

- [ ] Integration scenario 1
- [ ] Integration scenario 2

### Manual Testing

[What you tested manually and results]

---

## Implementation Notes

### Week [X] Progress

[What you built this week, challenges faced, decisions made]

### Week [Y] Progress

[Continue documenting as you work]

### Code Changes

- **Files modified:** [List]
- **Key commits:** [Links to important commits]
- **Approach decisions:** [Why you chose certain approaches]

---

## Pull Request

**PR Link:** [GitHub PR URL when submitted]

**PR Description:** [Draft or final PR description - much of the content above can be adapted]

**Maintainer Feedback:**
- [Date]: [Summary of feedback received]
- [Date]: [How you addressed it]

**Status:** [Awaiting review / Iterating / Approved / Merged]

---

## Learnings & Reflections

### Technical Skills Gained

[What you learned technically]

### Challenges Overcome

[What was hard and how you solved it]

### What I'd Do Differently Next Time

[Reflection on your process]

---

## Resources Used

- [Link to helpful documentation]
- [Tutorial or Stack Overflow post that helped]
- [GitHub issues or discussions that helped]
