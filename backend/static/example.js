//  Get today's date
const today = new Date();
const formattedDate = today.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});
// Put it in the HTML
document.getElementById('current-date').textContent = formattedDate;