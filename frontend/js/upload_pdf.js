function uploadPdf() {
    const fileInput = document.getElementById('jobPdf');
    const file = fileInput.files[0];
  
    // Check if a file is selected
    if (!file) {
      alert('Please select a PDF file to upload.');
      return;
    }
  
    // Validate file type (optional)
    if (!file.type.startsWith('application/pdf')) {
      alert('Only PDF files are allowed.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file', file);
  
    fetch('http://localhost:8080/api/v1/file/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (response.ok) {
        response.json().then(data => {
             console.log(data);
          });
        // Handle successful upload (e.g., clear file input, display confirmation message)
        alert("file Uploaded Sucessfully, The job details will be posted soon")
      } else {
        alert('Error uploading file. Please try again.');
        // Handle upload failure (e.g., log error message)
      }
    })
    .catch(error => {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file. Please try again later.');
    });
  }
  
  // Example usage:
  const uploadButton  = document.getElementById('uploadButton');
  uploadButton.addEventListener('click', function() {
    
    uploadPdf();
  });