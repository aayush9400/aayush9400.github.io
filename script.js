document.addEventListener("DOMContentLoaded", function() {
    const year = new Date().getFullYear();
    document.querySelector("footer p").textContent = `© ${year} Aayush Jaiswal`;
});
