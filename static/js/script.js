// Select the hamburger menu button and nav links
const menuButton = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");
// Add click event to the menu button
menuButton.addEventListener("click", function () {
    navLinks.classList.toggle("active");


});