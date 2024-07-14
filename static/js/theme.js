// Function to set the current theme in localStorage
function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

// Function to toggle between themes
function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : currentTheme === 'dark' ? 'high-contrast' : 'light';
    setTheme(newTheme);
}

// Check the localStorage and set the theme on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
});

// Event listener for theme toggle button
document.querySelector('#theme-toggle').addEventListener('click', toggleTheme);
