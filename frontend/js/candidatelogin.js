document.getElementById('candLoginForm').addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent default form submission

  const email = document.getElementById('candEmail').value;
  const password = document.getElementById('candPassword').value;

  // Prepare request body
  const requestBody = {
    email: email,
    password: password
  };

  console.log(JSON.stringify(requestBody));
  fetch('http://localhost:8080/api/v1/users/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestBody)
  })
  .then(response => {
    if (response.ok) {
      // Login successful
      alert('Login successful!');

      // Parse the response as JSON
      return response.json();
    } else {
      // Login failed
      alert('Login failed. Please check your credentials and try again.');
      throw new Error('Login failed'); // Throw an error for catch block
    }
  })
  .then(responseData => {
    // Access data from response
    const message = responseData.message;
    const userId = responseData.userId;
    const eligibleJobs = responseData.eligibleJobs;

    // Store data in browser storage (using localStorage for simplicity)
    localStorage.setItem('message', message);
    localStorage.setItem('userId', userId);
    localStorage.setItem('eligibleJobs', JSON.stringify(eligibleJobs)); // Store array as JSON string

    console.log('Login data stored in browser storage');
    window.location.href = "http://127.0.0.1:5500/candidate-profile.html"
  })
  .catch(error => {
    console.error('Error logging in:', error);
    alert('An error occurred while logging in. Please try again later.');
  });
});

