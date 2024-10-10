const adminRegistrationForm = document.getElementById('adminRegistrationForm');
const adminFullNameInput = document.getElementById('adminFullName');
const adminEmailInput = document.getElementById('adminEmail');
const adminPasswordInput = document.getElementById('adminPassword');

adminRegistrationForm.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission

  // Get full name, email, and password values
  const fullName = adminFullNameInput.value.trim();
  const email = adminEmailInput.value.trim();
  const password = adminPasswordInput.value.trim();

  // Basic validation (optional)
  if (!fullName || !email || !password) {
    alert('Please fill in all required fields.');
    return;
  }

  // Create the registration data object
  const registrationData = {
    fullName,
    email,
    password
  };

  // Send the registration request using fetch API
  try {
    const response = await fetch('http://localhost:8080/api/v1/admin/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // Set content type for JSON data
      },
      body: JSON.stringify(registrationData) // Convert registration data to JSON string
    });

    if (response.ok) {
      const responseData = await response.json(); // Parse response as JSON
      
        // Successful registration
        console.log('Registration successful!');

        
        alert('Registration successful! You can now log in.');
        window.location.href = '/admin-login.html'
        adminRegistrationForm.reset(); 
      
    } else {
      // Network error or unexpected response
      console.error('Error during registration request:', response.statusText);
      alert('Email Already Exist');
    }
  } catch (error) {
    // Handle other errors
    console.error('Error in registration process:', error);
    alert('An unexpected error occurred. Please try again.');
  }
});
