# Integrations

This directory holds the **integration bones** for connecting the Lesson Plan Scaffolder to external services.

## Status

Nothing is wired up yet. These are placeholder modules with clear interfaces so future development has a consistent pattern to follow.

## Planned Integrations

| Service | Module | Purpose |
|---------|--------|---------|
| OpenAI / Anthropic / Local LLMs | `llm_provider.py` | Generate richer content, suggest activities, personalize plans |
| Google Drive / Dropbox / OneDrive | `cloud_storage.py` | Save and load lesson plans from the cloud |
| Canvas / Moodle / Blackboard | *(future)* | Export plans directly to LMS platforms |
| Google / Outlook Calendar | *(future)* | Schedule lessons automatically |

## How to Add an Integration

1. Create a new module in this directory.
2. Inherit from `IntegrationBase` in `base.py`.
3. Implement `validate()` and `health_check()`.
4. Add service-specific methods (e.g. `generate_content()`, `upload()`).
5. Register the integration in the app config.

## Configuration

Place API keys and tokens in:
- Environment variables (`INTEGRATION_<NAME>_KEY`)
- `config.json` in this directory (gitignored by default)

Use `IntegrationConfig` to read settings uniformly.
