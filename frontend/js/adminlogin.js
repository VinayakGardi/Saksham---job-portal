const adminLoginForm = document.getElementById('adminLoginForm');
const adminEmailInput = document.getElementById('adminEmail');
const adminPasswordInput = document.getElementById('adminPassword');

adminLoginForm.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission

  // Get email and password values
  const email = adminEmailInput.value.trim();
  const password = adminPasswordInput.value.trim();

  // Basic validation (optional)
  if (!email || !password) {
    alert('Please enter your email and password.');
    return;
  }

  // Create the login data object
  const loginData = {
    email,
    password
  };

  // Send the login request using fetch API
  try {
    const response = await fetch('http://localhost:8080/api/v1/admin/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // Set content type for JSON data
      },
      body: JSON.stringify(loginData) // Convert login data to JSON string
    });

    if (response.ok) {
      const responseData = await response.json(); // Parse response as JSON
      
        // Successful login
        console.log('Login successful!');

       
        window.location.href = '/admin-profile-pdf-upload.html'; // Redirect to dashboard (replace with desired URL)
      
    } else {
      // Network error or unexpected response
      console.error('Error during login request:', response.statusText);
      alert('invalid email or password');
    }
  } catch (error) {
    // Handle other errors
    console.error('Error in login process:', error);
    alert('An unexpected error occurred. Please try again.');
  }
});