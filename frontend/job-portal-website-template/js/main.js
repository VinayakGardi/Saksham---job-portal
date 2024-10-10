(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    // Validation functions
    var validateName = function(name) {
        // Check if name is not empty
        return name.trim() !== '';
    };

    var validateEmail = function(email) {
        // Check if email is valid using a regular expression
        var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    };

    var validatePassword = function(password) {
        // Check if password is at least 6 characters long
        return password.length >= 6;
    };

    var validatePhone = function(phone) {
        // Check if phone number is valid using a regular expression
        var phonePattern = /^\d{10}$/;
        return phonePattern.test(phone);
    };

    var validateLocation = function(location) {
        // Check if location is not empty
        return location.trim() !== '';
    };

    var validateExperience = function() {
        // Check if either of the radio buttons is checked
        return $('#experienceFresher').is(':checked') || $('#experienceExperienced').is(':checked');
    };

    var validateResume = function(resume) {
        // Check if a file is selected
        return resume !== null;
    };

    // Form submission handler
    $('form').submit(function(e) {
        e.preventDefault(); // Prevent default form submission
        
        // Get form values
        var name = $('#fullName').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var phone = $('#phone').val();
        var location = $('#location').val();
        var isFresher = $('#experienceFresher').is(':checked');
        var isExperienced = $('#experienceExperienced').is(':checked');
        var resume = $('#resume').prop('files')[0];

        // Validate form fields
        if (!validateName(name)) {
            alert('Please enter your name.');
            return;
        }
        if (!validateEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }
        if (!validatePassword(password)) {
            alert('Password must be at least 6 characters long.');
            return;
        }
        if (!validatePhone(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }
        if (!validateLocation(location)) {
            alert('Please enter your location.');
            return;
        }
        if (!validateExperience()) {
            alert('Please select your experience.');
            return;
        }
        if (!validateResume(resume)) {
            alert('Please upload your resume.');
            return;
        }

        // If all fields are valid, proceed with form submission
        // You can submit the form using AJAX or perform any other action here
        alert('Form submitted successfully!');
    });

    // Initiate the wowjs
    new WOW().init();

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
    //candidateProfile

    $(document).ready(function() {
        // Assume user data is retrieved from server-side script and stored in userData object
        var userData = {
            fullName: "John Doe",
            email: "john.doe@example.com",
            mobile: "123-456-7890",
            location: "New York",
            experience: "5 years",
            resumeLink: "path_to_resume.pdf" // Update with actual path to resume
            // Add more user data properties here as needed
        };

        // Populate form fields with user data
        $('#fullName').val(userData.fullName);
        $('#email').val(userData.email);
        $('#mobile').val(userData.mobile);
        $('#location').val(userData.location);
        $('#experience').val(userData.experience);
        $('#resume').attr('href', userData.resumeLink);

        // Example of populating basic info fields
        $('#userId').text(userData.userId);
        $('#candidateName').text(userData.candidateName);
        $('#profession').text(userData.profession);
    });

})(jQuery);
