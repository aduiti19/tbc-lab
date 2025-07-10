// Form validation script for contact.html

function validateForm() {
    // Get form field values
    const name = document.forms["contactForm"]["name"].value.trim();
    const email = document.forms["contactForm"]["email"].value.trim();
    const message = document.forms["contactForm"]["message"].value.trim();
    
    // Name validation
    if (name === "") {
        alert("Please enter your name.");
        return false;
    }

    // Email validation (simple regex)
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === "" || !emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Message validation
    if (message === "") {
        alert("Please enter your message.");
        return false;
    }

    // If everything is valid
    alert("Thank you for your message!");
    return true;
}