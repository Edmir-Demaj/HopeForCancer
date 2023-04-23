document.addEventListener("DOMContentLoaded", function () {
  // add class active to home page
  document.getElementById("home").classList.add("active");
});

// Get all elements with class="nav-link"
let navLinks = document.getElementsByClassName("nav-link");

// Loop through the nav-links and add the active class onclick
for (let i = 0; i < navLinks.length; i++) {
  navLinks[i].addEventListener("click", function () {
    let current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
