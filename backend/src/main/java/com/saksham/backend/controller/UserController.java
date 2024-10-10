package com.saksham.backend.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.saksham.backend.entities.User;
import com.saksham.backend.exceptions.UserAlreadyExistException;
import com.saksham.backend.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/v1/users")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/register")
    private String registerUser(@RequestBody User user) {
        if (userService.findByEmail(user.getEmail()) != null) {
            // Email already exists, handle the case (e.g., inform user)
            return ("Email already exists");
        }
        userService.registerUser(user);
        return user.toString();
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody User user) throws JsonProcessingException {
        System.out.println(user.toString());
        if (userService.authenticateUser(user.getEmail(), user.getPassword())) {
            User loggedInUser = userService.findByEmail(user.getEmail());
            Map<String, String> response = new HashMap<>();
            response.put("message", "Login successful");
            response.put("userId", loggedInUser.get_Id());


            List<String> jobs = loggedInUser.getEligible_jobs();
            String eligibleJobsJson = jobs.isEmpty() ? "[]" : new ObjectMapper().writeValueAsString(jobs);
            response.put("eligible jobs", eligibleJobsJson);

            ObjectMapper mapper = new ObjectMapper();
            String responseJson = mapper.writeValueAsString(response);

            return ResponseEntity.ok(responseJson);
        } else {
            // Invalid credentials
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid email or password");
        }
    }


}