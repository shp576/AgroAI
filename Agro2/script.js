// Add your existing JavaScript code here

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Dummy authentication - Replace with actual authentication logic
    if (username === "admin" && password === "password") {
        document.getElementById("message").innerText = "Login successful!";
        // Redirect to dashboard or other page
        // window.location.href = "dashboard.html";
    } else {
        document.getElementById("message").innerText = "Invalid username or password.";
    }
});
