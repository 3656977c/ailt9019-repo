"""
Lesson-Plan Scaffolder
A small CLI tool that turns a topic brief and notes into a structured first-draft lesson plan.
"""

def get_input(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  (Please enter a value or press Enter again to skip)")
        allow_empty = True

def build_lesson_plan():
    print("=" * 50)
    print("      LESSON-PLAN SCAFFOLDER")
    print("=" * 50)
    print()

    topic = get_input("Lesson Topic: ")
    audience = get_input("Target Audience (e.g., Year 9 students): ")
    duration = get_input("Duration (e.g., 45 mins): ")
    notes = get_input("Brief Notes / Key Ideas (comma-separated OK): ")

    print()
    print("Generating draft...")
    print()

    objectives = [
        f"Understand the core concepts of {topic}.",
        f"Apply {topic} principles in a simple exercise.",
        f"Discuss and reflect on the relevance of {topic} to {audience.lower()}."
    ]

    materials = [
        "Whiteboard / projector",
        "Handout or digital slides",
        "Practice worksheets (optional)"
    ]

    sections = [
        ("Lesson Topic", topic),
        ("Target Audience", audience),
        ("Duration", duration),
        ("Learning Objectives", "\n".join(f"  - {obj}" for obj in objectives)),
        ("Materials Needed", "\n".join(f"  - {m}" for m in materials)),
        ("Lesson Structure",
         f"""  1. Introduction (10% of time)
       - Hook: Pose a relatable question about {topic}.
       - State the learning objectives.

  2. Main Content (50% of time)
       - Explain core concepts from your notes:
         • {notes}
       - Use examples relevant to {audience}.

  3. Guided Practice (25% of time)
       - Short exercise or group discussion on {topic}.
       - Walk through one example together.

  4. Wrap-Up & Reflection (15% of time)
       - Summarise key takeaways.
       - Quick exit ticket or reflection question."""),
        ("Assessment Ideas",
         "  - Observation during guided practice\n  - Exit-ticket responses\n  - Short quiz next lesson"),
        ("Notes / Reminders",
         "  - Adjust pacing based on student responses.\n  - Prepare extra challenge questions for early finishers.")
    ]

    output_lines = []
    for title, content in sections:
        output_lines.append(f"{title}\n{'-' * len(title)}")
        output_lines.append(content)
        output_lines.append("")

    draft = "\n".join(output_lines)
    print(draft)

    save = input("Save this draft to a file? (y/n): ").strip().lower()
    if save in ("y", "yes"):
        filename = input("Filename (e.g., draft.txt): ").strip() or "lesson_draft.txt"
        filepath = filename if filename.endswith(".txt") else filename + ".txt"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(draft)
        print(f"Draft saved to: {filepath}")
    else:
        print("Draft not saved.")

    print()
    print("Done. Good luck with your lesson!")

if __name__ == "__main__":
    build_lesson_plan()
