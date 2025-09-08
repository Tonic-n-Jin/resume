/**
 * Fetches HTML content from a file and injects it into a specified element.
 * @param {string} url - The path to the HTML file to include.
 * @param {string} elementId - The ID of the element to inject the content into.
 */
async function includeHTML(url, elementId) {
    const element = document.getElementById(elementId);
    if (!element) {
        console.error(`Element with ID "${elementId}" not found.`);
        return;
    }
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
        }
        const text = await response.text();
        element.innerHTML = text;
        element.classList.remove('placeholder'); // Optional: remove placeholder styling
    } catch (error) {
        console.error(`Error loading HTML from ${url}:`, error);
        element.innerHTML = `<p class="text-red-500">Could not load content from ${url}.</p>`;
    }
}

// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
    // Load all the HTML partials into their respective placeholders
    includeHTML('docs/header.html', 'header-placeholder');
    includeHTML('docs/side.html', 'side-placeholder');
    includeHTML('docs/main.html', 'main-placeholder');
    includeHTML('docs/footer.html', 'footer-placeholder');
});