/**
 * Frontend logic for the Lesson Plan Scaffolder UI.
 */

(function () {
    const form = document.getElementById('scaffold-form');
    const generateBtn = document.getElementById('generate-btn');
    const outputPlaceholder = document.getElementById('output-placeholder');
    const outputContent = document.getElementById('output-content');
    const markdownPreview = document.getElementById('markdown-preview');
    const copyBtn = document.getElementById('copy-btn');
    const downloadBtn = document.getElementById('download-btn');

    let currentMarkdown = '';
    let currentTitle = '';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const topic = document.getElementById('topic').value.trim();
        const duration = parseInt(document.getElementById('duration').value, 10);
        const notes = document.getElementById('notes').value.trim();

        if (!topic) {
            alert('Please enter a topic.');
            return;
        }

        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic, duration, notes: notes || null }),
            });

            const data = await response.json();

            if (!data.success) {
                throw new Error(data.error || 'Generation failed.');
            }

            currentMarkdown = data.markdown;
            currentTitle = data.plan.title || 'lesson_plan';

            markdownPreview.textContent = currentMarkdown;
            outputPlaceholder.classList.add('hidden');
            outputContent.classList.remove('hidden');
        } catch (err) {
            alert('Error: ' + err.message);
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Plan';
        }
    });

    copyBtn.addEventListener('click', () => {
        if (!currentMarkdown) return;
        navigator.clipboard.writeText(currentMarkdown).then(() => {
            const original = copyBtn.textContent;
            copyBtn.textContent = 'Copied!';
            setTimeout(() => (copyBtn.textContent = original), 1200);
        });
    });

    downloadBtn.addEventListener('click', async () => {
        if (!currentMarkdown) return;

        const safeName = currentTitle.replace(/[^a-z0-9\s]/gi, '').replace(/\s+/g, '_').toLowerCase();
        const filename = `${safeName || 'lesson_plan'}.md`;

        try {
            const response = await fetch('/api/export', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ markdown: currentMarkdown, filename }),
            });

            const data = await response.json();
            if (data.success) {
                const original = downloadBtn.textContent;
                downloadBtn.textContent = 'Saved!';
                setTimeout(() => (downloadBtn.textContent = original), 1200);
            } else {
                throw new Error(data.error || 'Export failed.');
            }
        } catch (err) {
            // Fallback: client-side download
            const blob = new Blob([currentMarkdown], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        }
    });
})();
