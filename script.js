// Custom JavaScript

document.addEventListener("DOMContentLoaded", function () {
  console.log("Page loaded!");

  // Handle CTA button click
  const ctaButton = document.getElementById("cta-button");
  if (ctaButton) {
    ctaButton.addEventListener("click", function () {
      console.log("CTA button clicked");
      alert("Welcome! This is your starting point.");
    });
  }
});
