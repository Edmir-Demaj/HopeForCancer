//Select back to top button
let topButton = document.getElementById("top-btn");

// Add an event listener to window object on scroll
window.addEventListener("scroll", showButton);

function showButton() {
  // code for all browsers and for safari to hide or display btn
  if (document.body.scrollTop > 850 || document.documentElement.scrollTop > 850) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
}

// function that bring to top of page when btn is clicked
function moveTop() {
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  document.body.scrollTop = 0; // For Safari
}
