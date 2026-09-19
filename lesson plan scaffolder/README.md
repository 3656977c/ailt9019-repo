# Lesson Plan Scaffolder

Generate first-draft lesson plans from a short topic brief.

## Quick Start

### CLI

```bash
python main.py --topic "Introduction to Machine Learning" --duration 90
```

### Web UI

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

## Project Structure

```
lesson plan scaffolder/
├── app.py                  # Flask web server
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── scaffolder/             # Core package
│   ├── __init__.py
│   ├── parser.py           # Input parsing
│   ├── planner.py          # Plan generation logic
│   ├── template.py         # Lesson structure templates
│   └── formatter.py        # Output formatting (Markdown / text)
├── web/                    # Frontend assets
│   ├── index.html
│   ├── style.css
│   └── app.js
├── integrations/           # External service hooks (future)
│   ├── base.py
│   ├── config.py
│   ├── llm_provider.py
│   ├── cloud_storage.py
│   └── README.md
├── data/                   # Notes / datasets
├── output/                 # Generated lesson plans
└── tests/                  # Unit tests (future)
```

## Features

- Generate structured lesson plans with time allocations
- Auto-suggest learning objectives and materials
- Export to Markdown
- Minimalist web UI with copy & download
- Ready for future LLM and cloud storage integrations

## Notes

- This tool does **not** assess real students, store class rosters, or claim the draft is an accredited curriculum.
- Integration modules are placeholder stubs. See `integrations/README.md` for the planned roadmap.
