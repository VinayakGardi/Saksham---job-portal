document.getElementById('candRegistrationForm').addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission


   
  
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const phone = document.getElementById('phone').value;
    const location = document.getElementById('location').value;
    const experience = document.getElementById("experience").value;
    const education = document.getElementById("education").value;
    const age = document.getElementById("age").value;
    const category = document.getElementById("category").value;

    // Prepare form data


    const requestBody = {
        name: fullName,
        email: email,
        password:password,
        phone_number:phone,
        location:location,
        experience:experience,
        education:education,
        age:age,
        category:category,
        eligible_jobs:["null"]
    };


    // Make API call to register user
    fetch('http://localhost:8080/api/v1/users/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    })
    .then(response => {
        if (response.ok) {
            // Registration successful
            alert('Registration successful!');
            // You can handle further actions here, such as redirecting the user
        } else {
            // Registration failed
            alert('Registration failed. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error registering user:', error);
        alert('An error occurred while registering. Please try again later.');
    });
});